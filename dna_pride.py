t = int(input())

for i in range(t):
    n = int(input())
    seq = input()
    pairseq = ''
    for j in range(n):
        base = seq[j]
        if base == 'T':
            pairseq += 'A'
        elif base == 'A':
            pairseq += 'T'
        elif base == 'G':
            pairseq += 'C'
        elif base == 'C':
            pairseq += 'G'
        else:
            pairseq = 'Error RNA nucleobases found!'
            break
    print(pairseq)