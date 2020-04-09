def shift_left(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the left
    and shift the first item to the last position.

    Precondition: len(L) >= 1
    '''
    
    first_item = L[0]

    for i in range(1, len(L)):
        L[i - 1] = L[i]

    L[-1] = first_item      
    

def count_adjacent_repeats(s):
    ''' (str) -> int

    Return the number of occurrences of a character and
    an adjacent character being the same.

    >>> count_adjacent_repeats('abccdeffggh')
    3
    '''

    repeats = 0

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeats = repeats + 1

    return repeats

def list_sum(list1, list2):
    '''(list, list) -> list

    Returns the sum of two given lists in a new list called sumlist.
    precondition len(list1) == len(list2)

    >>> list_sum([1, 2, 3], [1, 2, 3])
    [2, 4, 6]
    '''
    sumlist = []
    for i in range(len(list1)):
        sumlist.append(list1[i] + list2[i])
    return sumlist


def str_matches(string1, string2):
    '''(str, str) -> int

    Returns the number of matching letters with same indexes in the given strings.
    Precondition len(string1) == len(string2)

    >>> str_matches('def', kef')
    2
    >>> str_matches('etk', 'kte')
    0
    '''
    num_list = 0
    
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            num_list = num_list + 1
    return num_list


def lst_matches(list1, list2):
    '''(list, list) -> int

    Returns the number of matching numbers with the same indexes in the given lists.
    Precondition len(list1) == len(list2)

    >>> lst_matches([1, 2, 3], [1, 2, 4])
    2
    >>> lst_matches([1, 2, 4, 6], [2, 3, 5, 7])
    0
    '''

    num_list = 0

    for i in range(len(list1)):
        if list1[i] == list2[i]:
            num_list = num_list + 1
    return num_list

    