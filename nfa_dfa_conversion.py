from nfa_dfa import NfaDfa, parse_file

starting_state = 0


def find_ways(current_nodes: set[int], nfa: NfaDfa, dfa_node_sets: list[set[int]], dfa_transitions: dict,
              came_from_state: int, came_by_letter: int):
    for el in current_nodes:
        if (el, -1) in nfa.transitions:
            current_nodes = current_nodes.union(nfa.transitions[(el, -1)])
    if current_nodes not in dfa_node_sets:
        dfa_node_sets.append(current_nodes)
        if came_by_letter == -1:
            global starting_state
            starting_state = came_from_state
        else:
            dfa_transitions[(came_from_state, came_by_letter)] = {len(dfa_node_sets) - 1}
        ind = len(dfa_node_sets) - 1
        for buk in nfa.alphabet:
            new_set = set()
            for el in current_nodes:
                if (el, buk) in nfa.transitions:
                    new_set = new_set.union(nfa.transitions[(el, buk)])
            find_ways(new_set, nfa, dfa_node_sets, dfa_transitions, ind, buk)
    else:
        dfa_transitions[(came_from_state, came_by_letter)] = {dfa_node_sets.index(current_nodes)}


def convert(nfa: NfaDfa) -> NfaDfa:
    dfa_node_sets = []
    dfa_transitions = dict()
    find_ways(nfa.starting_states, nfa, dfa_node_sets, dfa_transitions, 0, -1)
    finish_states = set()
    for i in range(len(dfa_node_sets)):
        for q in nfa.finish_states:
            if q in dfa_node_sets[i]:
                finish_states.add(i)
    return NfaDfa(len(dfa_node_sets), len(nfa.alphabet), {starting_state}, finish_states, dfa_transitions)