import sys

def find_pair(gifts, target):
	length = len(gifts)
	# if there is only 1 item, we can't find two items
	if(length<2): return "Not Possible"
	# initialise pointers
	start = 0
	end = length - 1
	# initialising values
	p1 = gifts[0]
	p2 = gifts[1]
	closestSum = p1[1] + p2[1]
	minDiff = target-closestSum
	if(minDiff<0): 
		# balance amount is less than the value of cheapest 2 items
		return "Not Possible"
	while(start<end):
		# the loop condition makes sure that we aren't repeating values
		closestSum = gifts[start][1] + gifts[end][1]
		diff = target-closestSum
		if(diff==0): 
			# sum of items = balance amount
			return (gifts[start],gifts[end])
		elif(diff<0): 
			# sum of items > balance amount
			end-=1
		else: 
			# sum of items < balance amount
			if(diff<minDiff):
				# searching for the sum so that minimum balance is left
				minDiff = diff
				p1 = gifts[start]
				p2 = gifts[end]
			start+=1

	return (p1,p2)


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
		
		result = find_pair(gifts,target_price)
		if(type(result) == tuple):
			print result[0][0]+" "+str(result[0][1])+", "+result[1][0]+" "+str(result[1][1])
		else:
			print result 

setup()
