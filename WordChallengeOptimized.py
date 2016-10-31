#!/usr/bin/env python
import os
import sys
import time

listw = []
f = open('words.txt')
for word in f.read().split():
    listw.append(word)
    
def make_trie(listw):
    trie = {}
    for word in listw:
        temp_trie = trie
        for letter in word:
            temp_trie = temp_trie.setdefault(letter,{})
        temp_trie = temp_trie.setdefault('_end_', '_end_')
    return trie

def traverse(word, sometrie, endcounter):
    if len(word) == 0:
        if endcounter > 0 and '_end_' in sometrie:
            return True
        return False
    letter = word[0]
    if letter in sometrie:
        if '_end_' in sometrie[letter]:
            endcounter = endcounter + 1
            if traverse(word[1:], trie, endcounter):
                return True
            endcounter = endcounter - 1
        return traverse(word[1:], sometrie[letter], endcounter)
    return False

trie = make_trie(listw)

count = 0
max1 = 0
max2 = 0
long1 = ""

for word in listw:
    if traverse(word,trie,0):
        if len(word)>max1:
            long2 = long1
            max2 = max1
            long1 = word
            max1 = len(word)
        else:
            if len(word)>max2:
                long2 = word
                max2 = len(word)
        count = count+1

print(count)
print(long1)
print(long2)