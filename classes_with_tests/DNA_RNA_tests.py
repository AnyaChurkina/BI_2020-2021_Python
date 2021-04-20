import unittest
from DNA_RNA_classes_v1 import DNA
from DNA_RNA_classes_v1 import RNA


class TestingClassDNA(unittest.TestCase):

    def test_dna_is_dna(self):
        dna = DNA('ATGC')
        self.assertEqual(dna.sequence, 'ATGC')

    def test_dna_not_dna(self):
        self.assertRaises(TypeError, DNA, 'Hello world!')

    def test_dna_is_a_str(self):
        dna = DNA('ATGC')
        self.assertTrue(isinstance(dna.sequence, str))

    def test_dna_not_a_str(self):
        self.assertRaises(TypeError, DNA, ['ATGC'])

    def test_dna_sequence(self):
        dna = DNA('AtgC')
        self.assertEqual(dna.sequence, 'ATGC')

    def test_dna_sequence_length(self):
        dna = DNA('ATGC')
        self.assertEqual(dna.length, 4)

    def test_gc_content(self):
        dna = DNA('ATGC')
        self.assertEqual(dna.gc_content(), 50)

    def test_gc_content_with_zero_length(self):
        dna = DNA('')
        self.assertRaises(TypeError, dna.gc_content)

    def test_reverse_complement(self):
        dna = DNA('ATGC')
        self.assertEqual(dna.reverse_complement(), 'GCAT')

    def test_transcribe(self):
        dna = DNA('ATGC')
        self.assertEqual(dna.transcribe(), RNA('UACG'))

    def test_equal(self):
        self.assertEqual(DNA('ATGC'), DNA('ATGC'))

    def test_iterable(self):
        dna = DNA('ATGC')
        self.assertListEqual([x for x in dna.sequence], ['A', 'T', 'G', 'C'])


class TestingClassRNA(unittest.TestCase):

    def test_rna_is_dna(self):
        rna = RNA('AUGC')
        self.assertEqual(rna.sequence, 'AUGC')

    def test_rna_not_dna(self):
        self.assertRaises(TypeError, RNA, 'Hello world!')

    def test_rna_is_a_str(self):
        rna = RNA('AUGC')
        self.assertTrue(isinstance(rna.sequence, str))

    def test_rna_not_a_str(self):
        self.assertRaises(TypeError, RNA, ['AUGC'])

    def test_rna_sequence(self):
        rna = RNA('AugC')
        self.assertEqual(rna.sequence, 'AUGC')

    def test_rna_sequence_length(self):
        rna = RNA('AUGC')
        self.assertEqual(rna.length, 4)

    def test_gc_content(self):
        rna = RNA('AUGC')
        self.assertEqual(rna.gc_content(), 50)

    def test_gc_content_with_zero_length(self):
        rna = RNA('')
        self.assertRaises(TypeError, rna.gc_content)

    def test_reverse_complement(self):
        rna = RNA('AUGC')
        self.assertEqual(rna.reverse_complement(), 'GCAU')

    def test_cDNA(self):
        rna = RNA('AUGC')
        self.assertEqual(rna.cDNA(), DNA('TACG'))

    def test_equal(self):
        self.assertEqual(RNA('AUGC'), RNA('AUGC'))

    def test_iterable(self):
        rna = RNA('AUGC')
        self.assertListEqual([x for x in rna.sequence], ['A', 'U', 'G', 'C'])

if __name__ == '__main__':
    unittest.main()