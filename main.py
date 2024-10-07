from nfa_dfa import parse_file
from nfa_dfa_conversion import convert
import os


def run_nfa_dfa_tests():
    directory = 'dfa_nfa_tests/automats'
    directory2 = 'dfa_nfa_tests/strings'
    for filename in os.listdir(directory):
        nfa = parse_file(directory + '/' + filename)
        with open(directory2 + '/' + filename) as f:
            for line in f:
                test = line.strip().split(', ')
                word = list(map(int, test[0].split()))
                real_res = False
                if test[1] == 'true':
                    real_res = True
                if real_res != nfa.check_word(word):
                    print('1. Not all tests passed')
                    return
    print('1. All tests passed')


def run_conversion_tests():
    directory = 'dfa_nfa_tests/automats'
    directory2 = 'dfa_nfa_tests/strings'
    for filename in os.listdir(directory):
        nfa = parse_file(directory + '/' + filename)
        dfa = convert(nfa)
        with open(directory2 + '/' + filename) as f:
            for line in f:
                test = line.strip().split(', ')
                word = list(map(int, test[0].split()))
                real_res = False
                if test[1] == 'true':
                    real_res = True
                if real_res != dfa.check_word(word):
                    print('2. Not all tests passed')
                    return
    print('2. All tests passed')


def main():
    run_nfa_dfa_tests()
    run_conversion_tests()


if __name__ == "__main__":
    main()
