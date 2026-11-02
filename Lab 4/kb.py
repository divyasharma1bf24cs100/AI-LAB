import itertools
def evaluate_kb(p, q, r):
    rule1 = (not p) or q   
    rule2 = (not q) or r   
    fact = p              
    return rule1 and rule2 and fact
def tt_entails():
    models = list(itertools.product([True, False], repeat=3))
    for p, q, r in models:
        kb_val = evaluate_kb(p, q, r)
        query_val = r 
        if kb_val and not query_val:
            return False
    return True
query = "R"
if tt_entails():
    print(f"Yes, KB entails the query ({query}).")
else:
    print(f"No, KB does not entail the query ({query}).")
