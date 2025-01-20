"""
--- Day 14: One-Time Pad ---
https://adventofcode.com/2016/day/14

To solve this problem, we can keep track of potential keys (ie. hashes with triples), and then keep searching all
all potential keys for their corresponding quintuple in the next 1000 hashes. This way, we do not need to search
across a 1000 long array of cached hashes for the corresponding quintuple.

However, this comes with the issue that we could find a key out of order. Take the following case:
- A one-time pad key at index 100, with its quintuple at index 1090
- A one-time pad key at index 500, with its quintuple at index 600

In this case, we will find the quintuple for key at index 500 first, but really, the key at index 100 should be
an earlier key. To correct for this, we can save the valid key indexes, and search the next 1000 hashes once we have
found 64 keys. We can then sort this in case we found any corresponding quintuple later on that should appear first.
"""

from _md5 import md5

from utils import *

args = parse_args(year=2016, day=14)
salt = get_input(args.filename, year=2016, day=14)
# salt = "abc"


def find_keys(stretch: bool = False):
    count = 0
    limit = 10 ** 9
    keys = []
    candidates = []
    i = 0
    while i < limit:
        hash = md5(f"{salt}{i}".encode()).hexdigest()
        if stretch:
            for _ in range(2016):
                hash = md5(hash.encode()).hexdigest()

        valid = []
        for n, c in candidates:
            if i <= n + 1000 and (c * 5) in hash:
                count += 1
                keys.append(n)
                if count == 64:
                    limit = i + 1000
            elif i < n + 1000:
                valid.append((n, c))
        candidates = valid

        for a, b, c in windows(hash, n=3):
            if a == b and b == c:
                candidates.append((i, a))
                break
        i += 1
    return sorted(keys)[63]


p1 = find_keys()
print(p1)

p2 = find_keys(stretch=True)
print(p2)

if args.test:
    args.tester(p1, p2)
