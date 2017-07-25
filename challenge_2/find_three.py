import sys

def find_three(gifts, target):
	length = len(gifts)
	# if there are less than 3 items, we can't find 3 items
	if(length<3): return "Not Possible"
	# initialising values
	p1 = gifts[0]
	p2 = gifts[1]
	p3 = gifts[2]
	closestSum = p1[1] + p2[1] + p3[1]
	minDiff = target-closestSum
	if(minDiff<0): 
		# balance amount is less than the cheapest 3 items
		return "Not Possible"
	for i in xrange(length-2):
		# selecting 1 item at a time, and then choosing the other two with pointers
		start = i+1
		end = length-1
		while(start<end):
			# making sure we dont repeat
			closestSum = gifts[i][1]+gifts[start][1]+gifts[end][1]
			diff = target-closestSum
			if(diff==0): 
				# sum of items = balance amount
				return (gifts[i],gifts[start],gifts[end])
			elif(diff<0): 
				# sum of items > balance amount
				end-=1
			else:
				# sum of items < balance amount
				if(diff<minDiff):
					# searching for the sum so that minimum balance is left
					minDiff = diff
					p1 = gifts[i]
					p2 = gifts[start]
					p3 = gifts[end]
				start+=1

	return (p1,p2,p3)

# Setup to read the text file of gifts and prices and the balance on the card
def setup():
	if(len(sys.argv) < 3):
		print "Usage: " + str(sys.argv[0]) + " prices.txt 'target_price'"
	else:
		target_price = int(sys.argv[2])
		file = open(sys.argv[1])
		gifts = list()
		for line in file: 
			gift = line.split(',')
			# gifts is an array of tuples
			gifts.append((gift[0], int( gift[1].strip()) ))
		
		result = find_three(gifts,target_price)
		if(type(result) == tuple):
			print result[0][0]+" "+str(result[0][1])+", "+result[1][0]+" "+str(result[1][1])+", "+result[2][0]+" "+str(result[2][1])
		else:
			print result 

setup()