# generate all permutations of anagram and check if its an english word
from english_words import english_words_lower_set
from itertools import permutations, combinations
# use english_words_lower_set for test

string = "sasneo"
string_list = string.split()


# method 1 : diy function


# method 2 : itertools
# how efficient is itertools


l = list(permutations(string))
print(type(l))
words = []


for item in l:
    print(item, ''.join(item), ''.join(item) in english_words_lower_set)
    if ''.join(item) in english_words_lower_set:
        words.append(''.join(item))

#l2 = list(combinations(string, 6))
#words2 = []

#for item in l2:
    #print(item, ''.join(item), ''.join(item) in english_words_lower_set)
    #if ''.join(item) in english_words_lower_set:
        #words2.append(''.join(item))

print(words)