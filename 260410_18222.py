import sys 
from io import StringIO

sys.stdin = StringIO('''10000000000''')
N = int(sys.stdin.readline())

print(bin(N-1).count('1')%2)