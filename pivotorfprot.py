import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])

df = df.pivot_table('proportion', ['species'], 'amino acid')

df = df.groupby(['species'])['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y'].mean()

df.to_csv(sys.argv[2])
