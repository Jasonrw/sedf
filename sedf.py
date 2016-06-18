#!/usr/bin/python
# -*- coding:utf-8 -*-

from optparse import OptionParser
import itertools

def main():
  parser = OptionParser() 
  parser.add_option("-f", "--file", dest="inputMetaFile")
  parser.add_option("-o", "--output", dest="outputFile")
  parser.add_option("-c", "--conbination", action="store_true", dest="conbination")
  parser.add_option("-s", "--split", dest="split_symbol")
  (options, args) =  parser.parse_args() 

  if options.inputMetaFile:
    metaList = parseFile(options.inputMetaFile)
  else:
    parser.error("please specify a input file")
    exit()

  if options.split_symbol:
    splitSymbol = options.split_symbol
  else:
    splitSymbol = ""

  if options.conbination:
    conbine(splitSymbol, metaList, int(args[0])) 
  else: 
    permutate(splitSymbol, metaList, int(args[0]))

def parseFile(inputFilePath):
  file = open(inputFilePath, "r")
  metaList = file.read().splitlines()
  return metaList

def conbine(splitSymbol, metaList, length):
  conbinationsOrigin = list(itertools.combinations(metaList, length))
  for tupleItem in conbinationsOrigin:
    print splitSymbol.join(tupleItem)

def permutate(splitSymbol, metaList, length):
  permutationsOrigin = list(itertools.permutations(metaList, length))
  for tupleItem in permutationsOrigin:
    print splitSymbol.join(tupleItem)


if __name__ == "__main__":
  main()
