def helper_func(first, second):
	common = ""
	n1, n2 = len(first), len(second)
	i = 0
	j = 0

	while i <= n1 - 1 and j <= n2 - 1:
		if first[i] != second[j]:
			break
		common += first[i]
		i += 1
		j += 1
	
	return common

def longest_substring(strings, low, high):
	if low == high:
		return strings[low]

	if low < high:
		mid = low + (high - low) // 2

		first = longest_substring(strings, low, mid)
		second = longest_substring(strings, mid + 1, high)

		return helper_func(first, second)
# --------------------------------------------------------------------

def maximum_profit(prices):
	n = len(prices)
	if n == 0:
		return 0
	elif n == 1:
		return 0

    # Divide the input array into two halves
	mid = n//2
	left = prices[:mid]
	right = prices[mid:]

	# Recursively find the maximum profit that can be obtained from the left and right halves
	left_profit = maximum_profit(left)
	right_profit = maximum_profit(right)

	# Find the maximum profit that can be obtained by buying in the left half and selling in the right half
	cross_profit = 0
	left_min = min(left)
	right_max = max(right)
	if left_min < right_max:
		cross_profit = right_max - left_min

	# Return the maximum of the profits obtained
	return max(left_profit, right_profit, cross_profit)


def maximum_profit_without_dc(prices):
	n = len(prices)
	if n == 0:
		return 0
	elif n == 1:
		return

	max_profit = 0
	min_price = prices[0]
	for i in range(1, n):
		min_price = min(min_price, prices[i])
		max_profit = max(max_profit, prices[i] - min_price)

	return max_profit	
#-------------------------------------------------------------------------

def longest_increasing_subarray(arr):
    # Initialize lengths to store the lengths of the longest increasing sub-array ending at each index
    lengths = [1 for _ in range(len(arr))]

    # Loop through the array
    for i, num in enumerate(arr):
        # Look at all the elements before the current element
        for j in range(i):
            # If the element is smaller than the current element and can extend the current sub-array, update lengths[i]
            if arr[j] < num and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1

    # Return the maximum value in the lengths array
    return max(lengths)

def main():
	print("CSE321- HW5 Driver")
	print("""
	Press 1 for execution of Question-1
	Press 2 for execution of Question-2
	Press 3 for execution of Question-3
	""")

	choice = int(input(">>> "))
	if choice == 1:
		# Driver code
		list_of_string = []

		count = int(input("how many strings you want to enter:"))
		for i in range(0,count):
			temp = input(">>> ")
			list_of_string.append(temp)

		print("input:",list_of_string)
		print("output:",longest_substring(list_of_string, 0, count-1))

	elif choice == 2:
		# Driver code
		prices = []

		print("enter 7-day prices:")
		for i in range(0,7):
			temp = int(input(">>> "))
			prices.append(temp)

		print("input:",prices)
		print("output: maximum profit (with divide&conquer approach) ->",maximum_profit(prices)) 

		max_profit_w_dc = maximum_profit_without_dc(prices)
		print(f'output: maximum profit without dc: {max_profit_w_dc}')
	
	elif choice == 3:
		# Driver code
		ints = []

		count = int(input("enter the size of integer array:"))
		for i in range(0,count):
			temp = int(input(">>> "))
			ints.append(temp)

		print("input:",ints)
		print("output:", longest_increasing_subarray(ints))

	else: 
		print("undefined input.")

main()