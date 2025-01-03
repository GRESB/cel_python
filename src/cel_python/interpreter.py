import logging
from antlr4 import *
from .parser.CELParser import CELParser
from .parser.CELVisitor import CELVisitor
from datetime import datetime, timezone, date
from .context import Context
import math

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Interpreter(CELVisitor):
    def __init__(self, context: Context):
        self.context = context
        self.function_registry = {
            # Arithmetic Functions
            "min": min,
            "max": max,
            "abs": abs,
            "ceil": math.ceil,
            "floor": math.floor,
            "round": self.round_half_away_from_zero, 

            # String Functions
            "contains": lambda s, substr: substr in s,
            "endsWith": lambda s, suffix: s.endswith(suffix),
            "indexOf": lambda s, substr: s.find(substr),
            "length": len,
            "lower": str.lower,
            "upper": str.upper,
            "replace": lambda s, substr, replacement: s.replace(substr, replacement),
            "split": lambda s, separator: s.split(separator),
            "startsWith": lambda s, prefix: s.startswith(prefix),

            # List Functions
            "size": lambda lst: len(lst),

            # Type Conversion Functions
            "int": int,
            "uint": lambda x: max(0, int(x)),
            "double": float,
            "string": str,
            "bool": bool,

            # Null Handling Functions
            "exists": lambda x: x is not None,
            "existsOne": lambda lst: sum(1 for item in lst if item is not None) >= 1,

            # Date/Time Functions
            "duration": lambda seconds: f"{seconds}s",
            "timestamp": lambda: datetime.now(timezone.utc),
            "time": lambda year, month, day, hour, minute, second, millisecond: datetime(
                year, month, day, hour, minute, second, millisecond * 1000, tzinfo=timezone.utc
            ),

            "date": lambda year, month, day: date(year, month, day),
            "getFullYear": lambda timestamp: timestamp.year if isinstance(timestamp, datetime) else None,
            "getMonth": lambda timestamp: timestamp.month - 1 if isinstance(timestamp, datetime) else None,  # 0-indexed
            "getDate": lambda timestamp: timestamp.day if isinstance(timestamp, datetime) else None,
            "getHours": lambda timestamp: timestamp.hour if isinstance(timestamp, datetime) else None,
            "getMinutes": lambda timestamp: timestamp.minute if isinstance(timestamp, datetime) else None,
            "getSeconds": lambda timestamp: timestamp.second if isinstance(timestamp, datetime) else None,
        }

    def round_half_away_from_zero(self, x):
        if x > 0:
            return math.floor(x + 0.5)
        elif x < 0:
            return math.ceil(x - 0.5)
        else:
            return 0

    def visitStart(self, ctx: CELParser.StartContext):
        return self.visit(ctx.expr())

    def visitExpr(self, ctx: CELParser.ExprContext):
        return self.visit(ctx.getChild(0))

    def visitConditionalOr(self, ctx: CELParser.ConditionalOrContext):
        result = self.visit(ctx.conditionalAnd(0))
        logger.debug(f"ConditionalOr: Initial result '{result}'")
        for i in range(1, len(ctx.conditionalAnd())):
            next_result = self.visit(ctx.conditionalAnd(i))
            logger.debug(f"ConditionalOr: OR with '{next_result}'")
            result = result or next_result
        logger.debug(f"ConditionalOr: Final result '{result}'")
        return result

    def visitConditionalAnd(self, ctx: CELParser.ConditionalAndContext):
        result = self.visit(ctx.relation(0))
        logger.debug(f"ConditionalAnd: Initial result '{result}'")
        for i in range(1, len(ctx.relation())):
            next_result = self.visit(ctx.relation(i))
            logger.debug(f"ConditionalAnd: AND with '{next_result}'")
            result = result and next_result
        logger.debug(f"ConditionalAnd: Final result '{result}'")
        return result

    def visitRelationOp(self, ctx: CELParser.RelationOpContext):
        left = self.visit(ctx.relation(0))
        operator = ctx.op.text
        right = self.visit(ctx.relation(1))
        logger.debug(f"RelationOp Evaluation: {left} {operator} {right}")

        if operator == "==":
            return left == right
        elif operator == "!=":
            return left != right
        elif operator == "<":
            return left < right
        elif operator == "<=":
            return left <= right
        elif operator == ">":
            return left > right
        elif operator == ">=":
            return left >= right
        elif operator == "in":
            if isinstance(right, list):
                return left in right
            else:
                raise Exception(f"Invalid operation: 'in' applied to non-list.")
        else:
            raise Exception(f"Unknown operator: {operator}")

    def visitRelationCalc(self, ctx: CELParser.RelationCalcContext):
        return self.visit(ctx.getChild(0))

    def visitCalcAddSub(self, ctx: CELParser.CalcAddSubContext):
        result = self.visit(ctx.getChild(0))
        logger.debug(f"CalcAddSub: Initial result '{result}'")
        for i in range(1, ctx.getChildCount(), 2):
            operator = ctx.getChild(i).getText()
            right = self.visit(ctx.getChild(i + 1))
            logger.debug(f"CalcAddSub Operation: '{result}' {operator} '{right}'")
            if operator == "+":
                result += right
            elif operator == "-":
                result -= right
            else:
                raise Exception(f"Unknown operator: {operator}")
            logger.debug(f"CalcAddSub: Updated result '{result}'")
        return result

    def visitCalcMulDiv(self, ctx: CELParser.CalcMulDivContext):
        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))
        logger.debug(f"CalcMulDiv Operation: '{left}' {operator} '{right}'")

        if operator == "*":
            return left * right
        elif operator == "/":
            return left / right
        elif operator == "%":
            return left % right
        else:
            raise Exception(f"Unknown operator: {operator}")

    def visitLogicalNot(self, ctx: CELParser.LogicalNotContext):
        value = self.visit(ctx.getChild(1))
        logger.debug(f"LogicalNot Evaluation: !{value}")
        return not value

    def visitNegate(self, ctx: CELParser.NegateContext):
        value = self.visit(ctx.getChild(1))
        logger.debug(f"Negate Evaluation: -{value}")
        return -value

    def visitMember(self, ctx: CELParser.MemberContext):
        if ctx.primary():
            return self.visit(ctx.primary())

        elif ctx.DOT() and ctx.IDENTIFIER():
            target = self.visit(ctx.member())
            member_name = ctx.IDENTIFIER().getText()
            if ctx.LPAREN() and ctx.RPAREN():
                args = self.visit(ctx.exprList()) if ctx.exprList() else []
                func = self.function_registry.get(member_name)
                if callable(func):
                    try:
                        result = func(target, *args)
                        logger.debug(f"Function '{member_name}' executed with result '{result}'")
                        return result
                    except Exception as e:
                        raise Exception(f"Error executing function '{member_name}': {e}")
                else:
                    raise Exception(f"'{member_name}' is not a function")
            else:
                if isinstance(target, dict):
                    return target.get(member_name)
                elif hasattr(target, member_name):
                    return getattr(target, member_name)
                else:
                    raise Exception(f"Member '{member_name}' not found on '{target}'")

        elif ctx.LBRACKET() and ctx.RBRACKET():
            target = self.visit(ctx.member())
            index = self.visit(ctx.expr())
            logger.debug(f"List Indexing: '{target}'[{index}]")
            return target[index]

        elif ctx.LBRACE() and ctx.RBRACE():
            obj = {}
            if ctx.fieldInitializerList():
                fields = self.visit(ctx.fieldInitializerList())
                obj.update(fields)
            logger.debug(f"Map Initialization: {obj}")
            return obj

        else:
            raise Exception("Unexpected member structure")

    def visitMemberExpr(self, ctx: CELParser.MemberExprContext):
        return self.visit(ctx.member())

    def visitPrimaryExpr(self, ctx: CELParser.PrimaryExprContext):
        return self.visitPrimary(ctx.primary())

    def visitConstantLiteral(self, ctx: CELParser.ConstantLiteralContext):
        return self.visit(ctx.literal())

    def visitPrimary(self, ctx: CELParser.PrimaryContext):
        if isinstance(ctx, CELParser.IdentOrGlobalCallContext):
            return self.visitIdentOrGlobalCall(ctx)
        elif isinstance(ctx, CELParser.NestedContext):
            return self.visit(ctx.expr())
        elif isinstance(ctx, CELParser.CreateListContext):
            return self.visit(ctx.exprList()) if ctx.exprList() else []
        elif isinstance(ctx, CELParser.CreateStructContext):
            if ctx.mapInitializerList():
                return self.visit(ctx.mapInitializerList())
            else:
                return {}
        elif isinstance(ctx, CELParser.ConstantLiteralContext):
            return self.visit(ctx.literal())
        else:
            return None

    def visitIdentOrGlobalCall(self, ctx: CELParser.IdentOrGlobalCallContext):
        identifier = ctx.IDENTIFIER().getText()
        logger.debug(f"IdentOrGlobalCall: '{identifier}'")

        if ctx.LPAREN():
            # Function call
            args = self.visit(ctx.exprList()) if ctx.exprList() else []
            func = self.function_registry.get(identifier)
            if callable(func):
                try:
                    result = func(*args)
                    logger.debug(f"Function '{identifier}' executed with result '{result}'")
                    return result
                except Exception as e:
                    raise Exception(f"Error executing function '{identifier}': {e}")
            else:
                raise Exception(f"Function '{identifier}' is not defined")
        else:
            # Variable
            if not self.context.hasVariable(identifier):
                raise Exception(f"Variable '{identifier}' is not defined")
            value = self.context.getVariable(identifier)
            logger.debug(f"Variable '{identifier}' accessed with value '{value}'")
            return value

    def visitExprList(self, ctx: CELParser.ExprListContext):
        args = [self.visit(expr) for expr in ctx.expr()]
        logger.debug(f"ExprList Evaluated Args: {args}")
        return args

    def visitFieldInitializerList(self, ctx: CELParser.FieldInitializerListContext):
        fields = {}
        for i in range(len(ctx.IDENTIFIER())):
            field = ctx.IDENTIFIER(i).text
            value = self.visit(ctx.expr(i))
            fields[field] = value
            logger.debug(f"FieldInitializer: '{field}' = '{value}'")
        return fields

    def visitMapInitializerList(self, ctx: CELParser.MapInitializerListContext):
        map_ = {}
        for i in range(0, len(ctx.expr()), 2):
            key = self.visit(ctx.expr(i))
            value = self.visit(ctx.expr(i + 1))
            map_[key] = value
            logger.debug(f"MapInitializer: '{key}' = '{value}'")
        logger.debug(f"MapInitializerList: {map_}")
        return map_

    def visitInt(self, ctx: CELParser.IntContext):
        value = int(ctx.NUM_INT().getText())
        logger.debug(f"Constant Literal Int: {value}")
        return value

    def visitUint(self, ctx: CELParser.UintContext):
        value = int(ctx.NUM_UINT().getText())
        logger.debug(f"Constant Literal Uint: {value}")
        return value

    def visitDouble(self, ctx: CELParser.DoubleContext):
        value = float(ctx.NUM_FLOAT().getText())
        logger.debug(f"Constant Literal Double: {value}")
        return value

    def visitString(self, ctx: CELParser.StringContext):
        value = ctx.STRING().getText()[1:-1]  # Remove quotes
        logger.debug(f"Constant Literal String: {value}")
        return value

    def visitBytes(self, ctx: CELParser.BytesContext):
        value = bytes.fromhex(ctx.BYTES().getText().strip('"'))
        logger.debug(f"Constant Literal Bytes: {value}")
        return value

    def visitBoolTrue(self, ctx: CELParser.BoolTrueContext):
        logger.debug("Constant Literal Bool: True")
        return True

    def visitBoolFalse(self, ctx: CELParser.BoolFalseContext):
        logger.debug("Constant Literal Bool: False")
        return False

    def visitNull(self, ctx: CELParser.NullContext):
        logger.debug("Constant Literal: Null")
        return None
