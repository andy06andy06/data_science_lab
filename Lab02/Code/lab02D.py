from collections import defaultdict

def reverse_lookup(d, v):
    k = []

    inverted_d = defaultdict(list)
    for x, y in d.items():
        inverted_d[y].append(x)
    k = inverted_d[v]
    
    return k