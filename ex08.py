import itertools

class Factor:
    def __init__(self, variables, table):
        self.variables = variables
        self.table = table

def multiply(f1, f2):
    vars_new = list(set(f1.variables) | set(f2.variables))
    table_new = {}
    for assignment in itertools.product([True, False], repeat=len(vars_new)):
        assign = dict(zip(vars_new, assignment))
        p1 = f1.table.get(tuple(assign[v] for v in f1.variables), 0)
        p2 = f2.table.get(tuple(assign[v] for v in f2.variables), 0)
        table_new[tuple(assign[v] for v in vars_new)] = p1 * p2
    return Factor(vars_new, table_new)

def marginalize(factor, var):
    vars_new = [v for v in factor.variables if v != var]
    table_new = {}
    for assignment in itertools.product([True, False], repeat=len(vars_new)):
        prob = 0
        for val in [True, False]:
            full = dict(zip(vars_new, assignment))
            full[var] = val
            prob += factor.table.get(tuple(full[v] for v in factor.variables), 0)
        table_new[assignment] = prob
    return Factor(vars_new, table_new)

def restrict(factor, var, val):
    vars_new = [v for v in factor.variables if v != var]
    table_new = {}
    for assignment in itertools.product([True, False], repeat=len(vars_new)):
        full = dict(zip(vars_new, assignment))
        full[var] = val
        table_new[assignment] = factor.table.get(tuple(full[v] for v in factor.variables), 0)
    return Factor(vars_new, table_new)

def normalize(factor, query):
    dist, total = {}, 0.0
    for assignment, prob in factor.table.items():
        assign_dict = dict(zip(factor.variables, assignment))
        val = assign_dict[query]
        dist[val] = dist.get(val, 0) + prob
        total += prob
    if total == 0:
        return {k: 1/len(dist) for k in dist}
    return {k: v/total for k, v in dist.items()}

def variable_elimination(factors, query, evidence, hidden):
    for ev, val in evidence.items():
        factors = [restrict(f, ev, val) if ev in f.variables else f for f in factors]
    for var in hidden:
        rel = [f for f in factors if var in f.variables]
        if rel:
            prod = rel[0]
            for f in rel[1:]:
                prod = multiply(prod, f)
            summed = marginalize(prod, var)
            factors = [f for f in factors if f not in rel] + [summed]
    joint = factors[0]
    for f in factors[1:]:
        joint = multiply(joint, f)
    return normalize(joint, query)

# Define Burglary network
B = Factor(["B"], {(True,): 0.001, (False,): 0.999})
E = Factor(["E"], {(True,): 0.002, (False,): 0.998})
A = Factor(["A","B","E"], {
    (True,True,True): 0.95, (False,True,True): 0.05,
    (True,True,False): 0.94, (False,True,False): 0.06,
    (True,False,True): 0.29, (False,False,True): 0.71,
    (True,False,False): 0.001, (False,False,False): 0.999
})
J = Factor(["J","A"], {(True,True): 0.9, (False,True): 0.1,
                       (True,False): 0.05, (False,False): 0.95})
M = Factor(["M","A"], {(True,True): 0.7, (False,True): 0.3,
                       (True,False): 0.01, (False,False): 0.99})

factors = [B,E,A,J,M]
evidence = {"J":True,"M":True}
hidden = ["A","E"]

print("P(B | J=1, M=1):", variable_elimination(factors,"B",evidence,hidden))
