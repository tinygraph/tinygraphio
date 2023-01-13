from collections.abc import Iterable


def delta_encode(it: Iterable[int], prev: int = 0) -> Iterable[int]:
    r = []

    for v in it:
        r.append(v - prev)
        prev = v

    return r

def delta_decode(it: Iterable[int], prev: int = 0) -> Iterable[int]:
    r = []

    for v in it:
        r.append(v + prev)
        prev += v

    return r
