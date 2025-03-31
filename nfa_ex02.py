import dfa
from nfa import NFA  # Make sure your NFA class (with the run method) is available

def refuse(A):
    """Constructs a DFA A0 that accepts exactly the words that A refuses and vice versa."""
    Q0 = A.Q
    Sigma0 = A.Sigma
    delta0 = A.delta
    q0_0 = A.q0
    F0 = Q0 - A.F  # Complement of the accepting states
    return dfa.DFA(Q0, Sigma0, delta0, q0_0, F0)


# generate words for testing
def generate_words():
    words = []
    alphabet = ['a', 'b']
    for first in alphabet:
        for second in alphabet:
            for third in alphabet:
                words.append(first + second + third)
    return words

def __main__():
    # Define DFA A
    Q = {1, 2, 3, 4}
    Sigma = {'a', 'b'}
    delta = {
        (1, 'a'): 2, (1, 'b'): 4,
        (2, 'a'): 3, (2, 'b'): 4,
        (3, 'a'): 3, (3, 'b'): 3,
        (4, 'a'): 2, (4, 'b'): 3
    }
    q0 = 1
    F = {4}
    A = dfa.DFA(Q, Sigma, delta, q0, F)

    # Generate DFA A0 (complement of A)
    A0 = refuse(A)
    
    # DFA A1
    Q = {1, 2, 3, 4}
    Sigma = {'a', 'b'}
    delta = {
        (1, 'a'): 2, (1, 'b'): 4,
        (2, 'a'): 2, (2, 'b'): 3,
        (3, 'a'): 2, (3, 'b'): 2,
        (4, 'a'): 4, (4, 'b'): 4
    }
    q0 = 1
    F = {3}
    A1 = dfa.DFA(Q, Sigma, delta, q0, F)
    
    # DFA A2
    Q = {1, 2, 3}
    Sigma = {'a', 'b'}
    delta = {
        (1, 'a'): 2, (1, 'b'): 1,
        (2, 'a'): 3, (2, 'b'): 1,
        (3, 'a'): 3, (3, 'b'): 1
    }
    q0 = 1
    F = {3}
    A2 = dfa.DFA(Q, Sigma, delta, q0, F)
    
    # Generate test words
    words = generate_words()
    words += ['aaaaaaaaabbbbbb', 'babbbbbbbbbbbbbbb']
    
    # List of DFAs from the first lab
    automata_dfa = [A1, A2, A, A0]
    # Convert each DFA to its equivalent NFA using the to_NFA method
    automata_nfa = [X.to_NFA() for X in automata_dfa]
    
    print("=== Testing DFAs ===")
    for X in automata_dfa:
        print(X)
        for w in words:
            print(f"{w}: {X.run(w)}")
        print("\n")
    
    print("=== Testing corresponding NFAs ===")
    for i, X in enumerate(automata_nfa):
        print(f"NFA corresponding to DFA {i+1}:")
        for w in words:
            print(f"{w}: {X.run(w)}")
        print("\n")

__main__()
