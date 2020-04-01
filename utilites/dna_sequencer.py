def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if dna1 > dna2:
        return True
    else:
        return False

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna2 in dna1:
        return True
    else:
        return False

def is_valid_sequence(dna):    
    """(str) -> bool
        
    Return true if and only if the DNA sequence is valid (contains no character other than 'A', 'T', 'C', 'G')

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('FDD')
    False
    >>> is_valid_sequence('atcg')
    False
    >>> is_valid_sequence('ATCDD')
    False

    """
    valid = 0
    for char in dna:
        if char in "qazwsxedcrfvtgbyhnujmikolpQZWSXEDRFVBYHNUJMIKOLP":
            valid = valid + 1
    return not valid >= 1
   

def insert_sequence(dna1, dna2, index1):
    """(str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index.
    
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'

    """
    return dna1[:index1] + dna2 + dna1[index1:] 

def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement.

    >>> get_complement('A')
    'T'
    >>> get_complement('G')
    'C'
    >>> get_complement('C')
    'G'
    """
    if nucleotide == "A":
        return "T"
    elif nucleotide == "T":
        return "A"
    elif nucleotide == "G":
        return "C"
    elif nucleotide == "C":
        return "G"
    else:
        print("input error")

def get_complementary_sequence(sequence):
    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence. 

    >>> get_complementary_sequence("AT")
    "TA"
    >>> get_complementary_sequence("AG")  
    "TC"
    >>> get_complementary_sequence("TC")
    "AG"
    """
    container = ""
    for char in sequence:
        if char in "ATCG":
            container = container + get_complement(char)
    return container
        