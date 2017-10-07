# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 12:30:24 2016

@author: Lichenglong Liyidan
"""

#-------------------------------------------------------#
fp = open("0trainingdata.txt","r")
line = fp.readline()
traindic = {}
while(line != ""):
    wordlist = line.split("  ")
    for wordtemp in wordlist:
        temp = wordtemp.split("/")
        if temp[0] not in traindic:
            traindic[temp[0]] = {}
        if temp[-1] not in traindic[temp[0]]:
            traindic[temp[0]][temp[-1]] = 0
        traindic[temp[0]][temp[-1]] += 1
    line = fp.readline()
fp.close()
#-------------------------------------------------------#
fp = open("1dicInTrain.txt","r")
line = fp.readline()
worddic = {}
while(line != ""):
    line.strip()
    temp = line.split(" \t")
    typlist = temp[-1][1:-1]
    worddic[temp[0]] = []
    for typ in typlist:
        worddic[temp[0]].append(typ)
    line = fp.readline()
fp.close()
#-------------------------------------------------------#
maxlen = 0
for temp in traindic:
    if len(temp) > maxlen:
        maxlen = len(temp)

fp = open("test.txt","r")
outfp = open("result.txt","w")
line = fp.readline()
name_flag = False
end_flag = False
while(line != ""):
    start = 0
    while(start < len(line) - 1):
        if start+maxlen > len(line):
            word = line[start:len(line)]
        else:
            word = line[start:start+maxlen]
        mword = ""
        mnum = 0
        
        if (name_flag):
            for i in range(4):
                for j in range(i,4):
                    if (word[i:j+1] in traindic):
                        end_flag = True
                    elif (word[i:j+1] in worddic):
                        end_flag = True
                    break
                if (end_flag):
                    end_flag = False
                    break
            if i == 0:
                mword = word[i:j+1]
            else:
                mword = word[0:i]
            
            outfp.write(mword+"\n") 
            name_flag = False
            start += len(mword)
            continue
        
        while(word != ""):
            if word in traindic:
                for i in traindic[word]:
                    if mnum < traindic[word][i]:
                        mnum = traindic[word][i]
                        mword = word
                break
            elif (word in worddic) and (mnum == 0):
                mword = word
            elif mword == "":
                if len(word) == 2:
                    mword = word
            word = word[:-1]
        
        if word in worddic:
            for typ in worddic[word]:
                if typ == "nr":
                    name_flag = True
                    break
        
        outfp.write(mword+"\n")
        start += len(mword)
    line = fp.readline()

outfp.close()
fp.close()