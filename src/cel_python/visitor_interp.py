from antlr4 import *
from .parser.CELParser import CELParser
from .parser.CELVisitor import CELVisitor
from datetime import datetime
from datetime import timezone


class VisitorInterp(CELVisitor):
    def __init__(self, context):
        self.context = context
        self.function_registry = {
            # Arithmetic Functions
            "min": min,
            "max": max,
            "abs": abs,
            "ceil": lambda x: int(x) + (1 if x > int(x) else 0),
            "floor": lambda x: int(x),
            "round": round,

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
            "size": len,

            # Type Conversion Functions
            "int": int,
            "uint": lambda x: max(0, int(x)),
            "double": float,
            "string": str,
            "bool": bool,

            # Null Handling Functions
            "exists": lambda x: x is not None,
            "existsOne": lambda lst: sum(1 for item in lst if item is not None) == 1,

            # Date/Time Functions
            "duration": lambda seconds: f"{seconds}s",
            "timestamp": lambda: datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ')[:-4] + '000Z',
            "time": lambda year, month, day, hour, minute, second, millisecond: datetime(year, month, day, hour, minute, second, millisecond * 1000, tzinfo=timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ')[:-4] + '000Z',

            "date": lambda year, month, day: datetime(year, month, day).strftime("%Y-%m-%d"),
            "getFullYear": lambda timestamp: timestamp.year,
            "getMonth": lambda timestamp: timestamp.month - 1,  # 0-indexed
            "getDate": lambda timestamp: timestamp.day,
            "getHours": lambda timestamp: timestamp.hour,
            "getMinutes": lambda timestamp: timestamp.minute,
            "getSeconds": lambda timestamp: timestamp.second,
        }

    def visitStart(self, ctx:CELParser.StartContext):
        return self.visit(ctx.expr())

    def visitExpr(self, ctx: CELParser.ExprContext):
        if ctx.e1 is not None:
            condition = self.visit(ctx.e)
            true_case = self.visit(ctx.e1)
            false_case = self.visit(ctx.e2)
            return true_case if condition else false_case
        else:
            return self.visit(ctx.e)

    def visitConditionalOr(self, ctx:CELParser.ConditionalOrContext):
        result = self.visit(ctx.conditionalAnd(0))
        for i in range(1, len(ctx.conditionalAnd())):
            result = result or self.visit(ctx.conditionalAnd(i))
        return result

    def visitConditionalAnd(self, ctx:CELParser.ConditionalAndContext):
        result = self.visit(ctx.relation(0))
        for i in range(1, len(ctx.relation())):
            result = result and self.visit(ctx.relation(i))
        return result

    def visitRelationOp(self, ctx:CELParser.RelationOpContext):
        left = self.visit(ctx.relation(0))
        right = self.visit(ctx.relation(1))
        operator = ctx.op.text

        if operator in ["==", "!=", "<", "<=", ">", ">="]:
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
            return self.visit(ctx.calc())

    def visitRelationCalc(self, ctx: CELParser.RelationCalcContext):
        left = self.visit(ctx.getChild(0)) 

        for i in range(1, ctx.getChildCount(), 2):
            operator = ctx.getChild(i).getText() 
            right = self.visit(ctx.getChild(i + 1)) 

            if operator == "+":
                left += right
            elif operator == "-":
                left -= right
            elif operator == "*":
                left *= right
            elif operator == "/":
                left /= right
            elif operator == "%":
                left %= right
            else:
                raise Exception(f"Unknown operator: {operator}")
            
        return left

    def visitCalcMulDiv(self, ctx: CELParser.CalcMulDivContext):
        ty = ctx.getChild(0).__class__.__name__
        left = self.visit(ctx.getChild(0))

        right = self.visit(ctx.getChild(2))

        operator = ctx.getChild(1).getText()

        if operator == "*":
            result = left * right
        elif operator == "/":
            result = left / right
        elif operator == "%":
            result = left % right
        else:
            raise Exception(f"Unknown operator: {operator}")

        return result


    def visitCalcAddSub(self, ctx: CELParser.CalcAddSubContext):
        result = self.visit(ctx.getChild(0)) 
        for i in range(1, ctx.getChildCount(), 2):
            operator = ctx.getChild(i).getText() 
            right = self.visit(ctx.getChild(i + 1)) 

            if operator == "+":
                result += right
            elif operator == "-":
                result -= right
            else:
                raise Exception(f"Unknown operator: {operator}")
        return result


    def visitLogicalNot(self, ctx: CELParser.LogicalNotContext):
        result = self.visit(ctx.member())
        for _ in ctx.ops:
            result = not result
        return result

    def visitNegate(self, ctx:CELParser.NegateContext):
        result = self.visit(ctx.member())
        for _ in ctx._ops:
            result = -result
        return result

    def visitMember(self, ctx: CELParser.MemberContext):
        if ctx.primary():
            type = ctx.primary().__class__.__name__
            res =  self.visit(ctx.primary())
            return res

        elif ctx.DOT() and ctx.IDENTIFIER():
            target = self.visit(ctx.member())
            Member_name = ctx.IDENTIFIER().getText()            
            if ctx.LPAREN() and ctx.RPAREN():
                args = self.visit(ctx.exprList()) if ctx.exprList() else []
                if callable(getattr(target, member_name, None)):
                    return getattr(target, member_name)(*args)
                else:
                    raise Exception(f"'{member_name}' is not a function")
            else:
                if isinstance(target, dict):
                    return target.get(member_name)
                elif hasattr(target, member_name):
                    return getattr(target, member_name)
                else:
                    raise Exception(f"Member '{member_name}' not found")

        elif ctx.LBRACKET() and ctx.RPRACKET():
            print("QQ visiting braket" )
            target = self.visit(ctx.member())
            index = self.visit(ctx.expr())
            return target[index]

        elif ctx.LBRACE() and ctx.RBRACE():
            print("QQ visiting -ddfdsfsdfsdf from member" )
            message = {}
            if ctx.fieldInitializerList():
                fields = ctx.fieldInitializerList().fields
                values = ctx.fieldInitializerList().values
                for field, value in zip(fields, values):
                    field_name = field.getText()
                    field_value = self.visit(value)
                    message[field_name] = field_value
            return message

        else:
            raise Exception("Unexpected member structure")

    def visitMemberExpr(self, ctx: CELParser.MemberExprContext):
       result = self.visit(ctx.member())

       return result

    def visitPrimaryExpr(self, ctx: CELParser.PrimaryExprContext):
        result = self.visitPrimary(ctx.primary())

        return result


    def visitConstantLiteral(self, ctx:CELParser.ConstantLiteralContext):
        return self.visit(ctx.literal())

    def visitPrimary(self, ctx: CELParser.PrimaryContext):
        if isinstance(ctx, CELParser.IdentOrGlobalCallContext):
            return self.visitIdentOrGlobalCall(ctx)
        elif isinstance(ctx, CELParser.NestedContext):
            return self.visit(ctx.expr())
        elif isinstance(ctx, CELParser.CreateListContext):
            return self.visitExprList(ctx.exprList()) if ctx.exprList() else []
        elif isinstance(ctx, CELParser.CreateStructContext):
            obj = {}
            if ctx.mapInitializerList():
                entries = ctx.mapInitializerList().expr()
                for i in range(0, len(entries), 2):
                    key = self.visit(entries[i])
                    value = self.visit(entries[i + 1])
                    obj[key] = value
            return obj
        elif isinstance(ctx, CELParser.ConstantLiteralContext):
            return self.visit(ctx.literal())
        else:
            return None

    def visitCalcUnary(self, ctx: CELParser.CalcUnaryContext):
        child = ctx.getChild(0)
        return self.visit(child)


    def visitIdentOrGlobalCall(self, ctx:CELParser.IdentOrGlobalCallContext):
        identifier = ctx.IDENTIFIER().getText()

        if ctx.LPAREN():
            args = self.visitExprList(ctx.exprList()) if ctx.exprList() else []
            func = self.function_registry.get(identifier)
            if callable(func):
                return func(*args)
            else:
                raise Exception(f"Function '{identifier}' is not defined")
        else:
            variable_value = self.context.get(identifier)
            if variable_value is None:
                raise Exception(f"Variable '{identifier}' is not defined")
            return variable_value

    def visitExprList(self, ctx:CELParser.ExprListContext):
        return [self.visit(expr) for expr in ctx.expr()]

    def visitFieldInitializerList(self, ctx:CELParser.FieldInitializerListContext):
        fields = {}
        for i in range(len(ctx.IDENTIFIER())):
            field = ctx.IDENTIFIER(i).text
            value = self.visit(ctx.expr(i))
            fields[field] = value
        return fields

    def visitMapInitializerList(self, ctx:CELParser.MapInitializerListContext):
        map_ = {}
        for i in range(0, len(ctx.expr()), 2):
            key = self.visit(ctx.expr(i))
            value = self.visit(ctx.expr(i + 1))
            map_[key] = value
        return map_

    def visitInt(self, ctx:CELParser.IntContext):
        sign = -1 if ctx.MINUS() else 1
        return sign * int(ctx.NUM_INT().getText())

    def visitUint(self, ctx:CELParser.UintContext):
        return int(ctx.NUM_UINT().text)

    def visitDouble(self, ctx:CELParser.DoubleContext):
        sign = -1 if ctx.MINUS() else 1
        return sign * float(ctx.NUM_FLOAT().text)

    def visitString(self, ctx:CELParser.StringContext):
        return ctx.STRING().getText()[1:-1]

    def visitBytes(self, ctx:CELParser.BytesContext):
        return bytes.fromhex(ctx.BYTES().getText().strip('"'))

    def visitBoolTrue(self, ctx:CELParser.BoolTrueContext):
        return True

    def visitBoolFalse(self, ctx:CELParser.BoolFalseContext):
        return False

    def visitNull(self, ctx:CELParser.NullContext):
        return None

    def visit(self, tree):
        return super().visit(tree)
