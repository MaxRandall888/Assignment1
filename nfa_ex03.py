from nfa import NFA
from dfa import DFA  # Make sure your DFA class is accessible

def main():
    # Define A_1
    Q1 = {'q0', 'q1'}
    Sigma1 = {'0', '1'}
    delta1 = {
        ('q0', '0'): {'q0', 'q1'},
        ('q1', '1'): {'q0'}
    }
    q0_1 = 'q0'
    F1 = {'q1'}
    A_1 = NFA(Q1, Sigma1, delta1, q0_1, F1)

    # Define A_2
    Q2 = {'q0', 'q1', 'q2'}
    Sigma2 = {'0', '1'}
    delta2 = {
        ('q0', '0'): {'q0', 'q1'},
        ('q0', '1'): {'q0'},
        ('q1', '1'): {'q2'},
        ('q2', '0'): {'q2'},
        ('q2', '1'): {'q2'}
    }
    q0_2 = 'q0'
    F2 = {'q2'}
    A_2 = NFA(Q2, Sigma2, delta2, q0_2, F2)

    # Define A_3 (same as A_2 but with accepting states q0 and q1)
    Q3 = {'q0', 'q1', 'q2'}
    Sigma3 = {'0', '1'}
    delta3 = {
        ('q0', '0'): {'q0', 'q1'},
        ('q0', '1'): {'q0'},
        ('q1', '1'): {'q2'},
        ('q2', '0'): {'q2'},
        ('q2', '1'): {'q2'}
    }
    q0_3 = 'q0'
    F3 = {'q0', 'q1'}
    A_3 = NFA(Q3, Sigma3, delta3, q0_3, F3)

    # Define A_4
    Q4 = {'q0', 'q1', 'q2', 'q3', 'q4'}
    Sigma4 = {'0', '1'}
    delta4 = {
        ('q0', '0'): {'q0'},
        ('q0', '1'): {'q0', 'q1'},
        ('q1', '0'): {'q2'},
        ('q1', '1'): {'q2'},
        ('q2', '0'): {'q3'},
        ('q2', '1'): {'q3'},
        ('q3', '0'): {'q4'},
        ('q3', '1'): {'q4'},
        ('q4', '0'): {'q4'},
        ('q4', '1'): {'q4'}
    }
    q0_4 = 'q0'
    F4 = {'q4'}
    A_4 = NFA(Q4, Sigma4, delta4, q0_4, F4)

    # Define A_5: A new automaton with an unreachable state.
    # Here, Q5 contains 'q2' which is unreachable from the initial state 'q0'.
    Q5 = {'q0', 'q1', 'q2'}
    Sigma5 = {'a', 'b'}
    delta5 = {
        ('q0', 'a'): {'q1'},
        ('q1', 'b'): {'q0'},
        # 'q2' never appears in any transition from a reachable state.
    }
    q0_5 = 'q0'
    F5 = {'q1', 'q2'}  # Although q2 is accepting, it will never be reached.
    A_5 = NFA(Q5, Sigma5, delta5, q0_5, F5)

    # Collect all automata in a dictionary.
    automata = {
        'A_1': A_1,
        'A_2': A_2,
        'A_3': A_3,
        'A_4': A_4,
        'A_5': A_5,
    }

    # Define a set of test words that cover various cases (including empty and longer words).
    test_words = [
        '',      # empty word
        '0', '1', '00', '01', '10', '11',
        '000', '1010', '1100', '0011', '0101',
        'a', 'b', 'ab', 'ba'
    ]

    # Test each automaton: run the NFA and then its converted DFA.
    for name, nfa in automata.items():
        print(f"--- Testing Automaton {name} ---")
        print("Original NFA results:")
        for w in test_words:
            try:
                res = nfa.run(w)
            except Exception as e:
                res = f"Error: {e}"
            print(f"  {w!r}: {res}")
        
        # Convert the NFA to a DFA (this DFA only contains reachable states).
        dfa_conv = nfa.to_DFA()
        print("Converted DFA results:")
        for w in test_words:
            try:
                res = dfa_conv.run(w)
            except Exception as e:
                res = f"Error: {e}"
            print(f"  {w!r}: {res}")
        print("\n")

if __name__ == "__main__":
    main()
