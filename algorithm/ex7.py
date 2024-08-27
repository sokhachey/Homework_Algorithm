# EX7.Create function to count negative number in array [-1,11,2,0,-1,4]
def count(array):
    count=0
    for i in range(len(array)):
        if array[i]<0:
            count+=1
    return count
number=[-1,11,2,0,-1,4]
print(count(number))