import queue


class NfaDfa:
    def __init__(self, states_number: int, alphabet_number: int, starting_states: set[int],
                 finish_states: set[int], transitions: dict) -> None:
        self.states = [i for i in range(0, states_number)]
        self.alphabet = [i for i in range(0, alphabet_number)]
        self.starting_states = starting_states
        self.finish_states = finish_states
        self.transitions = transitions

    def get_epsilon(self, state: int) -> set:
        if (state, -1) in self.transitions:
            return self.transitions[(state, -1)]
        return set()

    def get_transitions(self, state: int, letter: int) -> set:
        if (state, letter) in self.transitions:
            return self.transitions[(state, letter)]
        return set()

    def check_word(self, word: list[int]) -> bool:
        visited = set()
        pointer = 0
        que = queue.Queue()
        was_last_trans_eps = 0
        for el in self.starting_states:
            que.put((el, pointer, was_last_trans_eps))
        while que.qsize() > 0:
            state, pointer, was_last_trans_eps = que.get()
            if (state, pointer, was_last_trans_eps) in visited:
                continue
            else:
                visited.add((state, pointer, was_last_trans_eps))
            if pointer == len(word) and state in self.finish_states:
                return True
            elif pointer == len(word) and was_last_trans_eps == 0:
                eps = self.get_epsilon(state)
                for el in eps:
                    que.put((el, pointer, 1))
            elif pointer == len(word):
                continue
            else:
                transits = self.get_transitions(state, word[pointer])
                eps = self.get_epsilon(state)
                for el in transits:
                    que.put((el, pointer + 1, 0))
                if was_last_trans_eps == 0:
                    for el in eps:
                        que.put((el, pointer, 1))
        return False


def all_epsilon_reachable(transitions: dict, state: int, already_counted: set[int]) -> set[int]:
    if (state, -1) in transitions:
        for el in transitions[(state, -1)]:
            if el not in already_counted:
                already_counted.add(el)
                already_counted = already_counted.union(all_epsilon_reachable(transitions, el, already_counted))
        return already_counted
    return set()


def parse_file(file_name: str) -> NfaDfa:
    with open(file_name, 'r') as file:
        lines = file.readlines()

        states_number = int(lines[0].strip())
        alphabet_number = int(lines[1].strip())
        starting_states = set(map(int, lines[2].strip().split()))
        finish_states = set(map(int, lines[3].strip().split()))

        transitions = dict()
        for i in range(4, len(lines)):
            beg_state, letter, end_state = map(int, lines[i].strip().split())
            if (beg_state, letter) in transitions:
                temp = transitions[beg_state, letter]
                temp.add(end_state)
                transitions[(beg_state, letter)] = temp
            else:
                transitions[(beg_state, letter)] = {end_state}

        for i in range(states_number):
            if (i, -1) in transitions:
                transitions[(i, -1)] = all_epsilon_reachable(transitions, i, set())

        return NfaDfa(states_number, alphabet_number, starting_states, finish_states, transitions)

