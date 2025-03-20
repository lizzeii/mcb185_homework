import math

#strings
s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)
##' or " can be used interchangably if you need to use quotes inside a quote

print('hey "dude" don\'t tell me what to do')
##\ backslashing the quote can be used to tell python it is not a delimiter

##string operators
s = 'hello'
## = for assignment
s = 'hello' + ' world'
## + for concatenation
polyA = 'A' * 100
print(polyA)
## * for repetition
## <, >, and == for comparision
##comparison operators work with the ASCII values of strings

##string functions
len(s)
##len() specifies for the length of string
chr(36)
##chr() specifies for the character of the ASCII value
ord('a')
##ord() specifies for the ASCII value of the character

##method syntax
###must be inside print()
print(s.count(s1))
## .count() specifies for number of occurences of s1 in s
print(s.endswith(s1))
## .endswith() returns True if s ends with s1
print(s.startswith(s1))
## .startswith() returns True if s starts with s1
print(s.upper())
## does not have anything within ()
## .upper() returns the uppercase version of s
print(s.lower())
## .lower() returns the lowercase version of s
print(s.rstrip())
## .rstrip() specifies for striping characters from the right
print(s.replace(s, s1))
## .replace(a, b) converts substring a to b

print(s.replace('o', '').replace('r', 'i'))
## replaces the individual letters

##string formatting
print(f'{math.pi}')
##f string is a string preceded with f
print(f'{math.pi:f}')
print(f'{math.pi:.3f}')
## f inside {} specifies for 6 digits after the decimal on default
## 3f specifies for 3 digits after the decimal
print(f'{1e6 * math.pi:e}')
## e inside {} specifies for exponent notation
print(f'{"hello world":>20}')
## >20 specifies for right justify with space filler
print(f'{"hello world":.>20}')
## >20 specifies for right justify with dot filler
print(f'{20:<10} {10}')
## < specifies for left justify

print('{} {:.3f}'.format('str.format', math.pi))
##str.format() style
##empty curly braces filled with parameters of the str.format()
##pi goes into the into the second set of braces with 3 digits

print('%s %.3f' % ('printf', math.pi))
##printf-style
##left side is a string
##right side is a tuple
## %s specifies for string
##%.3f specifies for 3 digits

#indexes
seq = 'GAATTC'
print(seq[0], seq[1])
## seq[0] specifies for the first character in the sequence
## seq[1] specifies for the second character in the sequence
print(seq[-1])
## negative indexes count backwards from the right
## seq[-1] specifies for the last character in the sequence
for nt in seq:
    print(nt, end='')
print()
## end='' removes the space that separates each output
## makes the outputs return into a single line
for i in range(len(seq)):
    print(i, seq[i])
## len() sets the limit
## seq[i] specifies for the nth character in the sequence

#slices
##slice is a subset of a container
##similar to range(), takes initial position and end-before limit
s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])
##has a step size, assumed to be 1 when omitted
print(s[0:5], s[:5])
##initial value may be omitted, assumed to be 0
print(s[5:len(s)], s[5:])
##final value my be omitted, assumed to be length of string
print(s, s[::], s[::-1])
##[::-1] returns the string backwards
dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    print(i, codon)
    ##slicing into codons

#tuples
##generally constructed with comma-separated values in parentheses
tax = ('Homo', 'sapiens', 9606)
print(tax)
##s[0] = 'C'
##tax[0] = 'human'
##you cannot change the contents of strings and tuples through their indices
print(tax[0], tax[::-1])

#enumerate() and zip()

##enumerate()
##using range()
nts = 'ACGT'
for i in range(len(nts)):
    print(i, nts[i])
##using enumerate()
##outputs tuple containing index and value
for i, nt in enumerate(nts):
    print(i, nt)

##zip()
##using range()
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
    print(nts[i], names[i])
##using zip()
##retrieves an element from each container
##returns them in a tuple
for nt, name in zip(nts, names):
    print(nt, name)
##zip() and enumerate() can be used together
##tuples are unpacked using additional parentheses
for i, (nt, name) in enumerate(zip(nts, names)):
    print(i, nt, name)

#lists
##similar to tuples
##use [square brackets]
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)
##indices can be modified
nts.append('C')
print(nts)
## .append() allows elements to be added to the end of the list
last = nts.pop()
print(last)
## .pop() removes elements from the end of a list
nts.sort()
print(nts)
## .sort() specifies for sorting the list
## all elements in the list must have similar types, cannot mix ints and floats with strings
nts.sort(reverse=True)
print(nts)
## (reverse=True) sorts the list in reverse
nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)
##putting a list under a new variable just creates another name for the list
## list.copy() is used to do a shallow copy

##list()
items = list()
print(items)
items.append('eggs')
print(items)
## list() without arguments creates empty lists
stuff = []
print(stuff)
## empty lists can also be created through []
alph = 'ABCDEFGHIJKLMNOPQ'
print(alph)
aas = list(alph)
print(aas)
##lists can convert iterables into lists, a string into a list of letters

##split() and join()
text = 'good day            to you'
words = text.split()
print(words)
##str.split() splits strings into lists of strings
line = '1.41,2.72,3.14'
print(line.split(','))
##can be used for TSV or CSV data
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)
## ''.join() turns lists into strings by joining them with a delimiter

#searching
if 'A' in alph: print('yay')
if 'a' in alph: print('no')
## in can be used to find items in conditional statements
print('index G?', alph.index('G'))
## .index() returns the index of the first element it finds
## returns an error if it cannot find a matching items
print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))
## .find() returns the index of the first element it finds
## returns -1 if it cannot find the matching items
##if searching in a list or tuple, use in first if you don't know if the element is in the lsit

#command line data

##sys.argv
import sys
print(sys.argv)
##sys.argv specifies for the complete list of words on the command line
##short for argument vector
##is a list
##inserting other arguments on the command line adds them to the output list

##converting types
i = int('42')
x = float('0.61803')
print(i * x)
##int('') and float ('')converts text representations of numbers to ints/floats before doing math with them
#x = float('hello')
##inserting something that doesn't look like a number into a number returns an error

#pairwise comparison
#for i in range(0, len(list)):
#    for j in range(X, len(list)):
##change X according to what type of matrix you need
##X = 0 for all combinations
##X = i for half matrix with diagonal
##X = i + 1 for half matric without diagonal