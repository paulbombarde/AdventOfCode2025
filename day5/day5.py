import sys
import unittest

def main(filename):
    parse_ids = False
    ids = []
    ranges = []

    with open(filename) as f:
        for line in f:
            line = line.strip()

            if line == "":
                parse_ids = True
                continue

            if parse_ids:
                ids.append(int(line))
            else:
                start, stop = line.split("-")
                ranges.append((int(start), int(stop)))

    ids = sorted(ids)
    raw_ranges = sorted(ranges, key=lambda x: x[0])

    ranges = []
    ri = 0
    while ri < len(raw_ranges):
        start = raw_ranges[ri][0]
        stop = raw_ranges[ri][1]
        while ri < len(raw_ranges) and raw_ranges[ri][0] <= stop:
            stop = max(raw_ranges[ri][1], stop)
            ri += 1
        ranges.append((start, stop))

    spoiled = []
    fresh = []

    ri = 0
    for id in ids:
        while ri < len(ranges) and ranges[ri][1] < id:
            ri += 1

        if ri == len(ranges) or id < ranges[ri][0]:
            spoiled.append(id)
            continue

        if id <= ranges[ri][1]:
            fresh.append(id)
            continue

    print(len(fresh))
    print(sum(stop - start + 1 for start, stop in ranges))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        unittest.main()
    else:
        main(sys.argv[1])