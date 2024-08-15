from antlr4 import *
from CELParser import CELParser
from CELVisitor import CELVisitor

class VisitorInterp(CELVisitor):
    def __init__(self, context):
        self.context = context
        self.function_registry = {
            "min": min,
            "max": max,
            "abs": abs,
            "ceil": lambda x: int(x) + (1 if x > int(x) else 0),
            "floor": lambda x: int(x),
            "round": round,
            "contains": lambda s, substr: substr in s,
            "endsWith": lambda s, suffix: s.endswith(suffix),
            "indexOf": lambda s, substr: s.find(substr),
            "length": len,
            "lower": str.lower,
            "upper": str.upper,
            "replace": lambda s, substr, replacement: s.replace(substr, replacement),
            "split": lambda s, separator: s.split(separator),
            "startsWith": lambda s, prefix: s.startswith(prefix),
            "matches": lambda s, regex: re.match(regex, s) is not None,
            "size": len,
            "all": all,
            "exists": any,
            "int": int,
            "uint": lambda x: max(0, int(x)),
            "double": float,
            "string": str,
            "bool": bool,
            "cond": lambda expr, true_val, false_val: true_val if expr else false_val,
            "existsOne": lambda lst, predicate: sum(1 for item in lst if predicate(item)) == 1,
            "timestamp": lambda: datetime.utcnow().isoformat() + "Z",
            "getDate": lambda timestamp: timestamp.getUTCDate(),
            "getDayOfMonth": lambda timestamp: timestamp.day,
            "getDayOfWeek": lambda timestamp: timestamp.weekday(),
            "getDayOfYear": lambda timestamp: timestamp.timetuple().tm_yday,
            "getFullYear": lambda timestamp: timestamp.year,
            "getHours": lambda timestamp: timestamp.hour,
            "getMilliseconds": lambda timestamp: timestamp.microsecond // 1000,
            "getMinutes": lambda timestamp: timestamp.minute,
            "getMonth": lambda timestamp: timestamp.month,
            "getSeconds": lambda timestamp: timestamp.second,
        }

    def visitStart(self, ctx:CELParser.StartContext):
        return self.visit(ctx.expr())

    def visitExpr(self, ctx:CELParser.ExprContext):
        if ctx.QUESTIONMARK():
            condition = self.visit(ctx.conditionalOr(0))
            true_branch = self.visit(ctx.conditionalOr(1))
            false_branch = self.visit(ctx.expr())
            return true_branch if condition else false_branch
        elif ctx.LPAREN():
            return self.visit(ctx.expr(0))
        else:
            return self.visit(ctx.conditionalOr(0))

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
        operator = ctx._op.text

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

    def visitCalcMulDiv(self, ctx:CELParser.CalcMulDivContext):
        left = self.visit(ctx.calc(0))
        right = self.visit(ctx.calc(1))
        operator = ctx._op.text

        if operator == "*":
            return left * right
        elif operator == "/":
            return left / right
        elif operator == "%":
            return left % right
        else:
            raise Exception(f"Unknown operator: {operator}")

    def visitCalcAddSub(self, ctx:CELParser.CalcAddSubContext):
        result = self.visit(ctx.calc(0))
        for i in range(1, len(ctx.calc())):
            right = self.visit(ctx.calc(i))
            operator = ctx._op[i - 1].text

            if operator == "+":
                result += right
            elif operator == "-":
                result -= right
            else:
                raise Exception(f"Unknown operator: {operator}")
        return result

    def visitLogicalNot(self, ctx:CELParser.LogicalNotContext):
        result = self.visit(ctx.member())
        for _ in ctx._ops:
            result = not result
        return result

    def visitNegate(self, ctx:CELParser.NegateContext):
        result = self.visit(ctx.member())
        for _ in ctx._ops:
            result = -result
        return result

    def visitMember(self, ctx:CELParser.MemberContext):
        if isinstance(ctx, CELParser.PrimaryContext):
            return self.visitPrimary(ctx)
        elif isinstance(ctx, CELParser.SelectOrCallContext):
            target = self.visit(ctx.member())
            member_name = ctx._id.text

            if ctx.LPAREN():
                args = self.visitExprList(ctx.exprList()) if ctx.exprList() else []
                if isinstance(target, dict) and member_name in target and callable(target[member_name]):
                    return target[member_name](*args)
                else:
                    raise Exception(f"'{member_name}' is not a function")
            else:
                return target.get(member_name)
        elif isinstance(ctx, CELParser.IndexContext):
            target = self.visit(ctx.member())
            index = self.visit(ctx.expr())
            return target[index]
        elif isinstance(ctx, CELParser.CreateMessageContext):
            obj = {}
            fields = ctx.fieldInitializerList().expr()
            for i in range(len(fields)):
                field = fields[i]
                key = ctx.fieldInitializerList().IDENTIFIER(i).text
                obj[key] = self.visit(field)
            return obj

    def visitPrimary(self, ctx:CELParser.PrimaryContext):
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

    def visitIdentOrGlobalCall(self, ctx:CELParser.IdentOrGlobalCallContext):
        identifier = ctx._id.text

        if ctx.LPAREN():
            args = self.visitExprList(ctx.exprList()) if ctx.exprList() else []
            func = self.function_registry.get(identifier)
            if callable(func):
                return func(*args)
            else:
                raise Exception(f"Function '{identifier}' is not defined")
        else:
            variable_value = self.context.get_variable(identifier)
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
        return sign * int(ctx.NUM_INT().text)

    def visitUint(self, ctx:CELParser.UintContext):
        return int(ctx.NUM_UINT().text)

    def visitDouble(self, ctx:CELParser.DoubleContext):
        sign = -1 if ctx.MINUS() else 1
        return sign * float(ctx.NUM_FLOAT().text)

    def visitString(self, ctx:CELParser.StringContext):
        return ctx.STRING().text.strip('"')

    def visitBytes(self, ctx:CELParser.BytesContext):
        return bytes.fromhex(ctx.BYTES().text.strip('"'))

    def visitBoolTrue(self, ctx:CELParser.BoolTrueContext):
        return True

    def visitBoolFalse(self, ctx:CELParser.BoolFalseContext):
        return False

    def visitNull(self, ctx:CELParser.NullContext):
        return None
