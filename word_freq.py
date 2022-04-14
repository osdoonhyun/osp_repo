#!/usr/bin/python3

import re
import sys


def CountFrequency(filename, n):
    f=open(filename)    
    lines=f.readlines()

    for line in lines:
        new_string=re.sub(r"[^a-zA-Z0-9]"," ",line)

        new_list=new_string.split()

        new_dic = dict.fromkeys(new_list)

        text={}

        for item in new_dic:
            if (item in text):
                text[item] += 1
            else:
                text[item] = 1

    word_list=sorted(text.items(),key=lambda x: x[1],reverse=True)

    for key in word_list(n):
        print("%-20s %20d" %(key,word_list[key]))


if __name__ == "__main__":

    input1 = str(sys.argv[1])
    input2 = int(sys.argv[2])

    CountFrequency(input1,input2)

