from dfa import DFA

class NFA:
    def __init__(self, Q, Sigma, delta, q0, F):
        """
        Q: a set of states
        Sigma: the alphabet (set of symbols)
        delta: the transition function, a dict mapping (state, symbol) -> set of states
        q0: the initial state
        F: set of accepting (final) states
        """
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

    def __repr__(self):
        return f"NFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    def run(self, w):
        """
        Simulate the NFA on input string w.
        Returns True if the word is accepted (i.e. at least one computation
        reaches a final state) and False otherwise.
        """
        # Start with the initial state.
        current_states = {self.q0}
        
        # Process each symbol in the input word.
        for symbol in w:
            next_states = set()
            for state in current_states:
                # Get the next states; if there's no transition, default to empty set.
                transitions = self.delta.get((state, symbol), set())
                next_states.update(transitions)
            current_states = next_states

        # If any of the current states is a final state, the word is accepted.
        return any(state in self.F for state in current_states)
    
    def to_DFA(self):
        # The initial DFA state is the frozenset containing only the NFA's start state.
        start = frozenset({self.q0})
        
        # Worklist for unprocessed DFA states
        unmarked = [start]
        
        # Set of DFA states (each state is a frozenset of NFA states)
        dfa_states = {start}
        
        # DFA transition function: keys are (dfa_state, symbol), values are dfa_states.
        dfa_delta = {}
        
        while unmarked:
            current = unmarked.pop()
            for symbol in self.Sigma:
                # For each symbol, compute the union of transitions from all states in 'current'
                next_states = set()
                for state in current:
                    next_states.update(self.delta.get((state, symbol), set()))
                next_state = frozenset(next_states)
                
                # Record the transition for the DFA.
                dfa_delta[(current, symbol)] = next_state
                
                # If this state hasn't been seen before, add it to the unmarked list.
                if next_state not in dfa_states:
                    dfa_states.add(next_state)
                    unmarked.append(next_state)
        
        # Define the DFA's accepting states: those that intersect with the NFA's accepting states.
        dfa_F = {state for state in dfa_states if state & self.F}
        
        # Return the constructed DFA.
        return DFA(dfa_states, self.Sigma, dfa_delta, start, dfa_F)
    

"""
What do you notice about the resulting DFAs?

1. **Equivalent Language Recognition**: 
   - The DFAs produced by `to_DFA()` recognize the same language as the original NFAs.
   - Running the same test words on both the NFA and its converted DFA results in the same accept/reject decisions.

2. **State Explosion in Some Cases**: 
   - The DFA states correspond to subsets of NFA states, which can lead to an exponential growth in the number of states.
   - However, in practical cases (like A_1 to A_4), the resulting DFA often has a manageable number of states.

3. **Pruning of Unreachable States**: 
   - The DFA only includes states that can be reached from the initial NFA state.
   - This is evident in the case of A_5, where `q2` exists in the NFA but is absent in the DFA since no transition leads to it from `q0`.

4. **Deterministic Transitions**: 
   - Unlike the NFA, which can transition to multiple states for a given (state, symbol) pair, the DFA always transitions to exactly one state.
   - This removes non-determinism, making the DFA easier to simulate and analyze.

5. **Increased Determinism at the Cost of More States**: 
   - NFAs can "guess" the correct path using non-deterministic transitions.
   - The resulting DFA must account for all possible paths explicitly, which often leads to additional states.
"""
