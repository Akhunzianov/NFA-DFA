# Generated from Regex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RegexParser import RegexParser
else:
    from RegexParser import RegexParser

# This class defines a complete listener for a parse tree produced by RegexParser.
class RegexListener(ParseTreeListener):

    # Enter a parse tree produced by RegexParser#regex.
    def enterRegex(self, ctx:RegexParser.RegexContext):
        pass

    # Exit a parse tree produced by RegexParser#regex.
    def exitRegex(self, ctx:RegexParser.RegexContext):
        pass


    # Enter a parse tree produced by RegexParser#Alternation.
    def enterAlternation(self, ctx:RegexParser.AlternationContext):
        pass

    # Exit a parse tree produced by RegexParser#Alternation.
    def exitAlternation(self, ctx:RegexParser.AlternationContext):
        pass


    # Enter a parse tree produced by RegexParser#Concatenation.
    def enterConcatenation(self, ctx:RegexParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by RegexParser#Concatenation.
    def exitConcatenation(self, ctx:RegexParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by RegexParser#Quantifiers.
    def enterQuantifiers(self, ctx:RegexParser.QuantifiersContext):
        pass

    # Exit a parse tree produced by RegexParser#Quantifiers.
    def exitQuantifiers(self, ctx:RegexParser.QuantifiersContext):
        pass


    # Enter a parse tree produced by RegexParser#Group.
    def enterGroup(self, ctx:RegexParser.GroupContext):
        pass

    # Exit a parse tree produced by RegexParser#Group.
    def exitGroup(self, ctx:RegexParser.GroupContext):
        pass


    # Enter a parse tree produced by RegexParser#Character.
    def enterCharacter(self, ctx:RegexParser.CharacterContext):
        pass

    # Exit a parse tree produced by RegexParser#Character.
    def exitCharacter(self, ctx:RegexParser.CharacterContext):
        pass



del RegexParser