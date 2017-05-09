
import sys, random

def combinations( l ) :
    if l == [] : return [ [] ]
    c = combinations( l[1:] )
    return c + [ [l[0]] + x for x in c ]

def check_solution( l ) :
    return all(l[i] < l[i+1] for i in xrange(len(l)-1))

def find_solution( cargo ) :
    c = combinations( cargo )
    maximal = []
    for x in c :
        if len( x ) > 0 :
            if check_solution( [ e[1] for e in x ] ) :
                if len( x ) > len( maximal ) :
                    maximal = x
    return maximal

max_size = int( sys.argv[1] )
num_boxes = int( sys.argv[2] )

cargo_types = ['frumento', 'armis', 'aere', 'pannum', 'sparto', 'garum']

cargo = []
for x in range( num_boxes ) :
       cargo.append( ( random.sample( cargo_types, 1 )[0], random.randint( 1, max_size ) ) )

print '\n'.join( [ x + ' ' + str( y ) for x,y in cargo ] )

print >> sys.stderr, '\n'.join( [ x + ' ' + str( y ) for x,y in  find_solution( cargo ) ] )
