from nfa_dfa import parse_file
from nfa_dfa_conversion import convert
from regex_tests.tests import test
from dfa_minimization import minimize_dfa, is_equivalent, is_accepting_all_words
from regex_tests.antlr_tests import invalid_reg_test, test_regex_matching
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
    directory3 = 'dfa_nfa_tests/expected_dfa'
    for filename in os.listdir(directory):
        nfa = parse_file(directory + '/' + filename)
        dfa = convert(nfa)
        expected_dfa = parse_file(directory3 + '/' + filename)
        if not is_equivalent(minimize_dfa(dfa), minimize_dfa(expected_dfa)):
            print('2. Not all tests passed')
            return
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


def run_minimization_test():
    directory = 'min_tests'

    dfa1 = parse_file(directory + '/' + 'ending01.txt')
    dfa2 = parse_file(directory + '/' + 'ending01_opt.txt')
    dfa1_min = minimize_dfa(dfa1)
    if not is_equivalent(dfa1_min, dfa2) and not is_accepting_all_words(dfa1_min):
        print('3. Not all tests passed')
        return

    dfa1 = parse_file(directory + '/' + 'ending1.txt')
    dfa2 = parse_file(directory + '/' + 'ending1_opt.txt')
    dfa1_min = minimize_dfa(dfa1)
    if not is_equivalent(dfa1_min, dfa2) and not is_accepting_all_words(dfa1_min):
        print('3. Not all tests passed')
        return

    dfa1 = parse_file(directory + '/' + 'contains1.txt')
    dfa2 = parse_file(directory + '/' + 'contains1_opt.txt')
    dfa1_min = minimize_dfa(dfa1)
    if not is_equivalent(dfa1_min, dfa2) and not is_accepting_all_words(dfa1_min):
        print('3. Not all tests passed')
        return

    print('3. All tests passed')

    dfa1 = parse_file(directory + '/' + 'all_accepting.txt')
    dfa2 = parse_file(directory + '/' + 'all_accepting_opt.txt')
    dfa1_min = minimize_dfa(dfa1)
    if not is_equivalent(dfa1_min, dfa2) and is_accepting_all_words(dfa1_min):
        print('3. Not all tests passed')
        return

    print('3. All tests passed')


def run_regex_tests():
    if test():
        print('4. All tests passed')
    else:
        print('4. Not all tests passed')


def run_new_regex_tests():
    if invalid_reg_test() and test_regex_matching():
        print('5. All tests passed')
    else:
        print('5. Not all tests passed')


def main():
    run_nfa_dfa_tests()
    run_conversion_tests()
    run_minimization_test()
    run_regex_tests()
    run_new_regex_tests()



if __name__ == "__main__":
    main()
