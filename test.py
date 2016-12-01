import sys
rank = int(sys.argv[1])
size = int(sys.argv[2])

print "I am process %d out of %d processes" % (rank,size)
