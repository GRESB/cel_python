import logging
from .parser.CELVisitor import CELVisitor
from .context import Context
from typing import Any, Dict, Optional, List
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TypeChecker(CELVisitor):
    def __init__(self, context: Context):
        super().__init__()
        if not isinstance(context, Context):
            raise ValueError("TypeChecker requires a Context object")

        self.context = context
        self.functionSignatures: Dict[str, Dict[str, Any]] = {
            # Arithmetic Functions
            "min": {"args": ["int"], "varArgs": True, "returnType": "int"},
            "max": {"args": ["int"], "varArgs": True, "returnType": "int"},
            "abs": {"args": ["int"], "returnType": "int"},
            "ceil": {"args": ["float"], "returnType": "int"},
            "floor": {"args": ["float"], "returnType": "int"},
            "round": {"args": ["float"], "returnType": "int"},
            # String Functions
            "contains": {"args": ["string", "string"], "returnType": "bool"},
            "endsWith": {"args": ["string", "string"], "returnType": "bool"},
            "indexOf": {"args": ["string", "string"], "returnType": "int"},
            "length": {"args": ["string"], "returnType": "int"},
            "lower": {"args": ["string"], "returnType": "string"},
            "replace": {"args": ["string", "string", "string"], "returnType": "string"},
            "split": {"args": ["string", "string"], "returnType": "list<any>"},
            "startsWith": {"args": ["string", "string"], "returnType": "bool"},
            "upper": {"args": ["string"], "returnType": "string"},
            # List Functions
            "size": {"args": [["string", "list<any>", "map<any, any>"]], "returnType": "int"},

            # Type Conversion Functions
            "int": {"args": ["any"], "returnType": "int"},
            "uint": {"args": ["any"], "returnType": "int"},
            "double": {"args": ["any"], "returnType": "float"},
            "string": {"args": ["any"], "returnType": "string"},
            "bool": {"args": ["any"], "returnType": "bool"},
            # Null Handling Functions
            "exists": {"args": ["any"], "returnType": "bool"},
            "existsOne": {"args": ["list<any>"], "returnType": "bool"},
            # Date/Time Functions
            "duration": {"args": ["int"], "returnType": "duration"},
            "timestamp": {"args": ["string"], "returnType": "timestamp"},
            "time": {"args": ["int", "int", "int", "int", "int", "int", "int"], "returnType": "timestamp"},
            "date": {"args": ["int", "int", "int"], "returnType": "date"},
            "getFullYear": {"args": ["timestamp"], "returnType": "int"},
            "getMonth": {"args": ["timestamp"], "returnType": "int"},
            "getDate": {"args": ["timestamp"], "returnType": "int"},
            "getHours": {"args": ["timestamp"], "returnType": "int"},
            "getMinutes": {"args": ["timestamp"], "returnType": "int"},
            "getSeconds": {"args": ["timestamp"], "returnType": "int"},
            "has": {"args": ["list<any>", "any"], "returnType": "bool"},
        }

    def visitStart(self, ctx: Any) -> Any:
        return self.visit(ctx.expr())

    def visitExpr(self, ctx: Any) -> Any:
        return self.visit(ctx.getChild(0))

    def visitConditionalOr(self, ctx: Any) -> str:
        result_type = self.visit(ctx.conditionalAnd(0))
        logger.debug(f"ConditionalOr: Initial type '{result_type}'")
        for i in range(1, len(ctx.conditionalAnd())):
            next_type = self.visit(ctx.conditionalAnd(i))
            logger.debug(f"ConditionalOr: Comparing '{result_type}' || '{next_type}'")
            if result_type != "bool" or next_type != "bool":
                raise ValueError(f"Logical '||' requires boolean operands, but got '{result_type}' and '{next_type}'")
            result_type = "bool"
        logger.debug(f"ConditionalOr: Final type '{result_type}'")
        return result_type

    def visitConditionalAnd(self, ctx: Any) -> str:
        result_type = self.visit(ctx.relation(0))
        logger.debug(f"ConditionalAnd: Initial type '{result_type}'")
        for i in range(1, len(ctx.relation())):
            next_type = self.visit(ctx.relation(i))
            logger.debug(f"ConditionalAnd: Comparing '{result_type}' && '{next_type}'")
            if result_type != "bool" or next_type != "bool":
                raise ValueError(f"Logical '&&' requires boolean operands, but got '{result_type}' and '{next_type}'")
            result_type = "bool"
        logger.debug(f"ConditionalAnd: Final type '{result_type}'")
        return result_type

    def visitRelationOp(self, ctx: Any) -> str:
        left_type = self.visit(ctx.relation(0))
        operator = ctx.op.text
        right_type = self.visit(ctx.relation(1))

        logger.debug(f"RelationOp: {left_type} {operator} {right_type}")

        normalized_left = self.__normalizeType(left_type)
        normalized_right = self.__normalizeType(right_type)

        logger.debug(f"RelationOp: Normalized types '{normalized_left}' and '{normalized_right}'")

        if operator in ["==", "!="]:
            if not self.are_types_compatible(normalized_left, normalized_right):
                raise ValueError(
                    f"Mismatching types: Cannot compare '{normalized_left}' and '{normalized_right}' with '{operator}'"
                )
        elif operator in ["<", "<=", ">", ">="]:
            if not self.are_types_compatible(normalized_left, normalized_right):
                raise ValueError(
                    f"Mismatching types: Cannot compare '{normalized_left}' and '{normalized_right}' with '{operator}'"
                )
            if normalized_left not in ["int", "float", "any"]:
                raise ValueError(
                    f"Operator '{operator}' requires numeric operands, but got '{normalized_left}' and '{normalized_right}'"
                )
        elif operator == "in":
            if not self.is_list_type(normalized_right):
                raise ValueError(f"Operator 'in' requires a list on the right-hand side, but got '{normalized_right}'")
        else:
            raise ValueError(f"Unknown operator '{operator}'")

        logger.debug("RelationOp: Type 'bool' returned")
        return "bool"

    def visitRelationCalc(self, ctx: Any) -> str:
        return self.visit(ctx.getChild(0))

    def visitCalcAddSub(self, ctx: Any) -> str:
        left_type = self.visit(ctx.getChild(0))
        left_type = self.__normalizeType(left_type)
        logger.debug(f"CalcAddSub: Left type '{left_type}'")

        i = 1
        while i < ctx.getChildCount():
            operator = ctx.getChild(i).getText()
            right_type = self.visit(ctx.getChild(i + 1))
            right_type = self.__normalizeType(right_type)
            logger.debug(f"CalcAddSub: Operator '{operator}' with right type '{right_type}'")

            operators = ["+", "-"]
            possibleTypesAdd = ["int", "float", "string"]
            possibleTypesSub = ["int", "float"]

            if operator not in operators:
                raise ValueError(f"Unknown operator '{operator}'")

            if not self.are_types_compatible(left_type, right_type):
                raise ValueError(
                    f"Operator '{operator}' requires matching types, but got '{left_type}' and '{right_type}'"
                )
            if operator == "+" and left_type not in possibleTypesAdd:
                raise ValueError(
                    f"Operator '+' requires int, float, or string, but got '{left_type}'"
                )
            if operator == "-" and left_type not in possibleTypesSub:
                raise ValueError(
                    f"Operator '-' requires int or float, but got '{left_type}'"
                )
            i += 2

        logger.debug(f"CalcAddSub: Final type '{left_type}'")
        return left_type

    def visitCalcMulDiv(self, ctx: Any) -> str:
        left_type = self.visit(ctx.getChild(0))
        left_type = self.__normalizeType(left_type)
        operator = ctx.getChild(1).getText()
        right_type = self.visit(ctx.getChild(2))
        right_type = self.__normalizeType(right_type)

        logger.debug(f"CalcMulDiv: {left_type} {operator} {right_type}")

        operators = ["*", "/", "%"]
        possibleCalcMulDivTypes = ["int", "float"]

        if operator not in operators:
            raise ValueError(f"Unknown operator '{operator}'")

        if not self.are_types_compatible(left_type, right_type) or left_type not in possibleCalcMulDivTypes:
            raise ValueError(
                f"Operator '{operator}' requires matching numeric operands, but got '{left_type}' and '{right_type}'"
            )

        logger.debug(f"CalcMulDiv: Final type '{left_type}'")
        return left_type

    def visitLogicalNot(self, ctx: Any) -> str:
        expr_type = self.visit(ctx.getChild(1))
        expr_type = self.__normalizeType(expr_type)
        logger.debug(f"LogicalNot: !{expr_type}")

        if expr_type != "bool":
            raise ValueError(f"Logical '!' requires boolean operand, but got '{expr_type}'")
        return "bool"

    def visitNegate(self, ctx: Any) -> str:
        expr_type = self.visit(ctx.getChild(1))
        expr_type = self.__normalizeType(expr_type)
        logger.debug(f"Negate: -{expr_type}")

        if expr_type not in ["int", "float"]:
            raise ValueError(f"Negation requires numeric operand, but got '{expr_type}'")
        return expr_type

    def visitIdentOrGlobalCall(self, ctx: Any) -> str:
        ident = ctx.getChild(0).getText()
        logger.debug(f"IdentOrGlobalCall: {ident}")

        if ctx.LPAREN():
            # Function call
            args = self.visit(ctx.exprList()) if ctx.exprList() else []
            signature = self.functionSignatures.get(ident)
            if not signature:
                raise ValueError(f"Function '{ident}' is not defined")
            required_arg_count = len(signature["args"])
            var_args = signature.get("varArgs", False)

            if var_args and len(args) < required_arg_count:
                raise ValueError(
                    f"Function '{ident}' expects at least {required_arg_count} arguments, but got {len(args)}"
                )
            elif not var_args and len(args) != required_arg_count:
                raise ValueError(
                    f"Function '{ident}' expects {required_arg_count} arguments, but got {len(args)}"
                )

            for i, arg in enumerate(args):
                expected_types = signature["args"][0] if var_args else signature["args"][i]
                if isinstance(expected_types, list):
                    if not any(self.is_type_compatible(arg, etype) for etype in expected_types):
                        raise ValueError(
                            f"Argument {i+1} of function '{ident}' expects type '{expected_types}', but got '{arg}'"
                        )
                else:
                    if not self.is_type_compatible(arg, expected_types):
                        raise ValueError(
                            f"Argument {i+1} of function '{ident}' expects type '{expected_types}', but got '{arg}'"
                        )
            logger.debug(f"IdentOrGlobalCall: Function '{ident}' validated successfully")
            return signature["returnType"]
        else:
            # Variable
            var_type = self.context.getType(ident)
            if var_type is None:
                variable_value = self.context.getVariable(ident)
                if self.context.hasVariable(ident):
                    if variable_value is not None:
                        var_type = self.__getType(variable_value)
                        self.context.setType(ident, var_type)
                    else:
                        var_type = 'null'
                        self.context.setType(ident, var_type)
                else:
                    raise ValueError(f"Variable '{ident}' is not defined")
            logger.debug(f"Variable '{ident}' has type '{var_type}'")
            return var_type

    def visitExprList(self, ctx: Any) -> List[str]:
        types = []
        for i in range(ctx.getChildCount()):
            if i % 2 == 0:  # expressions are at even indices
                expr_type = self.visit(ctx.getChild(i))
                types.append(expr_type)
        logger.debug(f"ExprList Types: {types}")
        return types

    def visitRelationCalc(self, ctx: Any) -> str:
        return self.visit(ctx.getChild(0))

    def visitFieldInitializerList(self, ctx: Any) -> Dict[str, str]:
        fields = {}
        for i in range(len(ctx.IDENTIFIER())):
            field = ctx.IDENTIFIER(i).text
            value_type = self.visit(ctx.expr(i))
            fields[field] = self.__normalizeType(value_type)
        logger.debug(f"FieldInitializerList Types: {fields}")
        return fields

    def visitMapInitializerList(self, ctx: Any) -> str:
        logger.debug("MapInitializerList: Returning 'map<any, any>'")
        return "map<any, any>"

    def visitInt(self, ctx: Any) -> str:
        logger.debug("Constant Literal: int")
        return "int"

    def visitDouble(self, ctx: Any) -> str:
        logger.debug("Constant Literal: float")
        return "float"

    def visitString(self, ctx: Any) -> str:
        logger.debug("Constant Literal: string")
        return "string"

    def visitBoolTrue(self, ctx: Any) -> str:
        logger.debug("Constant Literal: bool")
        return "bool"

    def visitBoolFalse(self, ctx: Any) -> str:
        logger.debug("Constant Literal: bool")
        return "bool"

    def visitNull(self, ctx: Any) -> str:
        logger.debug("Constant Literal: null")
        return "null"

    def visitMemberExpr(self, ctx):
        return self.visit(ctx.member())

    def visitPrimaryExpr(self, ctx):
        return self.visit(ctx.primary())

    def visitNested(self, ctx):
        # '(' expr ')'
        return self.visit(ctx.expr())

    def visitCreateList(self, ctx):
        # '[' exprList? ']'
        if ctx.exprList():
            types = self.visit(ctx.exprList())
            return "list<any>"
        else:
            return "list<any>"

    def visitCreateStruct(self, ctx):
        if ctx.mapInitializerList():
            return "map<any, any>"
        return "map<any, any>"

    def visitConstantLiteral(self, ctx):
        return self.visit(ctx.literal())

    def visitSelectOrCall(self, ctx):
        base_type = self.visit(ctx.member())

        identifier_node = ctx.IDENTIFIER()
        prop_or_func = identifier_node.getText() if identifier_node else None

        if ctx.LPAREN() and ctx.RPAREN():
            return "any"
        else:
            if base_type in ["map<any, any>", "any"]:
                return "any"
            
            return "any"

    def visitIndex(self, ctx):
        base_type = self.visit(ctx.member()) 
        return "any"

    def visitCreateMessage(self, ctx):
        return self.visitChildren(ctx)
    

    def __getType(self, value: Any) -> str:
        if value is None:
            return 'null'

        if isinstance(value, list):
            element_types = {self.__getType(elem) for elem in value}
            if len(element_types) == 1:
                return f"list<{element_types.pop()}>"
            else:
                return "list<any>"

        if isinstance(value, bool):
            return "bool"
        if isinstance(value, int):
            return "int"
        if isinstance(value, float):
            return "float"
        if isinstance(value, str):
            return "string"
        if isinstance(value, dict):
            return "map<any, any>"
        if isinstance(value, datetime):
            return "timestamp"

    def is_type_compatible(self, arg_type: str, expected_type: str) -> bool:
        logger.debug(f"Checking compatibility: arg_type='{arg_type}' vs expected_type='{expected_type}'")
        if expected_type == 'any':
            logger.debug("Type 'any' is compatible with any type.")
            return True
        if expected_type.startswith('list<') and expected_type.endswith('>'):
            compatible = arg_type.startswith('list<') and arg_type.endswith('>')
            logger.debug(f"'list<any>' compatibility with '{arg_type}': {compatible}")
            return compatible
        if expected_type.startswith('map<') and expected_type.endswith('>'):
            compatible = arg_type.startswith('map<') and arg_type.endswith('>')
            logger.debug(f"'map<any, any>' compatibility with '{arg_type}': {compatible}")
            return compatible
        # Add more compatibility rules as needed
        compatible = arg_type == expected_type
        logger.debug(f"Type '{arg_type}' compatibility with '{expected_type}': {compatible}")
        return compatible

    def are_types_compatible(self, type1: str, type2: str) -> bool:        
        if type1 == 'any' or type2 == 'any':
            return True
        return self.is_type_compatible(type1, type2) and self.is_type_compatible(type2, type1)

    def is_list_type(self, type_: str) -> bool:
        return type_.startswith("list<") and type_.endswith(">")

    def __normalizeType(self, input_type: Any) -> str:
        logger.debug(f"Normalizing type: {input_type} (type: {type(input_type).__name__})")
        if isinstance(input_type, str):
            normalized = input_type.strip()
            logger.debug(f"Normalized type (str): '{normalized}'")
            return normalized
        elif isinstance(input_type, list):
            flat_array = []
            for item in input_type:
                if isinstance(item, list):
                    flat_array.extend(item)
                else:
                    flat_array.append(item)

            # Filter out empty/None
            flat_array = [x for x in flat_array if x is not None and x != '']
            unique_types = list(set(flat_array))

            logger.debug(f"Flattened types: {flat_array}")
            logger.debug(f"Unique types after flattening: {unique_types}")

            if len(unique_types) == 1:
                logger.debug(f"Single unique type: '{unique_types[0]}'")
                return unique_types[0]
            elif len(unique_types) == 0:
                logger.debug("No types found after normalization. Returning 'unknown'")
                return "unknown"
            else:
                logger.debug("Multiple types found after normalization. Returning 'unknown'")
                return "unknown"
        else:
            logger.error(f"Unsupported input type: {type(input_type).__name__}")
            raise ValueError(f"Unsupported input type: <class '{type(input_type).__name__}'>")
