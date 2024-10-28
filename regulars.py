from dataclasses import dataclass


@dataclass
class RegCommand:
    def __init__(self, type: str, first_arg = None, second_arg = None) -> None:
        self.type = type
        self.n = first_arg
        self.m = second_arg


class RegularExpression:
    def __init__(self, expression: str) -> None:
        words = expression.split('|')
        add_on = 0
        commands = []
        for word in words:
            add_on += 1
            if add_on != 1:
                add_on += 1
            if (add_on + 1) == 2 * len(words):
                add_on -= 1
            if 1 == len(words):
                add_on = 0
            curr_commands = []
            for symb in word:
                if symb == 'a' or symb == 'b':
                    curr_commands.append(RegCommand('char', symb))
                elif symb == '?':
                    temp = curr_commands.pop()
                    curr_commands.append(RegCommand('split', len(curr_commands) + 1 + add_on, len(curr_commands) + 2 + add_on))
                    curr_commands.append(temp)
                elif symb == '*':
                    temp = curr_commands.pop()
                    curr_commands.append(RegCommand('split', len(curr_commands) + 1 + add_on, len(curr_commands) + 3 + add_on))
                    curr_commands.append(temp)
                    curr_commands.append(RegCommand('jmp', len(curr_commands) - 2 + add_on))
                elif symb == '+':
                    curr_commands.append(RegCommand('split', len(curr_commands) - 1 + add_on, len(curr_commands) + 1 + add_on))
            commands.append(curr_commands)

        res_commands = []
        last_cmd_numb = 0
        for el in commands:
            last_cmd_numb += len(el)
        if len(commands) > 1:
            last_cmd_numb += 2 * (len(commands) - 1)
        for i in range(0, len(commands) - 1):
            res_commands.append(RegCommand('split', len(res_commands) + 1, len(res_commands) + 1 + len(commands[i]) + 1))
            res_commands += commands[i]
            res_commands.append(RegCommand('jmp', last_cmd_numb))
        res_commands += commands[-1]
        res_commands.append(RegCommand('match'))

        self.cmds = res_commands

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
