import sys
from math import prod

def part1(filename):
    with open(filename) as f:
        splitted = []
        for line in f:
            splitted.append([c for c in line.strip().split(" ") if len(c)])

        ops = splitted[-1]
        splitted = splitted[:-1]
        res = []
        for i,op in enumerate(ops):
            if op == "+":
                res.append(sum(int(s[i]) for s in splitted))
            else:
                res.append(prod(int(s[i]) for s in splitted))

        print(sum(res))

def part2(filename):
    with open(filename) as f:
        lines = [line[:-1] for line in f]
        ops_pos = []
        for i,c in enumerate(lines[-1]):
            if c == " ": continue
            ops_pos.append(i)
        ops_pos.append(len(lines[-1])+1)
        ops = lines[-1]
        lines = lines[:-1]

        res = []
        for i in range(len(ops_pos)-1):
            start = ops_pos[i]
            stop = ops_pos[i+1]-1

            vals = []
            for j in range(start,stop):
                v = 0
                for l in lines:
                    if l[j] == " ": continue
                    v*=10
                    v+=int(l[j])
                vals.append(v)

            op = ops[start]
            #print(i, op, vals)
            if op == "+":
                res.append(sum(vals))
            else:
                res.append(prod(vals))

        print(sum(res))

if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])
