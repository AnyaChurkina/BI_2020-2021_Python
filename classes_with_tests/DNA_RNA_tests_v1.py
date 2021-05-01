import unittest
from DNA_RNA_classes_v1 import DNA, RNA


class TestingClassDNA(unittest.TestCase):
    
    def test_dna_type(self):
        dna = DNA('ATGC')
        self.assertTrue(type(dna), DNA)

    def test_dna_is_a_str(self):
        dna = DNA('ATGC')
        self.assertTrue(isinstance(dna.sequence, str))

    def test_dna_not_a_str(self):
        self.assertRaises(TypeError, DNA, ['ATGC'])

    def test_dna_nucleotides(self):
        dna = DNA('ATGC')
        self.assertEqual(dna.sequence, 'ATGC')

    def test_not_dna_nucleotides(self):
        self.assertRaises(TypeError, DNA, 'Hello world!')

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

    def test_transcribe_class(self):
        dna = DNA('ATGC')
        self.assertTrue(type(dna.transcribe()), RNA)

    def test_equal(self):
        self.assertEqual(DNA('ATGC'), DNA('ATGC'))

    def test_not_equal(self):
        self.assertNotEqual(DNA('ATGC'), DNA('ATTTTTTGC'))

    def test_hash(self):
        dna = DNA('ATGC')
        other_dna = DNA('ATGC')
        self.assertEqual(hash(dna), hash(other_dna))

    def test_iterable(self):
        dna = DNA('ATGC')
        self.assertListEqual([x for x in dna.sequence], ['A', 'T', 'G', 'C'])


class TestingClassRNA(unittest.TestCase):

    def test_rna_type(self):
        rna = RNA('AUGC')
        self.assertTrue(type(rna), RNA)

    def test_rna_is_a_str(self):
        rna = RNA('AUGC')
        self.assertTrue(isinstance(rna.sequence, str))

    def test_rna_not_a_str(self):
        rna = RNA('AUGC')
        self.assertRaises(TypeError, rna, ['AUGC'])

    def test_rna_nucleotides(self):
        rna = RNA('AUGC')
        self.assertEqual(rna.sequence, 'AUGC')

    def test_not_rna_nucleotides(self):
        self.assertRaises(TypeError, RNA, 'Hello world!')

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

    def test_cDNA_class(self):
        rna = RNA('AUGC')
        self.assertEqual(type(rna.cDNA()), DNA)

    def test_equal(self):
        self.assertEqual(RNA('AUGC'), RNA('AUGC'))

    def test_not_equal(self):
        self.assertNotEqual(RNA('AUGC'), RNA('AUUUUUUUGC'))

    def test_hash(self):
        rna = RNA('AUGC')
        other_rna = RNA('AUGC')
        self.assertEqual(hash(rna), hash(other_rna))

    def test_iterable(self):
        rna = RNA('AUGC')
        self.assertListEqual([x for x in rna.sequence], ['A', 'U', 'G', 'C'])


if __name__ == '__main__':
    unittest.main()
