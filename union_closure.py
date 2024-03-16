def find_closure(family):
    closure = family.copy()
    updated = True
    while updated:
        updated = False
        for s1 in closure:
            for s2 in closure:
                if s1 != s2 and s1.union(s2) not in closure:
                    closure.append(s1.union(s2))
                    updated = True
    return closure