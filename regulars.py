from antlr4 import InputStream, CommonTokenStream
from dist.RegexLexer import RegexLexer
from dist.RegexParser import RegexParser
from antlr_regulars import InstructionGenerator
from dist.RegexErrorListener import RegexErrorListener

from dataclasses import dataclass


@dataclass
class RegCommand:
    def __init__(self, type: str, first_arg = None, second_arg = None) -> None:
        self.type = type
        self.n = first_arg
        self.m = second_arg


class RegularExpression:
    def __init__(self, expression: str) -> None:
        input_stream = InputStream(expression)
        lexer = RegexLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = RegexParser(token_stream)

        error_listener = RegexErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        tree = parser.regex()
        if error_listener.errors:
            raise Exception("Invalid regular expression")

        visitor = InstructionGenerator()
        self.cmds = visitor.visit(tree)

    def check(self, input: str) -> bool:
        positions = [(0, 0)]
        while len(positions) != 0:
            cmd_ind, inp_ind = positions.pop()
            cmd = self.cmds[cmd_ind]
            if cmd.type == 'char':
                if inp_ind < len(input) and input[inp_ind] == cmd.n:
                    positions.append((cmd_ind + 1, inp_ind + 1))
            elif cmd.type == 'match' and inp_ind == len(input):
                return True
            elif cmd.type == 'jmp':
                positions.append((cmd.n, inp_ind))
            elif cmd.type == 'split':
                positions.append((cmd.n, inp_ind))
                positions.append((cmd.m, inp_ind))
        return False
