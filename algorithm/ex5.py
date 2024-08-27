# EX5.Create function to count of number 5 in array [2,3,5,0,11,5,2]
def count(array):
    count=0
    for i in range(len(array)):
        count+=1
    return count
number=[2,3,5,0,11,5,2]
print(count(number))
