#!/usr/bin/python3

import re
import sys


def CountFrequency(filename, n):
    f=open(filename)    
    lines=f.readlines()

    text= {}
    for line in lines:
        new_string=re.sub(r"[^a-zA-Z0-9]"," ",line)

        new_list=new_string.split()

        for word in new_list:
            if (word in text):
                text[word] += 1
            else:
                text[word] = 1

    sortingCntText = sorted(text.items(), key= lambda x: x[1], reverse=True)

    cnt = 0 
    for key in sortingCntText:
        cnt = cnt + 1
        if(cnt <= n):
            print("%-20s %20d" %(key[0],key[1]))
        else:
            break

if __name__ == "__main__":

    input1 = str(sys.argv[1])
    input2 = int(sys.argv[2])

    CountFrequency(input1,input2)

