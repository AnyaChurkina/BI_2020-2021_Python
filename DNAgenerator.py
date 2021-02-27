from itertools import product


def generator(DNALength):
    nucleotide = ['A', 'T', 'G', 'C']
    for i in range(1, (DNALength + 1)):
        for seq in product(nucleotide, repeat=i):
            yield ''.join(seq)


print(list(generator(2)))

#  Output: "['A', 'T', 'G', 'C', 'AA', 'AT', 'AG', 'AC', 'TA', 'TT', 'TG',
#  'TC', 'GA', 'GT', 'GG', 'GC', 'CA', 'CT', 'CG', 'CC']"
