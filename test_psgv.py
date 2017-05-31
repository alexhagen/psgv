
import psgv
import os
import time

A = psgv.psgv()

A.key = 'needs_latex'
A.val = {"A": 5, "b": 10}

processed = A.val
print processed['A']

print ("the value of $needs_latex is:")
os.system(r"echo $needs_latex")

A.val["C"] = 20.0

print ("the value of $needs_latex is:")
os.system(r"echo $needs_latex")

time.sleep(10)
