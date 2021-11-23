import sys
for line in sys.stdin:
    line=line.strip()
    l=line.split(',')
    print('%s\t%s' % (l[6],1))
