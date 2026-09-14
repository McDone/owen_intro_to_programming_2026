print("Where is the path to the DNA sequence file?")
filepath = input()
rnaseq = []
with open (filepath, "r") as dnafasta:
    for line in dnafasta:
        if line[0] != ">":
            dnaseq = line
            for base in dnaseq:
                if base not in ["A", "G", "C", "T"]:
                    print("DNA sequence contains non-DNA characters.")
            for base in dnaseq:
                if base == "T":
                    rnaseq.append("U")
                else:
                    rnaseq.append(base)
    with open("output_RNA_seq.fa", "w") as output:
        output.write(">output_RNA_seq\n" + "".join(rnaseq))
