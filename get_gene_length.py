from Bio import SeqIO

def make_record_dictionary(fastafile):
    "make a dictionary containing the description : length of each gene"
    seq_records = {}
    x = 0
    for seq_record in SeqIO.parse(fastafile, "fasta"):
        seq_records.update({seq_record.description : len(seq_record.seq)})
    return seq_records

def get_gene_length(locus_tag, seq_records):
    "Returns the length of the given gene in the given dictionary."
    for description, length in seq_records.items():
        if locus_tag in description:
            break
    return length

#use the above functions like this for example
fastafile = 'sequence_features.txt'
seq_records_dictionary = make_record_dictionary(fastafile)
locus_tag = 'PA0001'
length = get_gene_length(locus_tag, seq_records_dictionary)
print(locus_tag, length)


#locus_tags = ['PA0001', 'PA0002', 'PA0003']
#for locus_tag in locus_tags:
#    length = get_gene_length(locus_tag, seq_records_dictionary)

