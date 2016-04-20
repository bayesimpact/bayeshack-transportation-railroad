"""Script to downsample a csv file."""
import csv
import random
import sys


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print '*' * 50
        print '* ERROR'
        print '* Usage: python csv_sample.py [infile] [outfile] [fraction]'
        print '*' * 50
        sys.exit(1)
    infile, outfile, frac = sys.argv[1:]
    headers = None
    rows = []
    with open(infile) as f:
        reader = csv.reader(f)
        for line in reader:
            if not headers:
                headers = line
            else:
                rows.append(line)
    N = len(rows)
    size = int(round(N * float(frac)))
    rows = random.sample(rows, size)
    rows.sort()
    with open(outfile, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for r in rows:
            writer.writerow(r)
