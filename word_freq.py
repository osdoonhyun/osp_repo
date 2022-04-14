#!/usr/bin/python3

import re
import sys


def CountFrequency(filename, n):
  f=open(filename)
  lines=f.readlines()

 for l in lines:
    print(l)

  for line in lines:
    new_string=re.sub(r"[^a-zA-Z0-9]"," ",line)

    print("1:" + new_string)
    new_list=new_string.split()
    print(new_list)

    new_dic = dict.fromkeys(new_list)


if __name__ == "__main__":

  input1 = str(sys.argv[1])
  input2 = int(sys.argv[2])

  CountFrequency(input1,input2)

