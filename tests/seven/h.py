from collections import deque


def condition(this, cur):
    return this == cur


def search(gr, st, cur, f):
    if not gr:
        return None
    k = deque([(st, 0)])
    d = set([st])
    while k:
        this, forward = k.popleft()
        if f(this, cur):
            return forward
        for near in gr.get(this, []):
            if near not in d:
                k.append((near, forward + 1))
                d.add(near)
    return None