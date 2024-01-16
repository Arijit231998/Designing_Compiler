def compute_first(grammar):
    first = {}
    for nonterminal in grammar:
        compute_first_recursive(grammar, nonterminal, first)
    return first # return the first after  checking 

def compute_first_recursive(grammar, symbol, first):
    if symbol in first:
        return 

    first[symbol] = set()#If the First set for the symbol has already been computed and is present in the first dictionary

    for production in grammar[symbol]:
        first_of_production = compute_first_of_production(grammar, production, first)  # Pass 'first' as a parameter
        first[symbol].update(first_of_production)

def compute_first_of_production(grammar, production, first):
    first_set = set()
    for symbol in production:
        if symbol in grammar:
            first_set.update(compute_first_of_production(grammar, grammar[symbol][0], first))
            if '#' not in first_set:
                break
        else:
            first_set.add(symbol)
            break
    return first_set

def compute_follow(grammar, first):
    follow = {nonterminal: set() for nonterminal in grammar}
    follow[list(grammar.keys())[0]].add('$')

    for nonterminal in grammar:
        compute_follow_recursive(grammar, nonterminal, first, follow)

    return follow

def compute_follow_recursive(grammar, symbol, first, follow):
    if symbol in first:
        return
    for nonterminal, productions in grammar.items():
        for production in productions:
            for i, s in enumerate(production):
                if s == symbol:
                    remaining = production[i + 1:]
                    first_of_remaining = compute_first_of_production(grammar, remaining, first)  # Pass 'first' as a parameter
                    follow[nonterminal].update(first_of_remaining - {'#'})
                    if '#' in first_of_remaining:
                        follow[nonterminal].update(compute_follow_recursive(grammar, nonterminal, first, follow))  # Pass 'first' as a parameter
                elif s in grammar:
                    first_of_s = compute_first_of_production(grammar, [s], first)  # Pass 'first' as a parameter
                    follow[s].update(first_of_s - {'#'})
                    if '#' in first_of_s:
                        follow[s].update(compute_follow_recursive(grammar, s, first, follow))  # Pass 'first' as a parameter

def parse_grammar(grammar_str):
    grammar = {}
    for line in grammar_str.split('\n'):
        line = line.strip()
        if not line:
            continue
        nonterminal, production = line.split('->')
        nonterminal = nonterminal.strip()
        production = [p.strip() for p in production.split('|')]
        grammar[nonterminal] = production
    return grammar

def main():
    grammar_str = """
    S -> aSe | B
    B -> bBCf | C
    C -> cCg | d | #
    """
    grammar = parse_grammar(grammar_str)

    first = compute_first(grammar)
    follow = compute_follow(grammar, first)

    for nonterminal, first_set in first.items():
        print(f'First ({nonterminal}) = {first_set}')

    for nonterminal, follow_set in follow.items():
        print(f'Follow ({nonterminal}) = {follow_set}')

if __name__ == "__main__":
    main()
