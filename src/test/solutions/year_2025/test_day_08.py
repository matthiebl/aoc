from advent.solutions.year_2025.day_08 import DisjointSet


def test_disjoint_set_basic() -> None:
    ds = DisjointSet(5)
    assert ds.find(3) == 3
    assert ds.root_size(2) == 1
    assert ds.root_size(4) == 1
    assert ds.root_sizes() == [1, 1, 1, 1, 1]


def test_disjoint_set_union() -> None:
    ds = DisjointSet(5)
    assert ds.find(3) == 3
    assert ds.find(4) == 4
    ds.union(3, 4)
    assert ds.find(3) == ds.find(4)
    assert ds.root_size(3) == 2
    assert ds.root_size(3) == ds.root_size(4)
    sizes = ds.root_sizes()
    assert sizes.count(1) == 3
    assert sizes.count(2) == 1


def test_disjoint_set_union_all() -> None:
    ds = DisjointSet(5)
    ds.union(1, 2)
    ds.union(3, 4)
    ds.union(0, 4)
    ds.union(1, 3)
    assert ds.find(1) == ds.find(0)
    assert ds.root_size(4) == 5
    ds.root_sizes() == [5]
