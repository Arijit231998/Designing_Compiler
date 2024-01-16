def delete_left_recursion(grammar):
    new_grammar = {}
    non_terminals = {}

    for rule in grammar:
        left, right = rule.split(' -> ')
        productions = right.split(' | ')

        alpha_productions = []
        beta_productions = []

        for production in productions:
            if production.startswith(left):
                alpha_productions.append(production[len(left):])
            else:
                beta_productions.append(production)

        non_terminals[left] = (alpha_productions, beta_productions)

    for non_terminal, (alpha_productions, beta_productions) in non_terminals.items():
        if alpha_productions:
            new_non_terminal = non_terminal + "'"
            new_grammar[non_terminal] = []
            new_grammar[new_non_terminal] = []
            
            for beta_production in beta_productions:
                new_grammar[non_terminal].append(beta_production + " " + new_non_terminal)
            
            for alpha_production in alpha_productions:
                new_grammar[new_non_terminal].append(alpha_production + " " + new_non_terminal)
            
            new_grammar[new_non_terminal].append('ε')
        else:
            new_grammar[non_terminal] = beta_productions

    modified_grammar = []
    for non_terminal, productions in new_grammar.items():
        for production in productions:
            modified_grammar.append(f"{non_terminal} -> {production}")

    return modified_grammar

input_grammar = [
    "E -> E + T | T",
]

modified_grammar = delete_left_recursion(input_grammar)
print(input_grammar)
print("After deletion of left recursion, the grammar is:")
for rule in modified_grammar:
    print(rule)  
    