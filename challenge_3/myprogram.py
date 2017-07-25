import Queue
import sys

def solution(pattern):
	# counts number of X's in the input
	count = pattern.count("X") 
	for i in xrange(2 ** count):
		# there will be 2^n combinations of 0's and 1', where n is the number of X's
		# thus, loop over all numbers from 0 to 2^n in binary
		binary_result = bin(i)[2:]
		binary_result = ("0" * (count - len(binary_result))) + binary_result
		# converting string into an array
		barray = list(binary_result) 
		pattern_array = list(pattern)
		# loop through the pattern array to find X and replace with the binary number
		for x in xrange(len(pattern)):
			if pattern[x] == "X":
				pattern_array[x] = barray.pop()
		# now we have a combination, so print it
		print "".join(pattern_array)



if len(sys.argv)  > 1:
	solution(str(sys.argv[1]))
else:
	print "Usage: " + str(sys.argv[0]) + "XXXXXX"
