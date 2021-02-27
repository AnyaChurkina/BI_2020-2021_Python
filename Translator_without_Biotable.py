from Bio import SeqIO


def translate(seq):
    table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
        'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W',
    }
    protein = ""
    for i in range(0, len(seq), 3):
        codon = seq[i:i + 3]
        protein += table[codon]
    return protein


def translator(path_to_fasta, outfile):
    with open(outfile, "w") as polypeptide:
        for fasta in SeqIO.parse(path_to_fasta, "fasta"):
            if len(fasta.seq) % 3 == 0:
                peptide = translate(fasta.seq)
                polypeptide.write("Polypeptide from " + fasta.id + " "
                                  "sequence" + "\n")
                polypeptide.write(str(peptide) + "\n")
            else:
                print("Length of sequence not a multiple of three, the last "
                      "triplet not a whole triplet will not be counted.")
                fasta.seq = fasta.seq[0:(len(fasta.seq) // 3 * 3)]
                peptide = translate(fasta.seq)
                polypeptide.write("Polypeptide from " + fasta.id + " "
                                  "sequence" + "\n")
                polypeptide.write(str(peptide) + "\n")


#  For example Escherichia coli O157:H7 str. Sakai (E. coli) fasta file
translator("/GCF_000008865.2_ASM886v2_genomic.fna", "E_coli_polypeptide.fa")
