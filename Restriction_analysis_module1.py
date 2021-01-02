from Bio.Restriction import *
def restriction_sites_analysis(seq1_rs_lib, seq2_rs_lib):

    rs_dictionary_seq1 = seq1_rs_lib.full()
    rs_count_seq1 = {}
    for (enzyme_name, restriction_sites) in rs_dictionary_seq1.items():
        rs_count_seq1[enzyme_name] = len(restriction_sites)

    rs_dictionary_seq2 = seq2_rs_lib.full()
    rs_count_seq2 = {}
    for (enzyme_name, restriction_sites) in rs_dictionary_seq2.items():
        rs_count_seq2[enzyme_name] = len(restriction_sites)

    non_cutting_enzymes = RestrictionBatch([])
    seq1_unique_enzymes = RestrictionBatch([])
    seq2_unique_enzymes = RestrictionBatch([])

    for enzyme_name, restriction_sites in rs_count_seq1.items():
        if (enzyme_name in rs_count_seq2 and rs_count_seq1[enzyme_name] == 0 and rs_count_seq2[enzyme_name] == 0):
            non_cutting_enzymes += enzyme_name
        if (enzyme_name in rs_count_seq2 and rs_count_seq1[enzyme_name] == 1 and rs_count_seq2[enzyme_name] == 0):
            seq1_unique_enzymes += enzyme_name
        if (enzyme_name in rs_count_seq2 and rs_count_seq1[enzyme_name] == 0 and rs_count_seq2[enzyme_name] == 1):
            seq2_unique_enzymes += enzyme_name    

    result = {}
    result["Non_cutting_enzymes"] = non_cutting_enzymes
    result["Sequence1_unique_enzymes"] = seq1_unique_enzymes
    result["Sequence2_unique_enzymes"] = seq2_unique_enzymes

    return result