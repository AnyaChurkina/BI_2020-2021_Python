"""
DNA and RNA classes with general Sequence class
"""


class Sequence:

    def __init__(self, sequence):
        if isinstance(sequence, str):
            self.sequence = sequence.upper()
            self.length = len(sequence)
            self._index = 0
            self.complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        else:
            raise TypeError('Sequence should be type string')

    def __eq__(self, other):
        if self.sequence == other.sequence:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.sequence)

    def __next__(self):
        if self._index < self.length - 1:
            self._index += 1
            return self.sequence[self._index - 1]
        else:
            raise StopIteration

    def gc_content(self):
        g_count = self.sequence.count('G')
        c_count = self.sequence.count('C')
        return (g_count + c_count) / self.length


class DNA(Sequence):
    dna_nucleotides = {'A', 'T', 'G', 'C'}

    def __init__(self, sequence):
        if set(sequence.upper()) <= self.dna_nucleotides:
            super().__init__(sequence)
        else:
            raise TypeError('Incorrect DNA sequence')

    def reverse_complement(self):
        return "".join(self.complement.get(base, base) for base in
                       reversed(self.sequence))

    def transcribe(self):
        return RNA("".join(self.complement.get(base, base) for base in
                           self.sequence).replace('T', 'U'))


class RNA(Sequence):
    rna_nucleotides = {'A', 'U', 'G', 'C'}

    def __init__(self, sequence):
        if set(sequence.upper()) <= self.rna_nucleotides:
            super().__init__(sequence)
        else:
            raise TypeError('Incorrect RNA sequence')

    def reverse_complement(self):
        return "".join(self.complement.get(base, base) for base in
                       reversed(self.sequence.replace('U', 'T'))).replace('T',
                                                                          'U')

    def cDNA(self):
        return DNA("".join(self.complement.get(base, base) for base in
                           self.sequence).replace('U', 'T'))


if __name__ == '__main__':
    dna_seq = DNA('AGTAGTATGCTACGAGGC')
    rna_seq = RNA('AGUCGAGAGUAUGCUACGAGGC')
    other_seq = DNA('AGTAGTATCTACGAGGC')

    # DNA tests
    print(dna_seq.sequence)  # print DNA sequence
    print(dna_seq.length)  # print DNA sequence length
    print(dna_seq == other_seq)  # Sequences comparison
    print(hash(dna_seq))

    cnt = 1
    while cnt <= 5:
        print(next(dna_seq))  # print first 5 nucleotides from DNA sequence
        cnt += 1

    print(dna_seq.gc_content())  # GC content of DNA sequence
    print(dna_seq.reverse_complement())  # DNA sequence reverse complement
    print(dna_seq.transcribe().sequence)  # Transcribe DNA to RNA

    # RNA tests
    print(rna_seq.sequence)  # print sequence
    print(rna_seq.length)  # print sequence length
    print(rna_seq == other_seq)  # Sequences comparison
    print(hash(rna_seq))

    cnt = 1
    while cnt <= 5:
        print(next(rna_seq))  # print first 5 nucleotides from RNA sequence
        cnt += 1

    print(rna_seq.gc_content())  # GC content of RNA sequence
    print(rna_seq.reverse_complement())  # RNA sequence reverse complement
    print(rna_seq.cDNA().sequence)  # Reverse transcription to cDNA
