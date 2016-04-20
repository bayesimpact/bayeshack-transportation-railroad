"""Script to fix the transportation datafile."""
import os
import sys
import string
import tempfile

import pandas as pd


VALID_CHARS = set(string.punctuation + string.ascii_letters +
                  string.digits + string.whitespace)
COLUMN_RENAMES = {
    'LONGITUD': 'LONGITUDE',
    'YEAR4': 'YEAR',
    'IMO': 'MONTH',
    'NATINJ': 'INJURY_NATURE',
    'CASFATAL': 'FATAL',
    'INCDTNO': 'INCIDENT_NUM',
}
COLUMNS_TO_DROP = [
    'CAS54',
    'CAS57',
    'NARRLEN',
    # Will also drop all DUMMY columns
]


def process(infile, outfile):
    print 'Reading', infile
    with open(infile) as f:
        text = f.read()

    # First, there are some weird extraneous characters. Remove them.
    print 'Replacing strange characters'
    text = ''.join([ch for ch in text if ch in VALID_CHARS])
    # Read this into a pandas dataframe so we can do more manipulations
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(text)
    f.close()
    df = pd.DataFrame.from_csv(f.name)
    os.remove(f.name)

    print 'Renaming columns'
    df.columns = [COLUMN_RENAMES.get(c, c) for c in df.columns]
    dummies = [c for c in df.columns if c.startswith('DUMMY')]
    to_drop = list(set(COLUMNS_TO_DROP + dummies))
    print 'Dropping %d columns:\n%s' % (len(to_drop), to_drop)
    df.drop(to_drop, axis=1, inplace=True)

    print 'Fixing data'
    df['FATAL'] = df['FATAL'].apply(lambda answer: answer == 'Y').astype(bool)
    df['LATITUDE'] = df['LATITUDE'].replace(0, None)
    df['LONGITUDE'] = df['LONGITUDE'].replace(0, None)
    df['SUICIDE_ATTEMPTED'] = df['COVERDATA'] == 'X'

    # Combine narrative columns into one
    narratives = []
    for n1, n2 in zip(df['NARR1'], df['NARR2']):
        narratives.append(str(n1 if pd.notnull(n1) else '') + str(n2 if pd.notnull(n2) else ''))
    for i, n3 in enumerate(df['NARR3']):
        narratives[i] = narratives[i] + str(n3 if pd.notnull(n3) else '')
        narratives[i] = narratives[i].strip()
        if narratives[i] == '':
            narratives[i] = None
    df['NARRATIVE'] = narratives
    df.drop(['NARR1', 'NARR2', 'NARR3'], axis=1, inplace=True)

    print 'Writing to', outfile
    df.to_csv(outfile, index=False)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print '*' * 50
        print '* ERROR'
        print '* Usage: python fix_transportation.py [infile] [outfile]'
        print '*' * 50
        sys.exit(1)
    process(*sys.argv[1:])
