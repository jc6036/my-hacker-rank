# Solve for hackerrank problem "Ceaser Cipher"

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def moveAlphabetByOne(alphabet):
    new_alphabet = []
    for i in range(1, len(alphabet)):  # Copy the rest of the array, minus the first one
        new_alphabet.append(alphabet[i])
    new_alphabet.append(alphabet[0])  # Then bring the first element to the last spot
    
    return new_alphabet
    

def caesarCipher(s, k):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l',
                'm','n','o','p','q','r','s','t','u','v','w','x',
                'y','z']
    
    ciphered_alphabet = []
    
    ciphered_alphabet = alphabet
    for i in range(k):
        ciphered_alphabet = moveAlphabetByOne(ciphered_alphabet)  # This gives us the cipher
    
    capital = False
    a_index = 0
    ciphered_string = ""
    print(s)
    for l in s:
        capital = False
        if l.isupper():
            capital = True  # Set capital flag, as we will cipher then re-capitalize
            l = l.lower()
        
        if l in alphabet:
            a_index = alphabet.index(l)
            if capital is True:
                ciphered_string = ciphered_string + ciphered_alphabet[a_index].upper()
            else:
                ciphered_string = ciphered_string + ciphered_alphabet[a_index]
        else:
            ciphered_string = ciphered_string + l
    
    return ciphered_string
                
                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
