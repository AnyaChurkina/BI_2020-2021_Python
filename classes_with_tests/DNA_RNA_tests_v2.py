import unittest
from DNA_RNA_classes_v2 import DNA, RNA, Sequence


class TestingClassDNA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dna = DNA('ATGC')
        cls.strange_dna = DNA('AtGcAtGcAa')
        cls.other_dna = DNA('ATGC')
        cls.zero_dna = DNA('')

    def test_dna_type(self):
        self.assertTrue(type(self.dna), DNA)

    def test_dna_is_a_str(self):
        self.assertTrue(isinstance(self.dna.sequence, str))

    def test_dna_not_a_str(self):
        self.assertRaises(TypeError, self.dna, ['ATGC'])

    def test_dna_nucleotides(self):
        self.assertTrue(self.dna.sequence, 'ATGC')
        self.assertTrue(self.strange_dna.sequence, 'ATGCATGCAA')

    def test_not_dna_nucleotides(self):
        self.assertRaises(TypeError, DNA, 'Hello world!')

    def test_dna_is_a_sequence(self):
        self.assertTrue(issubclass(type(self.dna), Sequence))

    def test_dna_sequence(self):
        self.assertEqual(self.strange_dna.sequence, 'ATGCATGCAA')

    def test_dna_sequence_length(self):
        self.assertEqual(self.dna.length, 4)
        self.assertEqual(self.strange_dna.length, 10)

    def test_gc_content(self):
        self.assertEqual(self.dna.gc_content(), 50)
        self.assertEqual(self.strange_dna.gc_content(), 40)

    def test_gc_content_with_zero_length(self):
        self.assertRaises(TypeError, self.zero_dna.gc_content)

    def test_reverse_complement(self):
        self.assertEqual(self.dna.reverse_complement(), 'GCAT')
        self.assertEqual(self.strange_dna.reverse_complement(), 'TTGCATGCAT')

    def test_transcribe(self):
        self.assertEqual(self.dna.transcribe(), RNA('UACG'))
        self.assertEqual(self.strange_dna.transcribe(), RNA('UACGUACGUU'))

    def test_transcribe_class(self):
        self.assertTrue(type(self.dna.transcribe()), RNA)

    def test_equal(self):
        self.assertEqual(self.dna, self.other_dna)

    def test_not_equal(self):
        self.assertNotEqual(self.dna, self.strange_dna)

    def test_hash(self):
        self.assertEqual(self.dna, self.other_dna)

    def test_iterable(self):
        self.assertListEqual([x for x in self.dna.sequence],
                             ['A', 'T', 'G', 'C'])
        self.assertListEqual([x for x in self.strange_dna.sequence],
                             ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'C', 'A', 'A'])

class TestingClassRNA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rna = RNA('AUGC')
        cls.strange_rna = RNA('AuGcAuGcAa')
        cls.other_rna = RNA('AUGC')
        cls.zero_rna = RNA('')

    def test_rna_type(self):
        self.assertTrue(type(self.rna), RNA)

    def test_rna_is_rna(self):
        self.assertTrue(self.rna.sequence, 'AUGC')

    def test_rna_not_rna(self):
        self.assertRaises(TypeError, DNA, 'Hello world!')

    def test_rna_is_a_str(self):
        self.assertTrue(isinstance(self.rna.sequence, str))

    def test_rna_not_a_str(self):
        self.assertRaises(TypeError, self.rna, ['AUGC'])

    def test_rna_is_a_sequence(self):
        self.assertTrue(issubclass(type(self.rna), Sequence))

    def test_rna_sequence(self):
        self.assertEqual(self.strange_rna.sequence, 'AUGCAUGCAA')

    def test_rna_sequence_length(self):
        self.assertEqual(self.rna.length, 4)
        self.assertEqual(self.strange_rna.length, 10)

    def test_gc_content(self):
        self.assertEqual(self.rna.gc_content(), 50)
        self.assertEqual(self.strange_rna.gc_content(), 40)

    def test_gc_content_with_zero_length(self):
        self.assertRaises(TypeError, self.zero_rna.gc_content)

    def test_reverse_complement(self):
        self.assertEqual(self.rna.reverse_complement(), 'GCAU')
        self.assertEqual(self.strange_rna.reverse_complement(), 'UUGCAUGCAU')

    def test_cDNA(self):
        self.assertEqual(self.rna.cDNA(), DNA('TACG'))
        self.assertEqual(self.strange_rna.cDNA(), DNA('TACGTACGTT'))

    def test_cDNA_class(self):
        self.assertEqual(type(self.rna.cDNA()), DNA)

    def test_equal(self):
        self.assertEqual(self.rna, self.other_rna)

    def test_not_equal(self):
        self.assertNotEqual(self.rna, self.strange_rna)

    def test_hash(self):
        self.assertEqual(hash(self.rna), hash(self.other_rna))

    def test_iterable(self):
        self.assertListEqual([x for x in self.rna.sequence],
                             ['A', 'U', 'G', 'C'])
        self.assertListEqual([x for x in self.strange_rna.sequence],
                             ['A', 'U', 'G', 'C', 'A', 'U', 'G', 'C', 'A', 'A'])


if __name__ == '__main__':
    unittest.main()
