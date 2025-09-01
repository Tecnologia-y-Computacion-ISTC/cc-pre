# archivo: semana-01/dia-01/truth_tables.py

def implies(p: bool, q: bool) -> bool:
    """
    Calcula el valor de verdad de la implicación lógica (p -> q).
    La implicación es lógicamente equivalente a (no p) o q.
    """
    return (not p) or q

def row(p, q):
    """
    Genera un diccionario que contiene los valores de verdad para una fila dada
    en una tabla de verdad, incluyendo p, q y los resultados de las operaciones lógicas.
    """
    return {
        "p": p,
        "q": q,
        "p AND q": p and q,
        "p OR q": p or q,
        "p -> q": implies(p, q),
    }

def print_table():
    """
    Imprime una tabla de verdad completa para las operaciones lógicas
    p AND q, p OR q, y p -> q.
    """
    headers = ["p", "q", "p AND q", "p OR q", "p -> q"]
    print("\t".join(headers))
    
    # Este bucle anidado genera todas las combinaciones posibles
    # para las proposiciones p y q (True/False).
    for p in [False, True]:
        for q in [False, True]:
            r = row(p, q)
            print("\t".join(str(r[h]) for h in headers))

if __name__ == "__main__":
    print_table()
