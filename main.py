from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
from automata.gram.gram import *

if __name__== "__main__":
  
  # ==========================================================================================
# # MINIMIZAÇÃO DE AUTOMATO DFA
    
    dfa = DFA(
        states={'q0', 'q1', 'q2'},
        input_symbols={'0', '1'},
        transitions={
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q0', '1': 'q2'},
            'q2': {'0': 'q2', '1': 'q1'}
        },
        initial_state='q0',
        final_states={'q1'}
        )
    print ('MINIMIZAÇÃO DE AUTOMATO DFA')
    minimal_dfa = dfa.minify()
    #print(minimal_dfa)

    print("Automata symbol",dfa.input_symbols)
    print("Automata states",dfa.states )
    print("Initiate state",dfa.initial_state)
    print("Transitions",dfa.transitions)
    print("Final states",dfa.final_states)

    print('\n')
# =========================================================================================
    # DETERMINIZAÇÃO COM YPSILONE('ε')
    print ("DETERMINIZATION OF AUTOMATA WITH YPSILONE('ε')")
    nfa = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q1'}},
        'q1': {'a': {'q1'}, 'ε': {'q2'}},
        'q2': {'b': {'q0'}}
    },
    initial_state='q0',
    final_states={'q1'}
    )
    
    dfa = DFA.from_nfa(nfa)
    #print(dfa)

    print("Automata symbol",dfa.input_symbols)
    print("Automata states",dfa.states )
    print("Initiate state",dfa.initial_state)
    print("Transitions",dfa.transitions)
    print("Final states",dfa.final_states)
    print('\n')
# =============================================================================================
    # # DETERMINIZAÇÃO SEM YPSILONE
    print ("DETERMINIZATION OF AUTOMATA WITHOUT SEM YPSILONE")
    nfa = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q0','q1'},'b':{'q0'}},
        # Use 'ε' as the key name for empty string (lambda/epsilon) transitions
        'q1': {'b': {'q2'}},
        'q2': {}
    },
    initial_state='q0',
    final_states={'q2'}
    )
    
    dfa = DFA.from_nfa(nfa)
    #print(dfa)


    print("Automata symbol",dfa.input_symbols)
    print("Automata states",dfa.states )
    print("Initiate state",dfa.initial_state)
    print("Transitions",dfa.transitions)
    print("Final states",dfa.final_states)
    print('\n')    
	# ==============================================================================================
# #AUTOMATO TO GRAMMAR
    print ("CONVERT AUTOMATA TO GRAMMAR")
    nfa = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q0','q1'},'b':{'q0'}},
        'q1': {'b': {'q2'}},
        'q2': {}
    },
    initial_state='q0',
    final_states={'q2','q0'}
    )

    gram=Auto_to_gram(nfa)
    print("grammar symbol",gram.symbols)
    print("grammar variable:", gram.variables)
    print("Initiate variable",gram.initial_variable)
    print("Grammar productions",gram.productions)
   
    print('\n')
#-------------------------------------------------------------------------------------------------

    # #GRAMMAR TO AUTOMATA TO GRAMMAR
    print ("CONVERT GRAMMAR TO AUTOMATA ")
    gram= GRAM(
    variables={'S', 'B'},
    symbols={'a', 'b','c'},
    productions={'S':{'aS','bB'},
                'B':{'bB','c'}
    },
    initial_variable='S' 
    )
    Gram_to_auto(gram)
    #print(aut)


