#1. Muhammad Syazmi bin Suhaidi 1814573

import re
import os
import math

#You have to call this function in your interpreter or editor to use/activate it
def ngram():

    os.chdir("D:\\Download\\WhatsApp\\Syazmi")
    #create an empty dictionary for unigrams   
    unigram = {}
    bigram = {}
    trigram = {} 
    #using "with" will close the file immediately after last call
    with open("text-ngram.dat","r") as rfile:
        infile = rfile.readlines()

    unifile = open("unigram.dat","w")
    bifile = open("bigram.dat","w")
    trifile = open("trigram.dat","w")   
    
    sent = [s for s in infile[0].split(".")]
   
    for line in sent:        
        for j in range(len(line.split())-1):
            uni = line.split()[j]
            #example of storing frequency counts of unigrams
            if uni not in unigram.keys():
            	unigram[uni] = 1
            else:
                unigram[uni] += 1

            bi = line.split()[j]+" "+line.split()[j+1]

            if bi not in bigram.keys():
            	bigram[bi] = 1
            else:
                bigram[bi] += 1

            unifile = open("unigram.dat","a")
            bifile = open("bigram.dat","a")            
            unifile.write(str(uni)+"\n")
            bifile.write(str(bi)+"\n")            
            unifile.close()
            bifile.close()

        for k in range(len(line.split())-2):
            trifile = open("trigram.dat","a")            
            tri = line.split()[k]+" "+line.split()[k+1]+" "+line.split()[k+2]
            if tri not in trigram.keys():
            	trigram[tri] = 1
            else:
                trigram[tri] += 1
            trifile.write(str(tri)+"\n")
            trifile.close()

    print("Unigram:")
    print(unigram)
    print()
    print("Bigram:")
    print(bigram)
    print()
    print("Trigram:")
    print(trigram)
    print()

    #Trigram for the test sentences
    testtrigram = {} 
    with open("test-text.dat","r") as rfile:
        infile = rfile.readlines()

    testtrifile = open("testtrigram.dat","w")  
    
    sent = [s for s in infile[0].split(".")]

    for line in sent:
        for k in range(len(line.split())-2):
            testtri = line.split()[k]+" "+line.split()[k+1]+" "+line.split()[k+2]
            if testtri not in testtrigram.keys():
            	testtrigram[testtri] = 1
            else:
                testtrigram[testtri] += 1
            testtrifile = open("testtrigram.dat","a")            
            testtrifile.write(str(testtri)+"\n")
            testtrifile.close()
            
    print("Testing sentence trigram:")
    print(testtrigram)
    print()
    
    # v = 108
    #question 4
    print("Probability of each trigram in test sentence: \n")
    print("P(processing | Natural languange):\n")
    try:
        x = trigram["Natural languange processing"]
    except LookupError:
        x = 0
    else:
        x = trigram['Natural languange processing']
    try:
        y = bigram['Natural languange']
    except LookupError:
        y = 0
    else:
        y = bigram['Natural languange']
    processing_nl = (x+1)/(y+108)
    print("C(Natural languange processing) / C(Most mental) ")
    print("(",x,"+ 1 )/(",y,"+ 108 ) = ", end ='')
    print(processing_nl)
    print()
            
ngram()

        
