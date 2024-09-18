def find_content_children(g, s):
    g.sort()
    s.sort()
    
    child_i = 0
    cookie_i = 0
    
    while child_i < len(g) and cookie_i < len(s):
        if s[cookie_i] >= g[child_i]:
            child_i += 1
        cookie_i += 1
    
    return child_i

test_cases = [
    ([1, 2, 3], [1, 1])
]

results = [find_content_children(g, s) for g, s in test_cases]

for (g, s), result in zip(test_cases, results):
    print(f"For greed factors {g} and cookie sizes {s}, the maximum number of content children is {result}")
