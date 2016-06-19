#!/usr/bin/python
# -*- coding:utf-8 -*-

from optparse import OptionParser
import itertools


def main():
    usage = "usage: %prog intNuber -f inputFilePath [options]\n" \
            "  Example: ./sedf 3 -f metaFile -c\n" \
            "  this will generate a list of password conbination of your metaFile"
    parser = OptionParser(usage=usage)
    parser.add_option("-f", dest="inputMetaFile")
    parser.add_option("-o", dest="outputFile")
    parser.add_option("-c", action="store_true", dest="conbination")
    parser.add_option("-s", dest="split_symbol")
    (options, args) = parser.parse_args()

    if options.inputMetaFile:
        metaList = parseFile(options.inputMetaFile)
    else:
        parser.error("please specify a input file")
        exit()

    if len(args) > 0:
        length = int(args[0])
    else:
        print("default setting the length of 2, if you want to set your specific length, type a number after the program\n"
                     "eg. ./sedf 3 -f inputFilePath [options]")
        length = 2

    if options.split_symbol:
        splitSymbol = options.split_symbol
    else:
        splitSymbol = ""

    if options.conbination:
        passList = conbine(splitSymbol, metaList, length)
    else:
        passList = permutate(splitSymbol, metaList, length)
    passes = []
    for item in passList:
        password = splitSymbol.join(item)
        passes.append(password)

    if options.outputFile:
        print "out put to file"
    else:
        for item in passes:
            print item


def parseFile(inputFilePath):
    file = open(inputFilePath, "r")
    metaList = file.read().splitlines()
    return metaList


def conbine(splitSymbol, metaList, length):
    conbinationsOrigin = list(itertools.combinations(metaList, length))
    return conbinationsOrigin
    # for tupleItem in conbinationsOrigin:
    # print splitSymbol.join(tupleItem)


def permutate(splitSymbol, metaList, length):
    permutationsOrigin = list(itertools.permutations(metaList, length))
    return permutationsOrigin
    # for tupleItem in permutationsOrigin:
    # print splitSymbol.join(tupleItem)


if __name__ == "__main__":
    main()
