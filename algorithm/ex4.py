# EX4.Create function to find Min number in array [2,3,5,0,11,5,2]
def max(array):
    max=array[0]
    for i in range(len(array)):
        if array[i]>max:
            max=array[i]
    return max
number=[2,3,5,0,11,5,2]
print(max(number))