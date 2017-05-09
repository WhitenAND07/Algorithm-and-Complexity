#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim : set fileenconding=utf8 :

import optparse
import sys
import timeit

__version__ = '2.1'
__authors__ = "Jordi Blanco Lopez  ---> NIF: 20998"

'''

Procediment per calcular els costos Empirics

    start = timeit.timeit()
    for x in xrange(1,1000):
        solution = recursiu(boxnum, weight)
        end += timeit.timeit() - start
    print end/10

'''


def main():
    if len(sys.argv) == 2:
        boxnum, weight = readFile(sys.argv[1])
    elif len(sys.argv) > 2:
        boxnum, weight = readFile(sys.argv[2])
    else:
        boxnum, weight = read_keyboard()

    if options.recursiu == True:
        truckB, truckW = recursiu(boxnum, weight)
    else:
        truckB, truckW = iteratiu(boxnum, weight)

    print_results(truckB, truckW)


def readFile(fitxer):
    """Read File"""
    boxnum = []
    weight = []
    f = open(str(fitxer), 'r')
    for line in f:
        temporal = line.split()
        boxnum.append(int(temporal[0]))
        weight.append(int(temporal[1]))
    return boxnum, weight


def read_keyboard():
    """Read about Keyboard"""
    weight = []
    boxnum = []
    boolean = True
    while boolean == True:
        line = raw_input(
            'Enter the number of the Box and the weight where is (separated by spaces):')
        if line == '':
            boolean = False
        else:
            temporal = line.split()
            boxnum.append(int(temporal[0]))
            weight.append(int(temporal[1]))

    return boxnum, weight


def recursiu(boxnum, weight):
    truckB = []
    truckW = []
    lastbox = []
    index = 0
    if len(boxnum) == 1:
        return boxnum[0], weight[0]
    else:
        posbest = searchbestlenR(weight)
        recursiu2(boxnum, weight, posbest, index, truckB, truckW, lastbox)
        return truckB, truckW


def recursiu2(boxnum, weight, posbest, index, truckB, truckW, lastbox):
    if index < len(weight):
        if posbest == index:
            truckB.append(int(boxnum[index]))
            truckW.append(int(weight[index]))
            lastbox = weight[index]

        elif posbest < index:
            if weight[index] > lastbox:
                lastbox = weight[index]
                truckB.append(int(boxnum[index]))
                truckW.append(int(weight[index]))

        index += 1
        recursiu2(boxnum, weight, posbest, index, truckB, truckW, lastbox)


def searchbestlenR(weight):
    bestlen = 1
    posbest = 0
    index = 0
    if len(weight) == 1:
        return posbest

    else:

        for firstindex in range(0, len(weight)):
            littleWeight = weight[firstindex]
            large = 1
            large = searchbestlenR2(weight, large, littleWeight, firstindex, index)

            if bestlen < large:
                bestlen = large
                posbest = firstindex

        return posbest


def searchbestlenR2(weight, bestlen, littleWeight, firstindex, index):
    if index < len(weight):
        if weight[index] > littleWeight and firstindex < index:
            littleWeight = weight[index]
            bestlen += 1

        index += 1
        return searchbestlenR2(weight, bestlen, littleWeight, firstindex, index)
    else:
        return bestlen


def iteratiu(boxnum, weight):
    truckB = []
    truckW = []
    if len(boxnum) == 1:
        return boxnum[0], weight[0]
    else:
        posbest = searchbestlen(weight)

        for i in range(0, len(weight)):
            if i == posbest:
                truckB.append(int(boxnum[i]))
                truckW.append(int(weight[i]))
                lastbox = weight[i]

            elif i > posbest:
                if weight[i] > lastbox:
                    lastbox = weight[i]
                    truckB.append(int(boxnum[i]))
                    truckW.append(int(weight[i]))

        return truckB, truckW


def searchbestlen(weight):
    bestlen = 0
    for i in range(0, len(weight)):
        large = 1
        littleWeight = weight[i]

        for x in range(0, len(weight)):
            if littleWeight < weight[x] and i < x:
                littleWeight = weight[x]
                large = large + 1

        if bestlen < large:
            bestlen = large
            posbest = i

    return posbest


def print_results(truckB, truckW):
    resultB = str(truckB)
    resutlB = resultB.replace("[", " ")
    resultB = resutlB.replace("]", " ")
    resultW = str(truckW)
    resultW = resultW.replace("]", " ")
    resultW = resultW.replace("[", " ")
    print "Solution: Les caixes" + resultB + "amb alçades" + resultW


if __name__ == "__main__":
    parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), \
                                   usage=globals()["__doc__"], \
                                   version=__version__)
    parser.add_option('-r', '--recursiu', action='store_true', \
                      dest="recursiu")
    parser.add_option('-i', '--iteratiu', action='store_false', \
                      dest="iteratiu")
    (options, args) = parser.parse_args()

    if len(sys.argv) > 3: parser.error( \
        'bad args, Heu de escriure python ilerda.py [-i/-r] ' \
        '(iteratiu/recursiu) [fitxer-caixes.txt]')
    main()
