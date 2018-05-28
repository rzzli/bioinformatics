def hamdist(str1, str2):
   """Count the # of differences between equal length strings str1 and str2"""
        
   diffs = 0
   for ch1, ch2 in zip(str1, str2):
                if ch1 != ch2:
                        diffs += 1
   return diffs
    


str1='CGGCACATGGTGGTCCTCAGCCTGAGTGTGCGGTTGAATTTCTAAGTCCGCCCCCGTTCAAGCTCGTTTGCCTCTTCGCCTCTCATTTTTCTCCTCATTGTTGCGGGCAGTGGCCGTGTCGCCCCTTCACAACACCACCGGGCGGTGGCTCTACATATCCGAGCCCCAGTCGGAAGTAGTGTTTTTAGTGAACAATGTCGTCGGAATCGAGCCGTCACCGGTAGCTCGTCGTAGGCAATATTCGCAGTGGTAAAAGCTATATACCATCAACGATTTAAGTGCAATTTGGTGCTCCCTGCAGACTGCGACGTCTTTGAATCCTTGCCGGGGCTGCAATTGGTCCCACAAGTGAAACGGTACCATACCAACCCGGGCGGTTTGTTGCCCTTCTAATAGGAGAAGCATCCTGATACTTGCTAACGATTGTACGTTCTTAAAAGGGATGCATTGATACTCTTAGCTCAGAATACTGGACATCGGATGAATACGGCATTTGAAACAACAGCCAACGACGGTAGTGCCTAGTGACGAGTAGTAGCGTGTCTGCTGTGCTTCTACGGGGGGGTACGTGCTGTATATTGGCCAACAACAGCAACACCTCTATTTTAAGGTTTTGAACTGTGATGTCTAAGCAACACCTCGTTAATTCTCCTGGCATGAAAACCGCAAACATAATCCACAAGGGTTGGAAAGCTTCTGTTCGGTTCCTGCTACTTTGTCGAAAATTTAAATCAGTAGAATGATCTTGAGGTATAACTGCCCATACCATGTCTGCCAGTGATGATTGAATACAAACCACAGGTGCGCGATCAAATAACCCTATCTATTCGTCTTGAGTATGGCAATATCTTGTGGGAGTTGCACGTTAAGGGCAGAACTTAGCTGCTGAAATATCTCATGCTAAGACTTCCAAGGGATCGCTTAGACATAATGATAGGTGTACTTTGCGTTATTGCGACAGACAGTTGGTGTCCAGCCCAAATGCTAGGTTTTACATTCTTGCGCGGGCACCAGTCTGTGCCTCCTCCGCTACCTATACTGCCCCCGAAAGCAGCGCCTTATCCGTAACGGTCGTGTTGCGATTAGGACTCTCAATAATTGGTGCTGCCCCCGCGCCATAATTGAGTAATCCTAGAGTGCTCCTTGTAATCACC'
str2='GTGAGAGCTCCATGAACTGCGTCTGCCAATCAGCGCCGTTAACATGTCACATACGTGGTACCAGCAGTTACAGGATAAGCTATAGTGTCCGTTCCTAGAAGTTACTATTACAGCATGTTGCAGGCCAATTTTCTCTCTTGGTCTATTGTGTTCTAGAGAGATCACGGGCCCACGGAACTATCACCAAGTTGCATGGCCGACCTCTCAACTTACGTAGCACCACTCTGGCCACATATACTAACGCCTCAAATTTCCCTCAACTCAGGCTTTGTCAAACGGTTTACGAGGGCGTTTGATTCTCAACAATTAGCTCCTGTTTTGTACTTTCGCCGTTAACACTACCCTGTTAGCAAGCTCTCGATCGCAGTGTTGAGGCAACAGTGGGGCCCTGCCAAATGCCGCACGCTTCTGAGCCCTATCACTCATTTGTAGGAACGAAATACGCGAATAGAAGGCTAATCTATAGAGCTTCGTTTAACTCCATTGTCCCATGCACCGCCGGGGTATTTCGTGTCGGCAGAAAGAGTCTCTCTCTTCAATCACTTCGCCGTGACCGCTCTGCACCTAGCTTCCTCGACGGGGGCCGCCAGCGCCGTCCTTTGCTCAATATATGATTCTCCCCGATTGATAGCGACTGTCCTTTTGCGTTGAATCCAGTAACATGAACAACCATTTTTTCGGGCGTGCCCTTGATCGCGAGCGAGCACAGGGTGGTTTACAGTCTATTACAACAAGACTGGGCCCGGGTAGATGTATGATCGAGAAAGATATCCGTGGGTCTTTAGCCAGCAGACGGTACTTTACTCACCCACCGAGAACAGCAGAGTTGTTGCAGACATGTGCTCGGAGTTGAAGTACGAGATTATAAGTGATCGGACATTGGCCTATCCAGGTATCTGGACAGCTTCGGTGCTTTCAGGGGCGCGACACTCGCCACCAGAAGCGCCCCACGAGCACAACACAATTGTAAGCTTCAGCTGCATACTCAGGAATCTCACGCGTCCGACGTCTTGATGTGAACACTATGTTTCCCACGCTCTCCAGGCCGTTTGGGTATACACGGGGTCAATATATACTACGATGTACTTGCCATGCATCATACGGGTAAAGCGTATGGCTTACAGGGTTCATCTTGTAGAGGTCGGTGCGCTGTC'
print (hamdist(str1, str2))