
end_file = ""

f = open(r"NCBI\organisms\JRGG01.wd.fasta", "r")
for line in f:
    if '>' not in line:
        end_file += line


f = open(r"NCBI\organisms\NZ_AHWC00000000_corr.wd.fasta", "w")
f.write(end_file)