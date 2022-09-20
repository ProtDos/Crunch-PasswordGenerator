import argparse
import os
import sys
import re 
import random
import string

special_all = "§€%&/()='#—ˋ´…@;:,.-+*|_}?{!]~[^\•–≠¿>¥<£¡$"
special_normal = "$€%&/():;@!?.,-_"
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits

al = special_all + lower + upper + digits

V = string.digits
C = string.ascii_lowercase
U = string.ascii_uppercase
S = "@;:,.!?-_#+*()%&$€%"

pattern = []

def generate(arr, i, s, len):
    if(i == 0):
        print(s)
        return
    for j in range(0, len):
        appended = s + arr[j]
        generate(arr, i - 1, appended, len)
    return

def generate_num(mi, ma, output=None, characters=None):
    if characters == None:
        for i in range(mi, ma+1):
            generate(list(al), i, "", len(list(al))) 
    else:
        for i in range(mi, ma+1):
            generate(list(characters), i, "", len(list(characters)))

def fill_position(position, length, partial):
    if position == length - 1:
        for character in pattern[position]:
            print("%s%s" % (partial, character))
    else:
        for character in pattern[position]:
            fill_position(position+1, length, partial+character)

def generate_pattern(pat, output=None):
    global pattern
    pat = list(pat)
    pattern = []
    for item in pat:
        if item == "%":
            pattern.append(V)
        elif item == "@":
            pattern.append(C)
        elif item == ",":
            pattern.append(U)
        elif item == "^":
            pattern.append(S)
        else:
            pattern.append(item)
    length = len(pattern)

    fill_position(0, length, "")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced Password Generatoe")
    parser.add_argument("-min", "--minimum", help="Minimum character amount.")
    parser.add_argument("-max", "--maximum", help="Maximum character amount.")
    parser.add_argument("-t", "--pattern", help="Define a specific pattern.")
    parser.add_argument("-c", "--characters", help="Charscters to use to generate output.")
    parser.add_argument("-o", "--output", help="Output file")
    
    args = parser.parse_args()
    mi = args.minimum
    ma = args.maximum
    pattern = args.pattern
    characters = args.characters
    output = args.output
    
    if pattern == None:
        generate_num(mi, ma, output, characters)
    else:
        generate_pattern(pattern, output)
    
