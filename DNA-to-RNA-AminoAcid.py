#A large amount of data is stored, organized, analyzed and visualized with the use of Microsoft Excel.
#This method will combine Python and Excel, allowing users to read and work with Excel files within Python to expand the data sets even more.
#Be sure the user installs Pandas explicity with pip before using this method.
#If the method still does not work then the user may have a different Python version and Pandas is not installed for the correct one.
#
### ---- DISCLAIMER: THIS METHOD HEAVILY RELIES ON THE EXCEL FILE. IF THE UNIQUE VALUE IS NOT FOUND IN THE EXCEL FILE THEN IT WILL NOT EXECUTE AND WILL FAIL THE TEST. ---- ###
#
from DNA_Nucleotide_Counter import *
from Transcription_Reverse_Compliment import *
import pandas as pd #load pandas
dnaRNA = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'} #dictionary for DNA to RNA
rnaCodons = pd.read_excel('/Users/albertseo/Desktop/RNA Codon Table.xlsx', index_col = 0, header = 0) #import the Excel spreadsheet into a pandas DataFrame. 
codonDictionary = rnaCodons.to_dict() #convert the excel file to a dictionary 
validatedSeq = userDNA.upper()

#checkpoint to see that excel worksheet is correctly formatted as a dictionary
#print(codonDictionary.keys())
#print(codonDictionary.values())

#Function that will convert DNA to RNA
def rnaSeq(seq):
    return ''.join([dnaRNA[nuc] for nuc in seq])

print("The validated DNA sequence has been transcribed to the RNA sequence: ", rnaSeq(validatedSeq))
print()

#Establish the following:
#1. defined variables that will be passed into the functions
#2. empty variables to be used for iterations
#3. an empty dictionary for replacement values to be stored
amino_acid = rnaSeq(validatedSeq)
aminoAcidSeq = []
old = codonDictionary['Abbreviation']
new = {}

#Function that replaces every "T" character with "U" so that the RNA strand can be understood in the next function
for key, value in old.items():
    new_key = key.replace("T", "U")
    new_value = value.replace("T", "U")
    new[new_key] = new_value

#Function that will convert RNA to Amino Acid
for i in range(0, len(amino_acid), 3):
    aa = amino_acid[i:i+3]
    #print(aa)
    if aa in new:
        aminoAcidSeq.append(old[aa])
    else:
        print("Test failed")

print("Your amino acid sequence is:", aminoAcidSeq)
print()
