# DNA-Generator

Python Script to generate DNA sequences with equal base probability (ATCG)

## Example 

```
TTGCTACTGCAAGTAGCCGGCCGAGGATCGTCGTCGAATCTGGTTTCTGCATACGATCGTGTTACTAGCGGCCGCCGAGGGGGGCGGTCCGACCGAGTGC {'A': 0.16, 'G': 0.35, 'C': 0.27, 'T': 0.22}
CGTCAGTCACTCGCCCCATGTTGCAGCACTAAGCGACCACTAGTCGAGCATAGGGAAGGGATGAGGACTCCACTTAGGAATGATACAATAAAATTAGAGC {'A': 0.32, 'G': 0.25, 'C': 0.24, 'T': 0.19}
ATATGCTTCCGGAGGTGTAACGCATCCGCGGCTAGCCTTTGATTCGGCGCTGCTCCGTGCCACAACGCGGAAGAGAGGACTAATTGACATAACCGCATGA {'A': 0.24, 'G': 0.28, 'C': 0.27, 'T': 0.21}
CGGCGGGGACCAGAAGAGACACCTCGATACATCCGGAAGCATGCGCCCGGCTCAACACAAGGTGCATGAAGAATCGCTGAAATAAGCATCATTTGTTTGA {'A': 0.31, 'G': 0.27, 'C': 0.25, 'T': 0.17}
GCTGGATGGCTCGTTTGAGCAATATCTCCAAGAAGATGGGAAAGTCGCTTCTGTCGGCGGGCGCACTGGCCGTCCTCTCTTACATTTTCGGCTTTTGTCC {'A': 0.16, 'G': 0.28, 'C': 0.26, 'T': 0.3}
TAGTATGCTTCAAACAATGCGGGGCCGTCGCGTGAGTGTATTGCACCCCGAAAAGATAAGTAATAAGCCGAACCCGGGCAATATGGATTCGGTGCCCAAC {'A': 0.29, 'G': 0.27, 'C': 0.24, 'T': 0.2}
GAAGATCGTACGGTAGTTTTGAACATAGTCCACCCTAACGGAAGCAAAGCAACCGTAGACGATAGACAAACGAAGTTACTAACGACCGTGCTGTAATGCA {'A': 0.36, 'G': 0.23, 'C': 0.22, 'T': 0.19}
GGACCATCGCATTGAGCCACAGTGCCTGGCTGTCAGTTCCCCGAAGCGCCAGGAGTGGTGCGGACTGCTTTTTACACGCAGATTGGCCGGGGGAGTCATT {'A': 0.18, 'G': 0.33, 'C': 0.27, 'T': 0.22}
CGTACTCTTGAGGGCTGGTAGAGAACGTGCGACCATCTTGTAAGTACTAGCCGGAATGCGTATCTGGGTATCTCCATGTGAGAGTCACACTTTTCGCGCA {'A': 0.22, 'G': 0.28, 'C': 0.23, 'T': 0.27}
CGCCTTTTAGGTCACCACGGGATGATTCAGACCCGGCAGACTGGGAACCTGAGCGGCTCAAGTCCAACCCGCGGAGTTAAGATCTATTCTGTACTGCTAG {'A': 0.23, 'G': 0.27, 'C': 0.28, 'T': 0.22}
ACTGACGGAACGTCGTTAACCATTTGCCCGTTGTAAACTCCACTCCTCTTCCAAGGTGCTCCGATGGTACAAGGCGTTGTGCTAGATAGCCTCTGCGTCG {'A': 0.2, 'G': 0.24, 'C': 0.29, 'T': 0.27}
GGGCCGCCGCCTTAAGCAGCACCCCAAGTTAAGAGCTCGATTTAGCCTGTCGACTCTAACAAGACCCAGCACAGATGCAGGTTGAGAAGGGCTGCTTGGG {'A': 0.25, 'G': 0.29, 'C': 0.28, 'T': 0.18}
CACTTAGGGCGCTTTCTCTTCAGATTGCTCTAGGATTTAGGTGTGTCTGGGTCGTCCGCAAGGCCGGCGGCTGGGATGGACGGCGAATATGCAGAGGGTG {'A': 0.16, 'G': 0.37, 'C': 0.21, 'T': 0.26}
TTGTGGATTACGATGGTCTTGGTCTCCTCCAGCTTTCAGCTCCTTACCTAAGGGGGAGCCGGTAACTGGAATTACACCCCTACCTCAGCGAGTGTATGTC {'A': 0.19, 'G': 0.25, 'C': 0.27, 'T': 0.29}
AATATCTCGTTAGTGGTGTTTATCCTCCGCTTCATGTAGATGGTCGTATCTCTCGGCCTTAACTTTACGTCCCGTTGCGGTATTCGCCGAAAATGAATAA {'A': 0.21, 'G': 0.21, 'C': 0.23, 'T': 0.35}
ATGGAGTGACGGCGCAGGATTAATAGCCCGAGAGGTTCACCCGGACAGGCTCAGGAAGATTATTCTGTATGGGTAGGAACGCACATAAAGATCTTTATAT {'A': 0.3, 'G': 0.29, 'C': 0.18, 'T': 0.23}
ATGAAGGGTTATCCGTTGCCTGGTCTAAGGGGTTTCCCTATAAGCCAAAATTGGTTAATCTGACTACCATTAAGGAAATTTTCTTATTTTAGATTGCCTG {'A': 0.26, 'G': 0.21, 'C': 0.17, 'T': 0.36}
GAATCCGCAGTCCACTTACAGCGATCTTGAAAAACCATCTCAAACAATCACCCAGCGGGAGTATACTGACCCACCTGGCTTCTCCTGCAATCATCCTATA {'A': 0.3, 'G': 0.15, 'C': 0.33, 'T': 0.22}
TTAGTGCGACAGAGCTGCATGCTTCCTGGCGCCCGTTCACTGTGGCCTCCTCTAAACATTGGCGGTTTGACCCCTTCCTGACTACGTCACACGTGTTCTC {'A': 0.15, 'G': 0.23, 'C': 0.33, 'T': 0.29}
TAGGCGCAGAAGATAACGGTTCCGGGCTTGTGTCAGCTGCGCAACTTTGACCGGCCTAACTGTTTGCACTCCTTGCAGAGATACATATAGGCAACGATCC {'A': 0.24, 'G': 0.26, 'C': 0.26, 'T': 0.24}
```