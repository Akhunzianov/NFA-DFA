from dist.RegexParser import RegexParser
from dist.RegexVisitor import RegexVisitor
from dataclasses import dataclass


@dataclass
class RegCommand:
    def __init__(self, type: str, n = None, m = None) -> None:
        self.type = type
        self.n = n
        self.m = m


class InstructionGenerator(RegexVisitor):
    def __init__(self):
        self.commands = []
        self.minu = 0

    def visitRegex(self, ctx: RegexParser.RegexContext):
        self.visit(ctx.expression())
        self.commands.append(RegCommand('match'))
        return self.commands

    def visitAlternation(self, ctx: RegexParser.AlternationContext):
        self.minu -= 1
        if len(ctx.term()) > 1:
            for term in ctx.term():
                st_len = len(self.commands)
                if term != ctx.term()[-1]:
                    self.commands.append(RegCommand('split', st_len + 1, None))
                self.visit(term)
                if term != ctx.term()[-1]:
                    self.commands.append(RegCommand('jmp', self.minu))
                    self.commands[st_len].m = len(self.commands)
        else:
            self.visit(ctx.term(0))
        for i in range(len(self.commands)):
            if self.commands[i].n == self.minu :
                self.commands[i].n = len(self.commands)

        self.minu += 1

    def visitConcatenation(self, ctx: RegexParser.ConcatenationContext):
        for factor in ctx.factor():
            self.visit(factor)

    def visitQuantifiers(self, ctx: RegexParser.QuantifiersContext):
        quantifiers = list(ctx.getChildren())
        st_len = len(self.commands)
        prev = -1
        for q in reversed(quantifiers):
            if q.getText() == '*':
                self.commands.append(RegCommand('split', st_len + 1, None))
                self.visit(ctx.base())
                self.commands.append(RegCommand('jmp', st_len))
                self.commands[st_len].m = len(self.commands)
                prev = 1
            elif q.getText() == '+':
                self.visit(ctx.base())
                self.commands.append(RegCommand('split', st_len, len(self.commands) + 1))
                prev = 1
            elif q.getText() == '?':
                self.commands.append(RegCommand('split', st_len + 1, None))
                self.visit(ctx.base())
                self.commands[st_len].m = len(self.commands)
                prev = 1
            elif prev != 1:
                self.visit(ctx.base())



    def visitGroup(self, ctx: RegexParser.GroupContext):
        self.visit(ctx.expression())

    def visitCharacter(self, ctx: RegexParser.CharacterContext):
        self.commands.append(RegCommand('char', ctx.CHAR().getText()))