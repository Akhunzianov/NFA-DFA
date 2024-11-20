from regulars import RegularExpression, RegCommand

from itertools import product
import re

sequences = []
for i in range(11):
    sequences.extend([''.join(p) for p in product('ab', repeat=i)])

def test():
    cmd = RegularExpression('a')
    true_cmd = [RegCommand('char', 'a'), RegCommand('match')]
    reg = r'a'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not cmd.check(w):
                return False
        else:
            if cmd.check(w):
                return False
    for k in range(len(true_cmd)):
        if cmd.cmds[k].m != true_cmd[k].m or cmd.cmds[k].n != true_cmd[k].n or cmd.cmds[k].type != true_cmd[k].type:
            return False

    cmd = RegularExpression('b')
    true_cmd = [RegCommand('char', 'b'), RegCommand('match')]
    reg = r'b'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not cmd.check(w):
                return False
        else:
            if cmd.check(w):
                return False
    for k in range(len(true_cmd)):
        if cmd.cmds[k].m != true_cmd[k].m or cmd.cmds[k].n != true_cmd[k].n or cmd.cmds[k].type != true_cmd[k].type:
            return False

    cmd = RegularExpression('aa')
    true_cmd = [RegCommand('char', 'a'),
                RegCommand('char', 'a'),
                RegCommand('match')]
    reg = r'aa'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not cmd.check(w):
                return False
        else:
            if cmd.check(w):
                return False
    for k in range(len(true_cmd)):
        if cmd.cmds[k].m != true_cmd[k].m or cmd.cmds[k].n != true_cmd[k].n or cmd.cmds[k].type != true_cmd[k].type:
            return False

    cmd = RegularExpression('bb')
    true_cmd = [RegCommand('char', 'b'),
                RegCommand('char', 'b'),
                RegCommand('match')]
    reg = r'bb'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not cmd.check(w):
                return False
        else:
            if cmd.check(w):
                return False
    for k in range(len(true_cmd)):
        if cmd.cmds[k].m != true_cmd[k].m or cmd.cmds[k].n != true_cmd[k].n or cmd.cmds[k].type != true_cmd[k].type:
            return False

    cmd = RegularExpression('ab')
    true_cmd = [RegCommand('char', 'a'),
                RegCommand('char', 'b'),
                RegCommand('match')]
    reg = r'ab'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not cmd.check(w):
                return False
        else:
            if cmd.check(w):
                return False
    for k in range(len(true_cmd)):
        if cmd.cmds[k].m != true_cmd[k].m or cmd.cmds[k].n != true_cmd[k].n or cmd.cmds[k].type != true_cmd[k].type:
            return False

    cmd = RegularExpression('a|b')
    true_cmd = [RegCommand('split', 1, 3),
                RegCommand('char', 'a'),
                RegCommand('jmp', 4),
                RegCommand('char', 'b'),
                RegCommand('match')]
    reg = r'a|b'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not cmd.check(w):
                return False
        else:
            if cmd.check(w):
                return False
    for k in range(len(true_cmd)):
        if cmd.cmds[k].m != true_cmd[k].m or cmd.cmds[k].n != true_cmd[k].n or cmd.cmds[k].type != true_cmd[k].type:
            return False

    cmd = RegularExpression('a+b+')
    true_cmd = [
        RegCommand('char', 'a'),
        RegCommand('split', 0, 2),
        RegCommand('char', 'b'),
        RegCommand('split', 2, 4),
        RegCommand('match')
    ]
    reg = r'a+b+'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not cmd.check(w):
                return False
        else:
            if cmd.check(w):
                return False
    for k in range(len(true_cmd)):
        if cmd.cmds[k].m != true_cmd[k].m or cmd.cmds[k].n != true_cmd[k].n or cmd.cmds[k].type != true_cmd[k].type:
            return False

    cmd = RegularExpression('a*')
    true_cmd = [
        RegCommand('split', 1, 3),
        RegCommand('char', 'a'),
        RegCommand('jmp', 0),
        RegCommand('match')
    ]
    reg = r'a*'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not cmd.check(w):
                return False
        else:
            if cmd.check(w):
                return False
    for k in range(len(true_cmd)):
        if cmd.cmds[k].m != true_cmd[k].m or cmd.cmds[k].n != true_cmd[k].n or cmd.cmds[k].type != true_cmd[k].type:
            return False

    cmd = RegularExpression('b+')
    true_cmd = [
        RegCommand('char', 'b'),
        RegCommand('split', 0, 2),
        RegCommand('match')
    ]
    reg = r'b+'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not cmd.check(w):
                return False
        else:
            if cmd.check(w):
                return False
    for k in range(len(true_cmd)):
        if cmd.cmds[k].m != true_cmd[k].m or cmd.cmds[k].n != true_cmd[k].n or cmd.cmds[k].type != true_cmd[k].type:
            return False

    cmd = RegularExpression('ab*')
    true_cmd = [
        RegCommand('char', 'a'),
        RegCommand('split', 2, 4),
        RegCommand('char', 'b'),
        RegCommand('jmp', 1),
        RegCommand('match')
    ]
    reg = r'ab*'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not cmd.check(w):
                return False
        else:
            if cmd.check(w):
                return False
    for k in range(len(true_cmd)):
        if cmd.cmds[k].m != true_cmd[k].m or cmd.cmds[k].n != true_cmd[k].n or cmd.cmds[k].type != true_cmd[k].type:
            return False

    cmd = RegularExpression('a?b')
    true_cmd = [
        RegCommand('split', 1, 2),
        RegCommand('char', 'a'),
        RegCommand('char', 'b'),
        RegCommand('match')
    ]
    reg = r'a?b'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not cmd.check(w):
                return False
        else:
            if cmd.check(w):
                return False
    for k in range(len(true_cmd)):
        if cmd.cmds[k].m != true_cmd[k].m or cmd.cmds[k].n != true_cmd[k].n or cmd.cmds[k].type != true_cmd[k].type:
            return False

    cmd = RegularExpression('a|b*')
    true_cmd = [
        RegCommand('split', 1, 3),
        RegCommand('char', 'a'),
        RegCommand('jmp', 6),
        RegCommand('split', 4, 6),
        RegCommand('char', 'b'),
        RegCommand('jmp', 3),
        RegCommand('match')
    ]
    reg = r'a|b*'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not cmd.check(w):
                return False
        else:
            if cmd.check(w):
                return False
    for k in range(len(true_cmd)):
        if cmd.cmds[k].m != true_cmd[k].m or cmd.cmds[k].n != true_cmd[k].n or cmd.cmds[k].type != true_cmd[k].type:
            return False

    cmd = RegularExpression('a|b|ba')
    true_cmd = [
        RegCommand('split', 1, 3),
        RegCommand('char', 'a'),
        RegCommand('jmp', 8),
        RegCommand('split', 4, 6),
        RegCommand('char', 'b'),
        RegCommand('jmp', 8),
        RegCommand('char', 'b'),
        RegCommand('char', 'a'),
        RegCommand('match')
    ]
    reg = r'a|b|ba'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not cmd.check(w):
                return False
        else:
            if cmd.check(w):
                return False
    for k in range(len(true_cmd)):
        if cmd.cmds[k].m != true_cmd[k].m or cmd.cmds[k].n != true_cmd[k].n or cmd.cmds[k].type != true_cmd[k].type:
            return False

    cmd = RegularExpression('a+|b?a|a+b')
    true_cmd = [
        RegCommand('split', 1, 4),
        RegCommand('char', 'a'),
        RegCommand('split', 1, 3),
        RegCommand('jmp', 12),
        RegCommand('split', 5, 9),
        RegCommand('split', 6, 7),
        RegCommand('char', 'b'),
        RegCommand('char', 'a'),
        RegCommand('jmp', 12),
        RegCommand('char', 'a'),
        RegCommand('split', 9, 11),
        RegCommand('char', 'b'),
        RegCommand('match')
    ]
    reg = r'a+|b?a|a+b'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not cmd.check(w):
                return False
        else:
            if cmd.check(w):
                return False
    for k in range(len(true_cmd)):
        if cmd.cmds[k].m != true_cmd[k].m or cmd.cmds[k].n != true_cmd[k].n or cmd.cmds[k].type != true_cmd[k].type:
            return False


    return True