from nfa import NFA 

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

    # Define A_3
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

    # List of automata and their names
    automata = {'A_1': A_1, 'A_2': A_2, 'A_3': A_3, 'A_4': A_4}

    # Test cases
    test_words = ['0', '00', '01', '10', '0001', '000', '111', '1010', '1100', '1111', '10001']

    # Run each automaton on all test words
    for name, automaton in automata.items():
        print(f"Results for {name}:")
        for word in test_words:
            result = automaton.run(word)
            print(f"  Word '{word}' accepted? {result}")
        print()  # Blank line for separation

if __name__ == "__main__":
    main()
