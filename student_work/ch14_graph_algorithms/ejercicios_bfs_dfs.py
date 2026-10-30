from goodrich.ch14.graph import Graph

def vecinos(g, v):
    """Retorna una lista con los elementos de los vecinos de v."""
    L = []
    for e in g.incident_edges(v):
        L.append(e.opposite(v).element())
    return L


def dfs(g, v, d):
    """DFS desde v. Agrega a d cada vertice descubierto -> arista que lo descubrio.

    v ya debe estar en d antes de la llamada (normalmente d = {v: None}). No retorna nada.
    """
    for e in g.incident_edges(v):
        w = e.opposite(v)
        if w not in d:
            d[w] = e
            dfs(g, w, d)


def bfs(g, v):
    """BFS desde v. Retorna un dict vertice descubierto -> arista que lo descubrio (v -> None)."""
    d = {v: None}
    L = [v]
    while len(L) > 0:
        siguiente = []
        for u in L:
            for e in g.incident_edges(u):
                w = e.opposite(u)
                if w not in d:
                    d[w] = e
                    siguiente.append(w)
        L = siguiente
    return d


def alcanzables(g, v):
    """Retorna una lista con los elementos de los vertices alcanzables desde v (incluido v)."""
    d = bfs(g, v)
    return [w.element() for w in d]


if __name__ == "__main__":
    # tus pruebas (opcional)
    pass
