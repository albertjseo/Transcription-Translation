from DNA_Nucleotide_Counter import * #import from previous projects
from Transcription_Reverse_Compliment import * #import from previous projects

validatedSeq = userDNA.upper() #ensure that the string sequence is validated and enters the next function. 

dnaRNA = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'} #establish a dictionary for DNA-to-RNA matching

def rnaSeq(seq):
    return ''.join([dnaRNA[nuc] for nuc in seq])

print("The validated DNA sequence has been transcribed to the RNA sequence: ", rnaSeq(validatedSeq))
