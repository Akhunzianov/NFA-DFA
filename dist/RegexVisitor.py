# Generated from Regex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RegexParser import RegexParser
else:
    from RegexParser import RegexParser

# This class defines a complete generic visitor for a parse tree produced by RegexParser.

class RegexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RegexParser#regex.
    def visitRegex(self, ctx:RegexParser.RegexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#Alternation.
    def visitAlternation(self, ctx:RegexParser.AlternationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#Concatenation.
    def visitConcatenation(self, ctx:RegexParser.ConcatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#Quantifiers.
    def visitQuantifiers(self, ctx:RegexParser.QuantifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#Group.
    def visitGroup(self, ctx:RegexParser.GroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#Character.
    def visitCharacter(self, ctx:RegexParser.CharacterContext):
        return self.visitChildren(ctx)



del RegexParser