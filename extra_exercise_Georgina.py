#!/usr/bin/env python

# Imports
import sys, re
from argparse import ArgumentParser

# Inputs from command line
parser = ArgumentParser(description = 'Count percentage of nucleotides')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Obtaining the inputs
args = parser.parse_args()

# Checking for lower letters
args.seq = args.seq.upper()

# Showing results
counter=0
if re.search('^[ACGTU]+$', args.seq):
   # If the sequence is DNA
   if re.search('T', args.seq) and not re.search('U', args.seq):
      ts = args.seq.count("T")
      cs = args.seq.count("C")
      gs = args.seq.count("G")
      a = args.seq.count("A")
      counter= (ts+cs+gs+a)
      percT=ts/counter
      percC=cs/counter
      percG=gs/counter
      percA=a/counter
      print ("% of Ts: ", percT)
      print ("% of Cs: ", percC)
      print ("% of Gs: ", percG)
      print ("% of As: ", percA)
   
   # If the sequnece is RNA
   elif re.search('U', args.seq) and not re.search('T', args.seq):
      us = args.seq.count("U")
      cs = args.seq.count("C")
      gs = args.seq.count("G")
      a = args.seq.count("A")
      counter=(us+cs+gs+a)
      percU=us/counter
      percC=cs/counter
      percG=gs/counter
      percA=a/counter
      print ("% of Us: ", percU)
      print ("% of Cs: ", percC)
      print ("% of Gs: ", percG)
      print ("% of As: ", percA)
   
   # If the sequence is not DNA nor RNA
   else:
      print ("The sequnece is not DNA nor RNA")

# If the sequence is not DNA nor RNA
else:
   print ("The sequnece is not DNA nor RNA")
