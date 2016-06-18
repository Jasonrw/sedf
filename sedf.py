#!/usr/bin/python
# -*- coding:utf-8 -*-

from optparse import OptionParser
import itertools

def main():
  usage = "usage: %prog metaCount [options]\n  Example: ./sedf 3 -f metaFile -c\n  this will generate a list of password conbination of your metaFile"
  parser = OptionParser(usage=usage) 
  parser.add_option("-f", dest="inputMetaFile")
  parser.add_option("-o", dest="outputFile")
  parser.add_option("-c", action="store_true", dest="conbination")
  parser.add_option("-s", dest="split_symbol")
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
