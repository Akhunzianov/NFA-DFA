import queue

from nfa_dfa import NfaDfa


def delete_unreachable(input_dfa: NfaDfa) -> NfaDfa:
    reachable_states = []
    bfs_que = queue.Queue()
    bfs_que.put(next(iter(input_dfa.starting_states)))
    while bfs_que.qsize() > 0:
        curr_state = bfs_que.get()
        if curr_state in reachable_states:
            continue
        reachable_states.append(curr_state)
        for symb in input_dfa.alphabet:
            for el in input_dfa.transitions[(curr_state, symb)]:
                if el not in reachable_states:
                    bfs_que.put(el)
    set_new_states = set(reachable_states)
    input_dfa.states = set_new_states
    input_dfa.finish_states = input_dfa.finish_states.intersection(set_new_states)
    new_transitions = dict()
    for key in input_dfa.transitions:
        if key[0] in reachable_states:
            new_transitions[key] = input_dfa.transitions[key]
    input_dfa.transitions = new_transitions

    return input_dfa


def find_state_group_index(state: int, groups: list[set]) -> int:
    for i in range(len(groups)):
        if state in groups[i]:
            return i
    return -1


def minimize_dfa(input_dfa: NfaDfa) -> NfaDfa:
    input_dfa = delete_unreachable(input_dfa)
    groups = [input_dfa.finish_states]
    set_of_states = set(input_dfa.states)
    if len(input_dfa.finish_states) != len(input_dfa.states):
        groups.append(set_of_states.difference(input_dfa.finish_states))
    while True:
        flag = False
        last_added = 0
        for i in range(len(groups)):
            if last_added > 0:
                last_added -= 1
                continue
            for symb in input_dfa.alphabet:
                sorted_by_following_groups = dict()
                for state in groups[i]:
                    following_state = next(iter(input_dfa.transitions[(state, symb)]))
                    following_state_group = find_state_group_index(following_state, groups)
                    if following_state_group in sorted_by_following_groups:
                        temp = sorted_by_following_groups[following_state_group]
                        temp.add(state)
                        sorted_by_following_groups[following_state_group] = temp
                    else:
                        sorted_by_following_groups[following_state_group] = {state}
                if len(sorted_by_following_groups) > 1:
                    new_chunk = []
                    for el in sorted_by_following_groups:
                        new_chunk.append(sorted_by_following_groups[el])
                    groups = groups[:i] + new_chunk + groups[i + 1:]
                    flag = True
                    last_added = len(new_chunk) - 1
                    break
        if not flag:
            break
    new_starting_state = 0
    new_finish_states = set()
    new_transitions = dict()
    for i in range(len(groups)):
        if next(iter(input_dfa.starting_states)) in groups[i]:
            new_starting_state = i
        if next(iter(groups[i])) in input_dfa.finish_states:
            new_finish_states.add(i)
        for symb in input_dfa.alphabet:
            new_transitions[(i, symb)] = {
                find_state_group_index(next(iter(input_dfa.transitions[(next(iter(groups[i])), symb)])), groups)}

    return NfaDfa(len(groups), len(input_dfa.alphabet), {new_starting_state}, new_finish_states, new_transitions)


def is_equivalent(first_dfa: NfaDfa, second_dfa: NfaDfa) -> bool:
    first_dfa_min = minimize_dfa(first_dfa)
    second_dfa_min = minimize_dfa(second_dfa)
    if first_dfa_min.states != second_dfa_min.states:
        return False
    if first_dfa_min.alphabet != second_dfa_min.alphabet:
        return False
    if len(first_dfa_min.finish_states) != len(second_dfa_min.finish_states):
        return False
    matched_qs = dict()
    matched_qs[next(iter(first_dfa_min.starting_states))] = next(iter(second_dfa_min.starting_states))
    que = queue.Queue()
    que.put(next(iter(first_dfa_min.starting_states)))
    checked = set()
    while que.qsize() > 0:
        curr_state = que.get()
        if curr_state in checked:
            continue
        for symb in first_dfa_min.alphabet:
            new_first_st = next(iter(first_dfa_min.transitions[(curr_state, symb)]))
            new_second_st = next(iter(second_dfa_min.transitions[(matched_qs[curr_state], symb)]))
            for el in matched_qs:
                if el == new_first_st and matched_qs[el] != new_second_st:
                    return False
                if el != new_first_st and matched_qs[el] == new_second_st:
                    return False
                if new_first_st in first_dfa_min.finish_states and new_first_st not in first_dfa_min.finish_states:
                    return False
                if new_first_st not in first_dfa_min.finish_states and new_first_st in first_dfa_min.finish_states:
                    return False
            matched_qs[new_first_st] = new_second_st
            que.put(new_first_st)
        checked.add(curr_state)
    return True


def is_accepting_all_words(dfa: NfaDfa) -> bool:
    dfa_min = minimize_dfa(dfa)
    if dfa_min.finish_states == {0} and dfa_min.states == {0}:
        return True
    return False