#!/usr/bin/env python

# importing libraries and functions needed for further analysis 
import sys, re
from argparse import ArgumentParser

# pairsing the sequences 
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

# pairsing sequence's motifs
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# for classifying both, RNA and DNA sequences given as inputs
args.seq = args.seq.upper()                 # Note we just added this line

if re.search('^[ACGTU]+$', args.seq):
# as you can see I added an extra code which says that for being  a DNA
# needs to be a T and never a U 
# while for being an RNA sequence needs to be a U and never a T
    if re.search('T', args.seq) and not re.search('U', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq) and not re.search ('T', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

# for finding the motifs 
if args.motif:
  args.motif = args.motif.upper()
  print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
  if re.match(args.motif, args.seq):
    print("find out")
  else:
    print("not located")


