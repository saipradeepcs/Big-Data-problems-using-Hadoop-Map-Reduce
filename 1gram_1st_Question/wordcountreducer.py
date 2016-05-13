#!/usr/bin/env python

import sys
import string

word_count = 0
word_old = None

for line in sys.stdin:
  (key,val) = line.strip().split('\t',1)
  if word_old!=key:
    if word_old:
      print '%s\t%s' %(word_old,word_count)
      word_count=0
  word_old = key
  try:
    word_count = word_count + int(val)
  except:
    continue
print '%s\t%s' % (word_old,word_count)
     
  
