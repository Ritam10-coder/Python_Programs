def geometric_sequence(start, ratio, terms):
    sequence = []
    current_term = start
    for i in range(terms):
        sequence.append(current_term)
        current_term *= ratio
    
    return sequence
start = 2
ratio = 3
terms = 6
sequence = geometric_sequence(start, ratio, terms)

for i, term in enumerate(sequence, start=1):
    print(f"Term {i}: {term}")
