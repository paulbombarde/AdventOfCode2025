import sys

def main(filename):
    split_count = 0
    paths_counts = []
    with open(filename) as f:
        lines = f.readlines()
        tachyons = [lines[0].index("S")]
        paths_counts = [1]
        for line in lines[1:]:
            #print(tachyons)
            #print(paths_counts)
            #print("----")
            next_tachyons = []
            next_paths_counts = []
            for i,t in enumerate(tachyons):
                if line[t] != "^":
                    if not len(next_tachyons) or next_tachyons[-1] != t:
                        next_tachyons.append(t)
                        next_paths_counts.append(paths_counts[i])
                    elif next_tachyons[-1] == t:
                        next_paths_counts[-1] += paths_counts[i]
                    continue
                split_count += 1
                if not len(next_tachyons) or next_tachyons[-1] != t-1:
                    next_tachyons.append(t-1)
                    next_paths_counts.append(paths_counts[i])
                elif next_tachyons[-1] == t - 1:
                    next_paths_counts[-1] += paths_counts[i]

                next_tachyons.append(t+1)
                next_paths_counts.append(paths_counts[i])
            tachyons = next_tachyons
            paths_counts = next_paths_counts
    print(split_count)
    print(sum(paths_counts))

if __name__ == '__main__':
    main(sys.argv[1])