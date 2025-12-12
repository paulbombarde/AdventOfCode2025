import sys

def part1(map):
    movable_count=0
    for i,row in enumerate(map):
        for j,cell in enumerate(row):
            if cell != "@": continue

            nroll = -1 # to account for the current roll
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    if map[i+di][j+dj] == "@":
                        nroll += 1
            if nroll < 4:
                movable_count += 1
    return movable_count

def part2_round(map):
    movable_count=0
    for i,row in enumerate(map):
        for j,cell in enumerate(row):
            if cell != "@": continue

            nroll = -1 # to account for the current roll
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    if map[i+di][j+dj] == "@":
                        nroll += 1
            if nroll < 4:
                movable_count += 1
                map[i][j] = "x"
    return movable_count

def part2(map):
    r = 0
    n = part2_round(map)
    while n:
        r += n
        n = part2_round(map)
    return r

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    guard_line = ["*"]*(len(lines[0]) + 1)
    extended = [guard_line]
    extended.extend([["*"]+[c for c in l.strip()]+["*"] for l in lines])
    extended.append(guard_line)

    print(part1(extended))
    print(part2(extended))

