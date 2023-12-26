# Advent of Code 2023

My solutions for [Advent of Code 2023](https://adventofcode.com/2023)

## Personal Times

| Day | Part 1   | Rank  | Score | Part 2   | Rank  | Score | Notes
| --- | -------- | ----- | ----- | -------- | ----- | ----- | ----
| 1   | 00:03:30 | 1008  | 0     | 00:07:22 | 123   | 0     | Happy w/ p2
| 2   | 00:06:47 | 471   | 0     | 00:08:58 | 354   | 0     | 
| 3   | 00:21:58 | 1781  | 0     | 00:25:14 | 958   | 0     | At least I got p2 under 1000 :/
| 4   | 01:33:12 | 17542 | 0     | 01:52:28 | 13949 | 0     | Couldn't start until 1:25 after start so took my time
| 5   | 00:20:15 | 1370  | 0     | >24h     | 45104 | 0     | Had to stop p2 to study for exam, since it was too hard
| 6   | 02:05:16 | 17596 | 0     | 02:13:55 | 17051 | 0     | Did on train home after said exam
| 7   | 00:34:28 | 3239  | 0     | 01:23:39 | 5798  | 0     | Not my fav kind of puzzle, and working at same time
| 8   | 00:10:52 | 2641  | 0     | 00:27:40 | 1442  | 0     | Camping with only mobile data, made it difficult
| 9   | 00:16:19 | 2988  | 0     | 00:20:42 | 2728  | 0     | Same again
| 10  | 00:13:31 | 186   | 0     | 05:33:24 | 7198  | 0     | Struggled w/ p2
| 11  | 01:12:30 | 7827  | 0     | 01:24:55 | 6868  | 0     | Was working :/
| 12  | 00:33:53 | 2232  | 0     | 01:29:03 | 1658  | 0     | 
| 13  | 00:21:24 | 1240  | 0     | 00:43:02 | 1780  | 0     | 
| 14  | 00:11:36 | 1475  | 0     | 00:49:51 | 1784  | 0     | 
| 15  | 00:04:00 | 742   | 0     | 00:20:33 | 959   | 0     | 
| 16  | 00:28:53 | 1480  | 0     | 00:36:47 | 1405  | 0     | 
| 17  | 08:32:36 | 7981  | 0     | 08:38:41 | 6983  | 0     | Got stuck on caching
| 18  | 00:22:49 | 979   | 0     | 18:29:27 | 14451 | 0     | Had no idea about any existing algos
| 19  | 00:25:25 | 1204  | 0     | >24h     | 17057 | 0     | Took me way too long to work out 4D intersections
| 20  | 00:54:58 | 1306  | 0     | >24h     | 15696 | 0     | 
| 21  | 00:12:31 | 1133  | 0     | >24h     | 11749 | 0     |
| 22  | 23:46:52 | 11315 | 0     | >24h     | 13029 | 0     | Just Christmas things
| 23  | 00:11:21 | 189   | 0     | >24h     | 9732  | 0     | ^
| 24  | 00:33:14 | 576   | 0     | >24h     | 6822  | 0     | ^
| 25  | 04:28:47 | 3968  | 0     | >24h     | 6685  | 0     | ^, and all hard

## Asides

This year so far has been a nice twist on how I remember previous years. A lot of the puzzles involve
trying to calculate a number of things that is far too large to brute force. This makes the challenge
less about just doing something, but instead coming up with a smart way to do it efficiently.

Very glad day 17 wasn't just, "hey, we messed up, the heat map is actually 10 times larger in width and height, try again..."

Ah boy day 21 was exactly what I said about day 17... except infinite

Those last 6 or so days got difficult for part 2. I thoroughly enjoyed this year though, and it ended up
being a great learning experience.

I often prefer problems that don't require knowledge of complex algorithms, since these often end up
just requiring an imported library to do anything efficiently.
Having to use `sympy` for day 24, and `networkx` for day 25 made them feel a little less rewarding.
Learning these libraries is definitely beneficial but feels cheap.

## Tests

I made a test runner that ensures all of my results stay accurate throughout any refactors.

Cool enough, every day solves correcly in under 30 seconds!
