from Bio import SeqIO


def translator(path_to_fasta, table_type, outfile):
    with open(outfile, "w") as polypeptide:
        for fasta in SeqIO.parse(path_to_fasta, "fasta"):
            peptide = fasta.seq.translate(table=table_type)
            yield polypeptide.write("Polypeptide from " + fasta.id + " " +
                                    "sequence" + "\n")
            yield polypeptide.write(str(peptide) + "\n")


#  For example Escherichia coli O157:H7 str. Sakai (E. coli) fasta file
translator("/GCF_000008865.2_ASM886v2_genomic.fna", "Standard",
           "E_coli_polypeptide.fa")
