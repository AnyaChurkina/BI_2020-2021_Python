import unittest
from DNA_RNA_classes_v1 import DNA
from DNA_RNA_classes_v1 import RNA


class TestingClassDNA(unittest.TestCase):

    def test_dna_is_dna(self):
        dna = DNA('ATGC')
        self.assertEqual(dna.sequence, 'ATGC')

    # def test_dna_not_dna(self):
    #     dna = DNA('AUGC')
    #     self.assertRaises()

    def test_dna_is_a_str(self):
        dna = DNA('ATGC')
        self.assertTrue(isinstance(dna.sequence, str), True)

    # def test_dna_not_a_str(self):
    #     dna = DNA('AT', 'GC')
    #     self.assertRaises(TypeError, isinstance(dna.sequence, str))

    def test_dna_sequence(self):
        dna = DNA('AtgC')
        self.assertTrue(dna.sequence, 'ATGC')

    def test_dna_sequence_length(self):
        dna = DNA('ATGC')
        self.assertEqual(dna.length, 4)

    def test_dna_complement(self):
        dna = DNA('ATGC')
        self.assertTrue(dna.complement, 'TACG')

    def test_gc_content(self):
        dna = DNA('ATGC')
        self.assertEqual(dna.gc_content(), 50)

    def test_gc_content_with_zero_length(self):
        dna = DNA('')
        self.assertRaises(ZeroDivisionError, dna.gc_content)

    def test_reverse_complement(self):
        dna = DNA('ATGC')
        self.assertTrue(dna.reverse_complement(), 'GCAT')

    def test_transcribe(self):
        dna = DNA('ATGC')
        self.assertTrue(dna.transcribe(), RNA('UACG'))

    def test_equal(self):
        self.assertEqual(DNA('ATGC'), DNA('ATGC'))

    def test_hash(self):
        self.assertEqual(hash(DNA('ATGC')), hash(DNA('ATGC')))

    def test_iterable(self):
        dna = DNA('ATGC')
        self.assertEqual([x for x in dna.sequence], ['A', 'T', 'G', 'C'])

class TestingClassRNA(unittest.TestCase):
    def test_rna_is_rna(self):
        rna = RNA('AUGC')
        self.assertEqual(rna.sequence, 'AUGC')

    # def test_dna_not_dna(self):
    #     dna = DNA('AUGC')
    #     self.assertRaises(TypeError, dna.dna_nucleotides)

    def test_rna_is_a_str(self):
        rna = RNA('AUGC')
        self.assertTrue(isinstance(rna.sequence, str), True)

    # def test_dna_not_a_str(self):
    #     dna = DNA('ATGC')
    #     self.assertRaises(TypeError, isinstance(dna.sequence, str))

    def test_rna_sequence_upper(self):
        rna = RNA('AugC')
        self.assertTrue(rna.sequence, 'AUGC')

    def test_rna_sequence_length(self):
        rna = RNA('AUGC')
        self.assertEqual(rna.length, 4)

    def test_rna_complement(self):
        rna = RNA('AUGC')
        self.assertTrue(rna.complement, 'UACG')

    def test_gc_content(self):
        rna = RNA('AUGC')
        self.assertEqual(rna.gc_content(), 50)

    def test_gc_content_with_zero_length(self):
        rna = RNA('')
        self.assertRaises(ZeroDivisionError, rna.gc_content)

    def test_reverse_complement(self):
        rna = RNA('AUGC')
        self.assertTrue(rna.reverse_complement(), 'GCAU')

    def test_cDNA(self):
        rna = RNA('AUGC')
        self.assertTrue(rna.cDNA(), DNA('ATGC'))

    def test_equal(self):
        self.assertTrue(RNA('AUGC'), RNA('AUGC'))

    def test_hash(self):
        self.assertEqual(hash(RNA('AUGC')), hash(RNA('AUGC')))

    def test_iterable(self):
        rna = RNA('AUGC')
        self.assertEqual([x for x in rna.sequence], ['A', 'U', 'G', 'C'])

if __name__ == '__main__':
    unittest.main()