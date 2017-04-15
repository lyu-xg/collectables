# M(1,n)
# output MAX A[j]-A[i] over i<j

def maxProfit(input):
	low = float('inf')
	high = float('-inf')
	for n in input:
		high,low = max(high,n-low),min(low,n)	
	return high


if __name__ == '__main__':
	print maxProfit([1,23,4,5,6,2,2,3,5])
	print maxProfit([10,9,8,7])
	print maxProfit([-2,-4,-6])
	print maxProfit([10,9,8,8,7,8])
	print maxProfit([1,2,3])
	