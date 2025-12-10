from sys import argv
import unittest

from sphinx.builders.html import return_codes_re


class First:
    def __init__(self):
        self.current = 50
        self.password = 0

    def update(self, delta):
        self.current += delta
        self.current %= 100
        if self.current < 0: self.current += 100
        if self.current == 0: self.password += 1

class Second:
    def __init__(self, current=50, password=0):
        self.current = current
        self.password = password

    def update(self, delta):
        if delta > 0:
            self.current += delta
            self.password += self.current // 100
            self.current %= 100
        elif delta < 0:
            # ugly as hell. I couldn't wrap my head around a better solution :(
            prev0 = not self.current
            while delta <= -100:
                self.password += 1
                delta += 100
            self.current += delta
            if delta and self.current == 0:
                self.password += 1
            elif self.current < 0:
                self.current += 100
                if not prev0: self.password += 1

        return self.current, self.password

class TestSecond(unittest.TestCase):
    def test_add_12(self):
        self.assertEqual((62,0), Second().update(12))
    def test_stop_0(self):
        self.assertEqual((0,1), Second().update(-50))
    def test_stop_100(self):
        self.assertEqual((0,1), Second().update(50))
    def test_add_start_0(self):
        self.assertEqual((50,0), Second(0).update(50))
    def test_one_turn_up(self):
        self.assertEqual((50,1), Second(0).update(150))
    def test_one_turn_up_stops_0(self):
        self.assertEqual((0,2), Second().update(150))
    def test_two_turns_up_stops_0(self):
        self.assertEqual((0,2), Second(0).update(200))
    def test_two_turns_up(self):
        self.assertEqual((8,2), Second(8).update(200))
    def test_two_turns_up_and_a_little(self):
        self.assertEqual((10,2), Second(8).update(202))
    def test_two_turns_up_and_a_lot(self):
        self.assertEqual((2,3), Second(8).update(294))
    def test_minus_a_little(self):
        self.assertEqual((40,0), Second().update(-10))
    def test_minus_a_lot(self):
        self.assertEqual((90,1), Second().update(-60))
    def test_one_turn_down(self):
        self.assertEqual((50,1), Second().update(-100))
    def test_one_turn_down_start_0(self):
        self.assertEqual((0,1), Second(0).update(-100))
    def test_one_turn_down_and_a_bit(self):
        self.assertEqual((95,1), Second(0).update(-105))

def main():
    first = First()
    second = Second()

    with open(argv[1], 'r') as f:
        for line in f:
            if not line:
                continue
            delta = int(line[1:])
            if line[0] == "L":
                delta = -delta

            first.update(delta)
            second.update(delta)

    print("first:", first.password)
    print("second:", second.password)

if __name__ == '__main__':
    if len(argv) == 1:
        unittest.main()
    else:
        main()
