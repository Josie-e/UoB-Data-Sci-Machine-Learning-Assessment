# Determining Available Restriction Enzyme Recognition Sites for Molecular Cloning:

## Introduction
This pipeline is written Python3. When two DNA sequences are input as fasta files (or optionally as sequence strings) the output is a print of three lists: one list is the restriction enzymes which do not cut in either sequences. The other two lists are restriction enzymes which are unique cutters to only one of the two sequences.

## Getting Started
Download all Python scripts in this repository along with the example fasta files.

### Prerequisites
1. Requires Python3 and JupyterNotebook both available via the Anaconda Navigator package (https://www.anaconda.com/products/individual) or available separately
2. Requires Biopython to be installed (code to do this available in annotation of 'Unique and non-cutting restriction site analysis.ipynb' file).

## How To Run Sample Data
1. Ensure DNA files 'addgene_pUC19.fasta' and 'dCas9.fasta' are available in the same directory as the coding files.
2. Open 'Unique and non-cutting restriction site analysis.ipynb' Jupyter notebook file.
3. Run the first cell which: imports the required packages, reads in the DNA files, and analyses the restriction enzyme recognition sites. (This example is currently set to search with the New England Biolabs restriction enzymes list as default.)
4. The purpose of this first cell is to assign a Bio.Restriction.Restriction.Analysis object for each DNA sequence which contains, amongst other things, the positions of (or lack thereof) all restriction enzymes recognition sites searched in the DNA sequence.
5. Run the second cell. This imports the Restriction_analysis_module1.txt module and uses the function within this module that counts the the number of recognition sites for each restriction enzyme. Restriction enzymes that are not in either sequence or cut only once in one sequence and not the other are filtered to respective RestrictionBatches.
6. Run the third cell. This prints the RestrictionBatches created by the previous cell as alphabetised lists of all the restriction enzyme names contained therein.

*Example output:*

Non_cutting_enzymes: AfeI, AflII, AgeI, ApaI, AscI, AsiSI, AvrII, BaeI, BbvCI, BglII, BseRI, BsiWI, BspDI, BspEI, BsrGI, BssHII, BstEII, BstXI, Bsu36I, BtgZI, ClaI, CspCI, DraIII, EagI, EcoNI, FseI, HpaI, MscI, NaeI, NgoMIV, NotI, NsiI, PacI, PaeR7I, PflFI, PflMI, PmeI, PpuMI, PspOMI, PspXI, RsrII, SacII, SexAI, SfiI, SgrAI, SnaBI, SpeI, SrfI, StuI, Tth111I, XcmI, XhoI

Sequence1_unique_enzymes: AatII, AhdI, AlwNI, AvaI, BsaI, BseYI, BsoBI, BspQI, BsrFI, EcoO109I, KasI, NarI, NmeAIII, PluTI, PstI, SalI, SapI, SbfI, SfoI, SmaI, TspMI, XbaI, XmaI, ZraI

Sequence2_unique_enzymes: AleI, BmgBI, BmtI, BsgI, BsmFI, BsmI, BstBI, BstZ17I, BtgI, MluI, NcoI, NheI, NruI, PmlI, SwaI


## Custom usage:
To run on your own DNA sequences edit the filepaths from the sample data filepath to desired input DNA sequence fasta file filepath.

## Optional customisation in 'Unique and non-cutting restriction site analysis.ipynb':
1. DNA sequences, in the form of a string of 'A', 'G', 'C', 'T' characters, can be manually entered by replacing "sequence1 = SeqIO.read("filepath", "fasta")" with "seqeunce1 = Seq("{Paste sequence here}")". This also required the .seq to be removed from the sequence1.seq and sequence2.seq Analysis arguments at the end of the first cell.
2. The list of restriction enzyme recognition sites (the restriction batch) used when analysing the DNA sequence can be altered via two means:
    - Other supplier lists can be changed/added to the 'restriction_search_database' by using other supplier codes in the 'suppliers' argument of the 'RestrictionBatch' function. 
        - E.g.: C = Minotech Biotechnology; B = Life Technologies; E = Agilent Technologies; I = SibEnzyme Ltd.; K = Takara Bio Inc.; J = Nippon Gene Co., Ltd.; M = Roche Applied Science; O = Toyobo Biochemicals; N = New England Biolabs; Q = Molecular Biology Resources - CHIMERx; S = Sigma Chemical Corporation; R = Promega Corporation; V = Vivantis Technologies; Y = SinaClon BioScience Co.; X = EURx Ltd.
    - Within the 'Analysis' function the restriction batch argument can be changed from the custom 'restriction_search_database' to either 'AllEnzymes' or 'CommOnly' to search for either all available restriction enzyme recognition sites or all commercially avialable restriction enzymes respectively.
3. DNA sequences can either be set at linear (linear = True) or circular (linear = False) in the Analysis function at the end of the first cell.

## Summary of the 'restriction_sites_analysis' Function:
- Input: two Bio.Restriction.Restriction.Analysis objects, one for each DNA sequence.
- Output: a dictionary containing 3 RestrictionBatch objects: 
    - "Non_cutting_enzymes": containing the restriction enzymes that cut neither sequence, 
    - "Sequence1_unique_enzymes": containing the restriction enzymes that only cut uniquely in sequence 1, 
    - "Sequence2_unique_enzymes": containing restriction enzymes that only cut uniquely in sequence 2.

Author:
Josie Elliott


Acknowledgments
BioPython Tutorial and Cookbook: http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec11
and specifically the restriction enzymes section: http://biopython.org/DIST/docs/cookbook/Restriction.html