#Take user DNA input
#Convert a DNA sequence to RNA.
#Translate RNA to Amino Acids using the below dictionary.
#Use functions to break down the process.
#Output the Amino Acid sequence to the terminal.
#Fold the protein! Use ESMFold web version.

# RNA to AA dictionary:
genetic_code = {
    'AUG': 'M', 
    'UUU': 'F', 'UUC': 'F',
    'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y',
    'CAU': 'H', 'CAC': 'H',
    'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N',
    'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C',
    'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop'
}

dna_dict = {}
rna_dict = {}

def transcriber(user_dna_file):
    with open(user_dna_file, "r") as dna_input: #read file
        for i, line in enumerate(dna_input): 
            if line[0] != ">": #check for fasta 
                #is_fasta = False
                seq = line
                is_dna_seq = True
                for base in seq: #check if sequence is DNA only
                    if base not in ["A", "T", "G", "C"]:
                        is_dna_seq = False
                        print(f"The input sequence in {dna_input} on line {i + 1}")
                        break

                if is_dna_seq == True: #if it's dna then translate to rna
                    dna_seq = seq
                    rna_seq = dna_seq.replace("T", "U")
            else:
                #is_fasta = True
                fasta = line
            if i % 2 == 1: #check if line is even or odd
                dna_name = user_dna_file + "_dna_from_line_" + str(i + 1) #generate name of sequences for dictionary
                dna_dict[dna_name] = dna_seq # save outputs to dict before loop repeats

                rna_name = user_dna_file + "_rna_from_line_" + str(i + 1) #generate name of sequences for dictionary
                rna_dict[rna_name] = rna_seq # save outputs to dict before loop repeats

                seq_dict = {"DNA": dna_dict, "RNA": rna_dict} #combine dicts into one dict
    
    return seq_dict

def translator(transcriber_output): 
    aa_seq = ""
    for i, (rna_name, rna_seq) in enumerate(rna_dict.items()): #translate RNA to AA
        for base in rna_seq:
            if base not in ["A", "U", "G", "C"]:
                print("Invalid RNA sequence.")
                return None
        codon = rna_seq[i*3: (i*3)+3]
        if codon in genetic_code.keys():
            aa = genetic_code[codon]
            aa_seq = aa_seq + aa
        else:
            print("Could not find specified codon in genetic_code.")
            break
    aa_output = [rna_name, aa_seq]
    return aa_output

print("Please input the path to your DNA file from your current directory.")
user_dna_file = input()
print(f"Thank you! The file is here: {user_dna_file}")

transcription = transcriber(user_dna_file)
translation = translator(transcription)

with open("output.txt", "w") as output_file:
    output_file.write(f"Here's the file path: {user_dna_file}")
    output_file.write(f"Here's all saved DNA files: {transcription["DNA"]}")
    output_file.write(f"Here's all saved RNA trancriptions: {transcription["RNA"]}")
    output_file.write(f"Here's the final amino acid sequence: {translation}")

print(f"Here's the AA sequence: {translation}")
print("All done :)")
