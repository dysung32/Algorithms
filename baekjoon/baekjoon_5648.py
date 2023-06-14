import sys
input = sys.stdin.readline

first_input = list(map(int, input().split()))
n, atoms = int(first_input[0]), first_input[1:]

while len(atoms) < n:
    new_atoms = list(map(int, input().split()))
    atoms.extend(new_atoms)

reversed_atoms = []
for atom in atoms:
    reversed_atoms.append(int(str(atom)[::-1].lstrip('0')))

reversed_atoms.sort()

for a in reversed_atoms:
    print(a)