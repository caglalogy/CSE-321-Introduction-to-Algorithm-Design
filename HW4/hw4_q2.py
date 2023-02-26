def find_median(arr):
    #if array has 0-1 elements; 
    if len(arr) == 0:
        return None 
    elif len(arr) == 1:
        return arr[0]

    # dividing array
    half = len(arr) // 2

    # first half part
    f_half = arr[:half]
    # print(first_half)

    # second half part
    s_half = arr[half:]
    # print(second_half)

    #the median of first and second half
    m1 = find_median(f_half)
    m2 = find_median(s_half)

    # if the medians are equal, return
    if m1 == m2:
        return m1

    # if the median of the first half is greater than the second half, recursively call the function again for second half
    elif m1 > m2:
        return find_median(s_half)

    # vice versa
    elif m1 < m2:
        return find_median(f_half)


array = []
size = int(input("how many elements do you want in array: "))
print("enter the numbers")
for i in range(size):
    new_element = int(input())
    array.append(new_element)
    
print("array is",array)
print("median of array is:",find_median(array))