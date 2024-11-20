from regulars import RegularExpression, RegCommand

from itertools import product
import re

sequences = []
for i in range(11):
    sequences.extend([''.join(p) for p in product('ab', repeat=i)])


def test_regex_matching():
    regex = "a"
    vm = RegularExpression(regex)
    true_cmd = [RegCommand('char', 'a'), RegCommand('match')]
    reg = r'a'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "b"
    vm = RegularExpression(regex)
    true_cmd = [RegCommand('char', 'b'), RegCommand('match')]
    reg = r'b'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "aa"
    vm = RegularExpression(regex)
    true_cmd = [RegCommand('char', 'a'),
                RegCommand('char', 'a'),
                RegCommand('match')]
    reg = r'aa'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "bb"
    vm = RegularExpression(regex)
    true_cmd = [RegCommand('char', 'b'),
                RegCommand('char', 'b'),
                RegCommand('match')]
    reg = r'bb'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "ab"
    vm = RegularExpression(regex)
    true_cmd = [RegCommand('char', 'a'),
                RegCommand('char', 'b'),
                RegCommand('match')]
    reg = r'ab'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "a|b"
    vm = RegularExpression(regex)
    true_cmd = [RegCommand('split', 1, 3),
                RegCommand('char', 'a'),
                RegCommand('jmp', 4),
                RegCommand('char', 'b'),
                RegCommand('match')]
    reg = r'a|b'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "a+b+"
    vm = RegularExpression(regex)
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
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "a*"
    vm = RegularExpression(regex)
    true_cmd = [
        RegCommand('split', 1, 3),
        RegCommand('char', 'a'),
        RegCommand('jmp', 0),
        RegCommand('match')
    ]
    reg = r'a*'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "b+"
    vm = RegularExpression(regex)
    true_cmd = [
        RegCommand('char', 'b'),
        RegCommand('split', 0, 2),
        RegCommand('match')
    ]
    reg = r'b+'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "ab*"
    vm = RegularExpression(regex)
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
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "a?b"
    vm = RegularExpression(regex)
    true_cmd = [
        RegCommand('split', 1, 2),
        RegCommand('char', 'a'),
        RegCommand('char', 'b'),
        RegCommand('match')
    ]
    reg = r'a?b'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "a|b*"
    vm = RegularExpression(regex)
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
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "a|b|ba"
    vm = RegularExpression(regex)
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
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "a+|b?a|a+b"
    vm = RegularExpression(regex)
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
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "(a)"
    vm = RegularExpression(regex)
    true_cmd = [
        RegCommand('char', 'a'),
        RegCommand('match')
    ]
    reg = r'(a)'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if k >= len(vm.cmds):
            return False
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "(a|b)"
    vm = RegularExpression(regex)
    true_cmd = [
        RegCommand('split', 1, 3),
        RegCommand('char', 'a'),
        RegCommand('jmp', 4),
        RegCommand('char', 'b'),
        RegCommand('match')
    ]
    reg = r'(a|b)'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if k >= len(vm.cmds):
            return False
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "(ab)*"
    vm = RegularExpression(regex)
    true_cmd = [
        RegCommand('split', 1, 4),
        RegCommand('char', 'a'),
        RegCommand('char', 'b'),
        RegCommand('jmp', 0),
        RegCommand('match')
    ]
    reg = r'(ab)*'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if k >= len(vm.cmds):
            return False
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "a(bc)*"
    vm = RegularExpression(regex)
    true_cmd = [
        RegCommand('char', 'a'),
        RegCommand('split', 2, 5),
        RegCommand('char', 'b'),
        RegCommand('char', 'c'),
        RegCommand('jmp', 1),
        RegCommand('match')
    ]
    reg = r'a(bc)*'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if k >= len(vm.cmds):
            return False
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "a|(bc)"
    vm = RegularExpression(regex)
    true_cmd = [
        RegCommand('split', 1, 3),
        RegCommand('char', 'a'),
        RegCommand('jmp', 5),
        RegCommand('char', 'b'),
        RegCommand('char', 'c'),
        RegCommand('match')
    ]
    reg = r'a|(bc)'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if k >= len(vm.cmds):
            return False
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "a+(b|c)*"
    vm = RegularExpression(regex)
    true_cmd = [
        RegCommand('char', 'a'),
        RegCommand('split', 0, 2),
        RegCommand('split', 3, 8),
        RegCommand('split', 4, 6),
        RegCommand('char', 'b'),
        RegCommand('jmp', 7),
        RegCommand('char', 'c'),
        RegCommand('jmp', 2),
        RegCommand('match')
    ]
    reg = r'a+(b|c)*'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if k >= len(vm.cmds):
            return False
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "(a|(b|c))"
    vm = RegularExpression(regex)
    true_cmd = [
        RegCommand('split', 1, 3),
        RegCommand('char', 'a'),
        RegCommand('jmp', 7),
        RegCommand('split', 4, 6),
        RegCommand('char', 'b'),
        RegCommand('jmp', 7),
        RegCommand('char', 'c'),
        RegCommand('match')
    ]
    reg = r'(a|(b|c))'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if k >= len(vm.cmds):
            return False
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "(a|(bc))d"
    vm = RegularExpression(regex)
    true_cmd = [
        RegCommand('split', 1, 3),
        RegCommand('char', 'a'),
        RegCommand('jmp', 5),
        RegCommand('char', 'b'),
        RegCommand('char', 'c'),
        RegCommand('char', 'd'),
        RegCommand('match')
    ]
    reg = r'(a|(bc))d'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if k >= len(vm.cmds):
            return False
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "a|(b)c*"
    vm = RegularExpression(regex)
    true_cmd = [
        RegCommand('split', 1, 3),
        RegCommand('char', 'a'),
        RegCommand('jmp', 7),
        RegCommand('char', 'b'),
        RegCommand('split', 5, 7),
        RegCommand('char', 'c'),
        RegCommand('jmp', 4),
        RegCommand('match')
    ]
    reg = r'a|(b)c*'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if k >= len(vm.cmds):
            return False
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    regex = "a|(b|c)d"
    vm = RegularExpression(regex)
    true_cmd = [
        RegCommand('split', 1, 3),
        RegCommand('char', 'a'),
        RegCommand('jmp', 8),
        RegCommand('split', 4, 6),
        RegCommand('char', 'b'),
        RegCommand('jmp', 7),
        RegCommand('char', 'c'),
        RegCommand('char', 'd'),
        RegCommand('match')
    ]
    reg = r'a|(b|c)d'
    for w in sequences:
        if re.fullmatch(reg, w):
            if not vm.check(w):
                return False
        else:
            if vm.check(w):
                return False
    for k in range(len(true_cmd)):
        if k >= len(vm.cmds):
            return False
        if vm.cmds[k].m != true_cmd[k].m or vm.cmds[k].n != true_cmd[k].n or vm.cmds[k].type != true_cmd[k].type:
            return False

    return True

def invalid_reg_test():
    good = ['a', 'b', 'aa', 'bb', 'a|b', '(a|b)', 'a*b', '(a|b)c', '(abc)', '(a|b)c(d|e)', 'a+|(bc)+|bc*|b?']
    bad = ['a|', 'a)b', '*a', 'a++', 'a|b|', 'a*?', '(a', 'a||b', '|a++', '(a|b))', 'a**(b|c)', '()', '']

    try:
        for el in good:
            vm = RegularExpression(el)
    except Exception:
        return False

    for el in bad:
        try:
            vm = RegularExpression(el)
        except Exception:
            continue
        return False

    return True
