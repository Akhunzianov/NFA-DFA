from regulars import RegularExpression, RegCommand

def test():
    cmd = RegularExpression('a')
    true_cmd = [RegCommand('char', 'a'), RegCommand('match')]
    if cmd.cmds != true_cmd:
        return False

    cmd = RegularExpression('b')
    true_cmd = [RegCommand('char', 'b'), RegCommand('match')]
    if cmd.cmds != true_cmd:
        return False

    cmd = RegularExpression('aa')
    true_cmd = [RegCommand('char', 'a'),
                RegCommand('char', 'a'),
                RegCommand('match')]
    if cmd.cmds != true_cmd:
        return False

    cmd = RegularExpression('bb')
    true_cmd = [RegCommand('char', 'b'),
                RegCommand('char', 'b'),
                RegCommand('match')]
    if cmd.cmds != true_cmd:
        return False

    cmd = RegularExpression('ab')
    true_cmd = [RegCommand('char', 'a'),
                RegCommand('char', 'b'),
                RegCommand('match')]
    if cmd.cmds != true_cmd:
        return False

    cmd = RegularExpression('a|b')
    true_cmd = [RegCommand('split', 1, 3),
                RegCommand('char', 'a'),
                RegCommand('jmp', 4),
                RegCommand('char', 'b'),
                RegCommand('match')]
    if cmd.cmds != true_cmd:
        return False

    cmd = RegularExpression('a+b+')
    true_cmd = [
        RegCommand('char', 'a'),
        RegCommand('split', 0, 2),
        RegCommand('char', 'b'),
        RegCommand('split', 2, 4),
        RegCommand('match')
    ]
    if cmd.cmds != true_cmd:
        return False

    cmd = RegularExpression('a*')
    true_cmd = [
        RegCommand('split', 1, 3),
        RegCommand('char', 'a'),
        RegCommand('jmp', 0),
        RegCommand('match')
    ]
    if cmd.cmds != true_cmd:
        return False

    cmd = RegularExpression('b+')
    true_cmd = [
        RegCommand('char', 'b'),
        RegCommand('split', 0, 2),
        RegCommand('match')
    ]
    if cmd.cmds != true_cmd:
        return False

    cmd = RegularExpression('ab*')
    true_cmd = [
        RegCommand('char', 'a'),
        RegCommand('split', 2, 4),
        RegCommand('char', 'b'),
        RegCommand('jmp', 1),
        RegCommand('match')
    ]
    if cmd.cmds != true_cmd:
        return False

    cmd = RegularExpression('a?b')
    true_cmd = [
        RegCommand('split', 1, 3),
        RegCommand('char', 'a'),
        RegCommand('char', 'b'),
        RegCommand('match')
    ]
    if cmd.cmds != true_cmd:
        return False

    cmd = RegularExpression('a|b*')
    true_cmd = [
        RegCommand('split', 1, 4),
        RegCommand('char', 'a'),
        RegCommand('jmp', 6),
        RegCommand('split', 4, 5),
        RegCommand('char', 'b'),
        RegCommand('jmp', 4),
        RegCommand('match')
    ]
    if cmd.cmds != true_cmd:
        return False

    cmd = RegularExpression('a|b|ba')
    true_cmd = [
        RegCommand('split', 1, 3),
        RegCommand('char', 'a'),
        RegCommand('jmp', 7),
        RegCommand('split', 4, 6),
        RegCommand('char', 'b'),
        RegCommand('jmp', 7),
        RegCommand('char', 'b'),
        RegCommand('char', 'a'),
        RegCommand('match')
    ]
    if cmd.cmds != true_cmd:
        return False

    cmd = RegularExpression('a+|b?a|a+b')
    true_cmd = [
        RegCommand('split', 1, 4),
        RegCommand('char', 'a'),
        RegCommand('split', 1, 3),
        RegCommand('jmp', 12),
        RegCommand('split', 5, 6),
        RegCommand('split', 6, 7),
        RegCommand('char', 'b'),
        RegCommand('char', 'a'),
        RegCommand('jmp', 12),
        RegCommand('char', 'a'),
        RegCommand('split', 9, 11),
        RegCommand('char', 'b'),
        RegCommand('match')
    ]
    if cmd.cmds != true_cmd:
        return False


    return True