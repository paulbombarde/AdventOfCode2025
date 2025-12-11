import sys
import unittest


def split_id(id):
    top_len = len(id)//2
    return id[:top_len], id[top_len:]

def split_ints(id):
    t, b = split_id(id)
    return int(t) if len(t) else 0, int(b)

def join_int(val):
    n = len(str(val))
    return val + pow(10, n) * val

def patterns(id):
    return patterns_from_top(id[:len(id)//2])

def patterns_from_top(top_id):
    return [top_id[:i+1] for i in range(len(top_id))]

def repeat(pattern, l):
    r = pattern
    while len(r) < l:
        r += pattern
    if len(r) == l:
        return int(r)
    raise ValueError

def part2_invalids(start, stop):
    stop_int = int(stop)



class TestSplit(unittest.TestCase):
    def test_split_17458(self):
        self.assertEqual(("17","458"), split_id("17458"))
    def test_split_174058(self):
        self.assertEqual(("174","058"), split_id("174058"))
    def test_split_107458(self):
        self.assertEqual(("107","458"), split_id("107458"))
    def test_split_16(self):
        self.assertEqual(("1","6"), split_id("16"))
    def test_split_1(self):
        self.assertEqual(("","1"), split_id("1"))
    def test_split_int_17458(self):
        self.assertEqual((17,458), split_ints("17458"))
    def test_split_int_174058(self):
        self.assertEqual((174,58), split_ints("174058"))
    def test_split_int_107458(self):
        self.assertEqual((107,458), split_ints("107458"))
    def test_split_int_16(self):
        self.assertEqual((1,6), split_ints("16"))
    def test_split_int_1(self):
        self.assertEqual((0,1), split_ints("1"))
    def test_join_0(self):
        self.assertEqual(0, join_int(0))
    def test_join_1(self):
        self.assertEqual(11, join_int(1))
    def test_join_123(self):
        self.assertEqual(123123, join_int(123))
    def test_pattern_17458(self):
        self.assertEqual(["1", "17"], patterns("17458"))
    def test_pattern_174058(self):
        self.assertEqual(["1", "17", "174"], patterns("174058"))
    def test_pattern_107458(self):
        self.assertEqual(["1", "10", "107"], patterns("107458"))
    def test_pattern_16(self):
        self.assertEqual(["1"], patterns("16"))
    def test_pattern_1(self):
        self.assertEqual([], patterns("1"))
    def test_repeat_123_6(self):
        self.assertEqual(123123, repeat("123", 6))
    def test_repeat_123_7(self):
        with self.assertRaises(ValueError):
            repeat("123", 7)
    def test_repeat_12_8(self):
        self.assertEqual(12121212, repeat("12", 8))
    def test_part2_11_12(self):
        self.assertEqual([11,22], list(part2_gen("11", "22")))
    def test_part2_95_115(self):
        self.assertEqual([99,111], list(part2_gen("95", "115")))
    def test_part2_998_1012(self):
        self.assertEqual([999, 1010], list(part2_gen('998', '1012')))
    def test_part2_1188511880_1188511890(self):
        self.assertEqual([1188511885], list(part2_gen('1188511880', '1188511890')))
    def test_part2_222220_222224(self):
        self.assertEqual([222222], list(part2_gen('222220', '222224')))
    def test_part2_1698522_1698528(self):
        self.assertEqual([], list(part2_gen('1698522', '1698528')))
    def test_part2_446443_446449(self):
        self.assertEqual([446446], list(part2_gen('446443', '446449')))
    def test_part2_38593856_38593862(self):
        self.assertEqual([38593859], list(part2_gen('38593856', '38593862')))
    def test_part2_565653_565659(self):
        self.assertEqual([565656], list(part2_gen('565653', '565659')))
    def test_part2_824824821_824824827(self):
        self.assertEqual([824824824], list(part2_gen('824824821', '824824827')))
    def test_part2_2121212118_2121212124(self):
        self.assertEqual([2121212121], list(part2_gen('2121212118', '2121212124')))

def ranges(filenames):
    ids = []
    with open(sys.argv[1]) as f:
        for line in f:
            elems = line.strip().split(',')
            for elem in elems:
                start, stop = elem.split('-')
                ids.append((start, stop))
    return ids

def part1(ranges):
    invalid_ids = []
    for start, stop in ranges:
        stop_int = int(stop)
        start_int = int(start)
        start_top, start_bottom = split_ints(start)

        id = join_int(start_top)
        while id <= stop_int:
            if start_int <= id:
                invalid_ids.append(id)
            start_top += 1
            id = join_int(start_top)
    return sum(invalid_ids)

def part2_gen(start, stop):
    start_int = int(start)
    stop_int = int(stop)
    top, start_bottom = split_ints(start)

    inc = pow(10, len(start) - len(start) // 2)
    v = top * inc
    invalid_ids = set()
    while v <= stop_int:
        patterns = patterns_from_top(str(top))
        l = len(str(v))
        for pattern in patterns:
            try:
                val = repeat(pattern, l)
                if start_int <= val and val <= stop_int:
                    if val in invalid_ids:
                        continue
                    invalid_ids.add(val)
                    yield val
            except:
                pass
        top += 1
        v += inc


def part2(ranges):
    invalid_ids = []
    for start, stop in ranges:
        for val in part2_gen(start, stop):
            invalid_ids.append(val)

    return sum(invalid_ids)

def main(filename):
    rs = ranges(filename)
    print("First:", part1(rs))
    print("Second:", part2(rs))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        unittest.main()
    else:
        main(sys.argv[1])
