def truth_table():
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                result = (p and q) == r
                print(p, q, r, result)
truth_table()