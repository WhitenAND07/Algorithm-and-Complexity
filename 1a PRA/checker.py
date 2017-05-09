#!/usr/bin/env python

import sys

def load_cargo( filename ) :
    return [int(line.split()[1]) for line in open( filename )]

def is_subseq(x, y):
    return all(c in iter(y) for c in x)

def is_increasing( l ) :
    return all(int(l[i]) < int(l[i+1]) for i in xrange(len(l)-1))

c = load_cargo( sys.argv[1] )
a = load_cargo( sys.argv[3] )
b = load_cargo( sys.argv[2] )

if len( a ) != len( b ) or not is_increasing( a ) or not is_subseq( a, c ) :
    sys.exit(-1)
