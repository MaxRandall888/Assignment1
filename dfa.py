import nfa

class DFA:
    # Initialize the DFA
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q  # Set of states
        self.Sigma = Sigma  # Alphabet
        self.delta = delta  # Transition function (dict mapping (state, symbol) to a single state)
        self.q0 = q0  # Initial state
        self.F = F  # Set of accepting states

    # String representation of the DFA
    def __repr__(self):
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    # Runs the DFA on an input string w
    def run(self, w):
        current_state = self.q0  # Start at initial state
        loop = 0
        for symbol in w:
            loop += 1
            if symbol not in self.Sigma:
                return False  # Reject if symbol is not in the alphabet
            if (current_state, symbol) not in self.delta:
                return False  # Reject if there's no valid transition
            current_state = self.delta[(current_state, symbol)]  # Move to next state
        return current_state in self.F  # Accept if final state is in F

    # Constructs an NFA equivalent to this DFA
    def to_NFA(self):
        # Convert DFA's transition function to the NFA's format:
        # For each (state, symbol) in the DFA, the NFA's delta is a set containing the single DFA destination.
        nfa_delta = {}
        for (state, symbol), next_state in self.delta.items():
            nfa_delta[(state, symbol)] = {next_state}
        # Return an NFA with the same states, alphabet, initial state, and final states.
        return nfa.NFA(self.Q, self.Sigma, nfa_delta, self.q0, self.F)
