# Rule-based reasoning system: Forward & Backward Chaining

# Knowledge Base: rules are (premises -> conclusion)
rules = [
    (["A", "B"], "C"),
    (["C"], "D"),
    (["D", "E"], "F")
]

# Initial facts
facts = {"A", "B", "E"}

# Forward Chaining
def forward_chaining(rules, facts, goal):
    inferred = set(facts)
    changed = True

    while changed:
        changed = False
        for premises, conclusion in rules:
            if all(p in inferred for p in premises) and conclusion not in inferred:
                inferred.add(conclusion)
                changed = True
                if conclusion == goal:
                    return True, inferred
    return goal in inferred, inferred

# Backward Chaining
def backward_chaining(rules, facts, goal):
    if goal in facts:
        return True
    for premises, conclusion in rules:
        if conclusion == goal:
            if all(backward_chaining(rules, facts, p) for p in premises):
                return True
    return False


goal = "F"

fc_result, fc_facts = forward_chaining(rules, facts, goal)
print("Forward Chaining: Goal", goal, "->", fc_result, "| Facts:", fc_facts)

bc_result = backward_chaining(rules, facts, goal)
print("Backward Chaining: Goal", goal, "->", bc_result)
