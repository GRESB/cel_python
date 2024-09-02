# Generated from grammar/CEL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .CELParser import CELParser
else:
    from CELParser import CELParser

# This class defines a complete listener for a parse tree produced by CELParser.
class CELListener(ParseTreeListener):

    # Enter a parse tree produced by CELParser#start.
    def enterStart(self, ctx:CELParser.StartContext):
        pass

    # Exit a parse tree produced by CELParser#start.
    def exitStart(self, ctx:CELParser.StartContext):
        pass


    # Enter a parse tree produced by CELParser#expr.
    def enterExpr(self, ctx:CELParser.ExprContext):
        pass

    # Exit a parse tree produced by CELParser#expr.
    def exitExpr(self, ctx:CELParser.ExprContext):
        pass


    # Enter a parse tree produced by CELParser#conditionalOr.
    def enterConditionalOr(self, ctx:CELParser.ConditionalOrContext):
        pass

    # Exit a parse tree produced by CELParser#conditionalOr.
    def exitConditionalOr(self, ctx:CELParser.ConditionalOrContext):
        pass


    # Enter a parse tree produced by CELParser#conditionalAnd.
    def enterConditionalAnd(self, ctx:CELParser.ConditionalAndContext):
        pass

    # Exit a parse tree produced by CELParser#conditionalAnd.
    def exitConditionalAnd(self, ctx:CELParser.ConditionalAndContext):
        pass


    # Enter a parse tree produced by CELParser#RelationOp.
    def enterRelationOp(self, ctx:CELParser.RelationOpContext):
        pass

    # Exit a parse tree produced by CELParser#RelationOp.
    def exitRelationOp(self, ctx:CELParser.RelationOpContext):
        pass


    # Enter a parse tree produced by CELParser#RelationCalc.
    def enterRelationCalc(self, ctx:CELParser.RelationCalcContext):
        pass

    # Exit a parse tree produced by CELParser#RelationCalc.
    def exitRelationCalc(self, ctx:CELParser.RelationCalcContext):
        pass


    # Enter a parse tree produced by CELParser#CalcMulDiv.
    def enterCalcMulDiv(self, ctx:CELParser.CalcMulDivContext):
        pass

    # Exit a parse tree produced by CELParser#CalcMulDiv.
    def exitCalcMulDiv(self, ctx:CELParser.CalcMulDivContext):
        pass


    # Enter a parse tree produced by CELParser#CalcUnary.
    def enterCalcUnary(self, ctx:CELParser.CalcUnaryContext):
        pass

    # Exit a parse tree produced by CELParser#CalcUnary.
    def exitCalcUnary(self, ctx:CELParser.CalcUnaryContext):
        pass


    # Enter a parse tree produced by CELParser#CalcAddSub.
    def enterCalcAddSub(self, ctx:CELParser.CalcAddSubContext):
        pass

    # Exit a parse tree produced by CELParser#CalcAddSub.
    def exitCalcAddSub(self, ctx:CELParser.CalcAddSubContext):
        pass


    # Enter a parse tree produced by CELParser#MemberExpr.
    def enterMemberExpr(self, ctx:CELParser.MemberExprContext):
        pass

    # Exit a parse tree produced by CELParser#MemberExpr.
    def exitMemberExpr(self, ctx:CELParser.MemberExprContext):
        pass


    # Enter a parse tree produced by CELParser#LogicalNot.
    def enterLogicalNot(self, ctx:CELParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by CELParser#LogicalNot.
    def exitLogicalNot(self, ctx:CELParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by CELParser#Negate.
    def enterNegate(self, ctx:CELParser.NegateContext):
        pass

    # Exit a parse tree produced by CELParser#Negate.
    def exitNegate(self, ctx:CELParser.NegateContext):
        pass


    # Enter a parse tree produced by CELParser#SelectOrCall.
    def enterSelectOrCall(self, ctx:CELParser.SelectOrCallContext):
        pass

    # Exit a parse tree produced by CELParser#SelectOrCall.
    def exitSelectOrCall(self, ctx:CELParser.SelectOrCallContext):
        pass


    # Enter a parse tree produced by CELParser#PrimaryExpr.
    def enterPrimaryExpr(self, ctx:CELParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by CELParser#PrimaryExpr.
    def exitPrimaryExpr(self, ctx:CELParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by CELParser#Index.
    def enterIndex(self, ctx:CELParser.IndexContext):
        pass

    # Exit a parse tree produced by CELParser#Index.
    def exitIndex(self, ctx:CELParser.IndexContext):
        pass


    # Enter a parse tree produced by CELParser#CreateMessage.
    def enterCreateMessage(self, ctx:CELParser.CreateMessageContext):
        pass

    # Exit a parse tree produced by CELParser#CreateMessage.
    def exitCreateMessage(self, ctx:CELParser.CreateMessageContext):
        pass


    # Enter a parse tree produced by CELParser#IdentOrGlobalCall.
    def enterIdentOrGlobalCall(self, ctx:CELParser.IdentOrGlobalCallContext):
        pass

    # Exit a parse tree produced by CELParser#IdentOrGlobalCall.
    def exitIdentOrGlobalCall(self, ctx:CELParser.IdentOrGlobalCallContext):
        pass


    # Enter a parse tree produced by CELParser#Nested.
    def enterNested(self, ctx:CELParser.NestedContext):
        pass

    # Exit a parse tree produced by CELParser#Nested.
    def exitNested(self, ctx:CELParser.NestedContext):
        pass


    # Enter a parse tree produced by CELParser#CreateList.
    def enterCreateList(self, ctx:CELParser.CreateListContext):
        pass

    # Exit a parse tree produced by CELParser#CreateList.
    def exitCreateList(self, ctx:CELParser.CreateListContext):
        pass


    # Enter a parse tree produced by CELParser#CreateStruct.
    def enterCreateStruct(self, ctx:CELParser.CreateStructContext):
        pass

    # Exit a parse tree produced by CELParser#CreateStruct.
    def exitCreateStruct(self, ctx:CELParser.CreateStructContext):
        pass


    # Enter a parse tree produced by CELParser#ConstantLiteral.
    def enterConstantLiteral(self, ctx:CELParser.ConstantLiteralContext):
        pass

    # Exit a parse tree produced by CELParser#ConstantLiteral.
    def exitConstantLiteral(self, ctx:CELParser.ConstantLiteralContext):
        pass


    # Enter a parse tree produced by CELParser#exprList.
    def enterExprList(self, ctx:CELParser.ExprListContext):
        pass

    # Exit a parse tree produced by CELParser#exprList.
    def exitExprList(self, ctx:CELParser.ExprListContext):
        pass


    # Enter a parse tree produced by CELParser#fieldInitializerList.
    def enterFieldInitializerList(self, ctx:CELParser.FieldInitializerListContext):
        pass

    # Exit a parse tree produced by CELParser#fieldInitializerList.
    def exitFieldInitializerList(self, ctx:CELParser.FieldInitializerListContext):
        pass


    # Enter a parse tree produced by CELParser#mapInitializerList.
    def enterMapInitializerList(self, ctx:CELParser.MapInitializerListContext):
        pass

    # Exit a parse tree produced by CELParser#mapInitializerList.
    def exitMapInitializerList(self, ctx:CELParser.MapInitializerListContext):
        pass


    # Enter a parse tree produced by CELParser#Int.
    def enterInt(self, ctx:CELParser.IntContext):
        pass

    # Exit a parse tree produced by CELParser#Int.
    def exitInt(self, ctx:CELParser.IntContext):
        pass


    # Enter a parse tree produced by CELParser#Uint.
    def enterUint(self, ctx:CELParser.UintContext):
        pass

    # Exit a parse tree produced by CELParser#Uint.
    def exitUint(self, ctx:CELParser.UintContext):
        pass


    # Enter a parse tree produced by CELParser#Double.
    def enterDouble(self, ctx:CELParser.DoubleContext):
        pass

    # Exit a parse tree produced by CELParser#Double.
    def exitDouble(self, ctx:CELParser.DoubleContext):
        pass


    # Enter a parse tree produced by CELParser#String.
    def enterString(self, ctx:CELParser.StringContext):
        pass

    # Exit a parse tree produced by CELParser#String.
    def exitString(self, ctx:CELParser.StringContext):
        pass


    # Enter a parse tree produced by CELParser#Bytes.
    def enterBytes(self, ctx:CELParser.BytesContext):
        pass

    # Exit a parse tree produced by CELParser#Bytes.
    def exitBytes(self, ctx:CELParser.BytesContext):
        pass


    # Enter a parse tree produced by CELParser#BoolTrue.
    def enterBoolTrue(self, ctx:CELParser.BoolTrueContext):
        pass

    # Exit a parse tree produced by CELParser#BoolTrue.
    def exitBoolTrue(self, ctx:CELParser.BoolTrueContext):
        pass


    # Enter a parse tree produced by CELParser#BoolFalse.
    def enterBoolFalse(self, ctx:CELParser.BoolFalseContext):
        pass

    # Exit a parse tree produced by CELParser#BoolFalse.
    def exitBoolFalse(self, ctx:CELParser.BoolFalseContext):
        pass


    # Enter a parse tree produced by CELParser#Null.
    def enterNull(self, ctx:CELParser.NullContext):
        pass

    # Exit a parse tree produced by CELParser#Null.
    def exitNull(self, ctx:CELParser.NullContext):
        pass



del CELParser