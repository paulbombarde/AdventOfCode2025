import sys
import unittest

def part1(bank):
    return generic(bank, 2)

def part2(bank):
    return generic(bank, 12)

def generic(bank, N):
    topi = 0
    res = 0
    for n in range(N):
        res *= 10

        top = 0
        start = topi
        stop = len(bank) - N + n
        for i in range(start, stop+1):
            ii = int(bank[i])
            if top < ii:
                top = ii
                topi = i

        topi += 1
        res += top
    return res

class TestDay3(unittest.TestCase):
    def test_part1_987654321111111(self):
        self.assertEqual(98, part1("987654321111111"))
    def test_part1_811111111111119(self):
        self.assertEqual(89, part1("811111111111119"))
    def test_part1_234234234234278(self):
        self.assertEqual(78, part1("234234234234278"))
    def test_part1_818181911112111(self):
        self.assertEqual(92, part1("818181911112111"))
    def test_part2_987654321111111(self):
        self.assertEqual(987654321111, part2("987654321111111"))
    def test_part2_811111111111119(self):
        self.assertEqual(811111111119, part2("811111111111119"))
    def test_part2_234234234234278(self):
        self.assertEqual(434234234278, part2("234234234234278"))
    def test_part2_818181911112111(self):
        self.assertEqual(888911112111, part2("818181911112111"))

def main(filename):
    res1 = 0
    res2 = 0
    with open(filename) as f:
        for line in f:
            res1 += part1(line.strip())
            res2 += part2(line.strip())
    print(res1)
    print(res2)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        unittest.main()
    else:
        main(sys.argv[1])