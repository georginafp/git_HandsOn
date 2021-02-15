#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Count percentage of nucleotides')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()                 # Note we just added this line
counter=0
if re.search('^[ACGTU]+$', args.seq):
   if re.search('T', args.seq) and not re.search('U', args.seq):
      ts = args.seq.count("T")
      cs = args.seq.count("C")
      gs = args.seq.count("G")
      ass = args.seq.count("A")
      counter= sum(ts, cs, gs, aas)
      percT=ts/counter
      percC=cs/counter
      percG=gs/counter
      percA=ass/counter
      print ("% of Ts": percT)
      print ("% of Cs": percC)
      print ("% of Gs": percG)
      print ("% of As": percA)

   if re.search('U', args.seq) and not re.search('T', args.seq):
      us = args.seq.count("U")
      cs = args.seq.count("C")
      gs = args.seq.count("G")
      ass = args.seq.count("A")
      counter=sum(us, cs, gs, ass)
      percU=us/counter
      percC=cs/counter
      percG=gs/counter
      percA=ass/counter
      print ("% of Us": percU)
      print ("% of Cs": percC)
      print ("% of Gs": percG)
      print ("% of As": percA)

