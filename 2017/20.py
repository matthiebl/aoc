"""
--- Day 20: Particle Swarm ---
https://adventofcode.com/2017/day/20
"""

from collections import defaultdict

from utils import *

args = parse_args(year=2017, day=20)
raw = get_input(args.filename, year=2017, day=20)

particles = [tuple(nums(line)) for line in raw.splitlines()]


def displacement(s0: int, v: int, a: int, t: int = 1):
    return abs(s0 + v * t + 0.5 * a * t * t)


dists = []
for i, (x, y, z, vx, vy, vz, ax, ay, az) in enumerate(particles):
    dists.append(displacement(x, vx, ax, 10000) + displacement(y, vy, ay, 10000) + displacement(z, vz, az, 10000))
    particles[i] = (x, y, z, vx, vy, vz, ax, ay, az)
_, p1 = min((abs(d), i) for i, d in enumerate(dists))
print(p1)

p2 = len(particles)
while True:
    for _ in range(100):
        positions = []
        for i, (x, y, z, vx, vy, vz, ax, ay, az) in enumerate(particles):
            vx, vy, vz = vx + ax, vy + ay, vz + az
            x, y, z = x + vx, y + vy, z + vz
            particles[i] = (x, y, z, vx, vy, vz, ax, ay, az)
            positions.append((x, y, z))
        particles = [particle for particle in particles if positions.count(particle[:3]) == 1]
    if len(particles) == p2:
        break
    p2 = len(particles)
print(p2)

if args.test:
    args.tester(p1, p2)
