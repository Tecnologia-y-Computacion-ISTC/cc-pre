

def implies(p: bool, q: bool) -> bool:
    return (not p) or q

def row(p, q):
    return {
        "p": p,
        "q": q,
        "p AND q": p and q,
        "p OR q": p or q,
        "p -> q": implies(p, q),
    }

def print_table():
    headers = ["p", "q", "p AND q", "p OR q", "p -> q"]
    print("\t".join(headers))
    for p in [False, True]:
        for q in [False, True]:
            r = row(p, q)
            print(" - ".join(str(r[h]) for h in headers))

if __name__ == "__main__":
    print_table()
