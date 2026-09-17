#1. Prints the sequence back to the user
#2. Builds the one-hot encoded matrix for the sequence (you have everything you need: `np.zeros()` to initialize the array, a `for` loop over the sequence's positions from Day 3, and a dictionary mapping base → column index from Day 4)
#3. Displays the matrix as a heatmap using `plt.imshow()`, with one axis as DNA position and the other as the one-hot index


#Get dna file from user 
#Get sequence from file
#Create empty matrix of zeros with shape (len(sequence), 4)
#Create a dictionary mapping bases to column indices
# Display the matrix as a heatmap -> plt.imshow(2D array, color)

import numpy as np
import matplotlib.pyplot as plt

print("Please input your DNA sequence:")
input = input()
dna_seq = input.upper()
print("Your input sequence is" + dna_seq)



basetoarray = {"A":0, "T":1, "C":2, "G":3}
array = np.zeros((len(dna_seq), 4))

for base in dna_seq:
    is_dna = True
    if base not in basetoarray.keys():
        is_dna = False
        print("not dna lol")
        break
if is_dna == True:
    for i, base in enumerate(dna_seq):
        column = basetoarray[base]
        row = i
        array[i, column] = 1

plt.imshow(array, cmap="magma")
plt.xlabel("Base (A,T,C,G)")
plt.ylabel("Presence")
plt.show()



