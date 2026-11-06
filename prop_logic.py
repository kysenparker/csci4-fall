def truth_table():
    print("p\tq\tr\t(p AND q) <-> r")

    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                result = (p and q) == r
                print(p, q, r, result, sep="\t")
truth_table()