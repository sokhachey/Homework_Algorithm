# EX3.Create function to find Max number in array [2,3,5,0,11,5,2]
def min(array):
    min=array[0]
    for i in range(len(array)):
        if array[i]<min:
            min=array[i]
    return min
number=[2,3,5,0,11,5,2]
print(min(number))