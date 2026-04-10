import sys
from io import StringIO

sys.stdin = StringIO('''4
AH
ABAHC
AHDFG
DFGAH''')

R = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(R)]


def slimp(s,i):
    if i >= len(s):
        return None 
    
    if s[i] == 'A':
        if i+1 < len(s) and s[i+1] == 'H':
            return i+2

        if  i+1 < len(s) and s[i+1] == 'B':
            idx = slimp(s, i+2)
            if idx is not None and idx < len(s) and s[idx] == 'C':
                return idx + 1
            else:
                return None
        else:
            idx = slump(s, i+1)
            if idx is not None and idx < len(s) and s[idx] == 'C':
                return idx + 1
            else:
                return None
                
def slump(s, i):

    if i >= len(s):
        return None
    
    if s[i] == 'D' or s[i] == 'E':
        if i+1 < len(s) and s[i+1] == 'F':
            j = i+1

            while j < len(s) and s[j] == 'F':
                j+=1
            
            if j < len(s) and s[j] == 'G':
                return j+1
            else:
                return slump(s, j)
print('SLURPYS OUTPUT')
for word in words:
    idx = slimp(word, 0)
    if idx is not None:
        idx = slump(word, idx)

    if idx == len(word):
        print('YES')
    else:
        print('NO')

print('END OF OUTPUT')