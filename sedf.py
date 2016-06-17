#!/usr/bin/python
# -*- coding:utf-8 -*-
from optparse import OptionParser
import itertools

def main():
  parser = OptionParser() 
  parser.add_option("-f", "--file", dest="inputMetaFile")
  parser.add_option("-o", "--output", dest="outputFile")
  parser.add_option("-b", "--blank")
  (options, args) =  parser.parse_args() 

  if options.inputMetaFile:
    metaList = parseFile(options.inputMetaFile)
    conbine(options.blank, metaList, int(args[0])) 

def parseFile(inputFilePath):
  file = open(inputFilePath, "r")
  metaList = file.read().splitlines()
  return metaList

def conbine(addBlank, metaList, length):
  if addBlank:
    split = " "
  else:
    split =""
  conbinationsOrigin = list(itertools.combinations(metaList, length))
  for tupleItem in conbinationsOrigin:
    print "".join(tupleItem)

if __name__ == "__main__":
  main()
