#   Course: CS 2302
#   Assignment: Lab V
#   Author: Oswaldo Escobedo 
#   Instructor: Dr. Fuentes
#   TA: Harshavardhini Bagavathyraj
#   Date of Last Modification: 04/9/2020
#   Purpose of the Program: to analyz multiple text documents using hashtable
import numpy as np
import os
import hash_table_chain as htc
     
def get_word_list(text):
    # Receives a string containing a document
    # Returns a list of strings containing the words in the document
    text = text.lower()
    word_list = []
    curr_wrd = ''
    for c in text:
        if ord(c)>=97 and ord(c)<=122:
            curr_wrd = curr_wrd+c
        else:
            if len(curr_wrd)>0:
                word_list.append(curr_wrd)
                curr_wrd = ''
    return word_list

def get_stop_word_list(): 
    f = open('stop_words.txt') 
    txt = f.read()
    f.close()
    stop_words = get_word_list(txt) 
    return stop_words

def create_hashtable(L):
    h = htc.HashTableChain(len(L))
    for i in L:
        h.insert(i,i)
    return h 
 
def remove_stop_words(txt,stop):
    ctxt = txt.copy()
    c = 0
    i = 0
    while i < len(ctxt):
        if stop.retrieve(ctxt[i]) in ctxt: # stop_word found
            ctxt.pop(i) # Deletes the stop_word from the text
            c += 1 # Counts how many stop_words were in the text
        else: # Because each time we are decreasing the text length, we will only
            i += 1  # change i when there is no stop_word in the current position
    return ctxt,c

def most_repeated_word(L):
    h = htc.HashTableChain(len(L))
    rep = ['',0] # Stores the most repeated word and how many times appears in the text
    for i in L:
        count = h.retrieve(i)
        if count == None: # Word is not in hashtable
            h.insert(i,1)
        else:
            count += 1
            h.update(i,count) # Updates the times a word appears in the text
            if count > rep[1]: # Updates the most repeated word
                rep[0],rep[1] = i,count
    return rep[0],rep[1]

def num_of_records(h):
    c = 0
    for b in h.bucket: # Visits each bucket
        c += len(b) # Counts how many record a bucket has
    return c 

def load_factor(h):
    s = 0
    for b in h.bucket:
        if len(b) >= 1:
            s += len(b) 
    return round(s/len(h.bucket),3) # Rounds the final answer by 3 decimal places

def empty_buckets(h):
    c = 0
    for b in h.bucket:
        if len(b) == 0: # Empty bucket found
            c += 1
    return round(c/len(h.bucket),3)

def long_buckets(h):
    max_buck = 0
    c = 0
    for b in h.bucket:
        if len(b) > 1: # Long bucket found
            c += 1
        if len(b) > max_buck: # Updates the size of the longest bucket
            max_buck = len(b)
    return round(c/len(h.bucket),3),max_buck

def print_info(wl,stop,abstract): # Method to print the introduction of the text
    txt,count = remove_stop_words(wl,stop_table)
    stop_count = len(wl) - count
    print('Total Words: {}, total non-stop-words: {}'.format(len(wl),stop_count))
    print('Analysis of {} hash table'.format(abstract))
    h = create_hashtable(txt)
    statistics(h,txt) 
    
def statistics(h,L=[]): # Method that displays the statistics from the text
    long,length_long = long_buckets(h)
    total = len(h.bucket)
    rec = num_of_records(h)
    load = load_factor(h)
    empty = empty_buckets(h)
    print('Total buckets: {}'.format(total),end=', ')
    print('total records: {}'.format(rec),end=', ') 
    print('load factor: {}'.format(load),end='\n') 
    print('Empty bucket fraction in table: {}'.format(empty))
    print('Long bucket fraction in table: {}'.format(long))
    print('Length of longest bucket in table: {}'.format(length_long))
    if len(L) != 0: 
        word,times = most_repeated_word(L)
        print('Most common word: {} - occurs {} times'.format(word,times))

if __name__ == "__main__":

    abs_dir = '.\\abstracts\\'  # abstracts folder must be in current folder
    abstracts =   sorted(os.listdir(abs_dir)) # Abstract contains a lsit with all abstract file names
    
    stop_words = get_stop_word_list()
    stop_table = create_hashtable(stop_words)
    print('\nAnalysis of stop word hash table')
    statistics(stop_table)
    
    for abstract in abstracts:
        f = open(abs_dir+abstract, 'r', encoding="utf8")
        print('\nFile:',abstract)
        text = f.read()
        f.close()
        wl = get_word_list(text)  
        print_info(wl,stop_table,abstract)
        