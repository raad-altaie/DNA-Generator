import random

#Generate Random DNA Sequence

def random_dna_sequence(length):
    return ''.join(random.choice('ACTG') for each in range(length))



#DNA sequences with equal base probability

def base_frequency(dna):
    D = {}
    for base in 'ATCG':
        D[base] = dna.count(base)/float(len(dna))
    return D

for each in range(20):
    dna = random_dna_sequence(50)
    print (dna, base_frequency(dna))

    
