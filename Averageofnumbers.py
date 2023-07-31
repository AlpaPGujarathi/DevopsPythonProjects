def collectnumbers(x):
    for i in range(0,x):
        y = float(input("Enter the numbers: "))
        my_list.append(y)


def average():
    total = 0
    for i in range(0,len(my_list)):
        total = total + my_list[i]
    aver = total/len(my_list)
    return aver






my_list = []
num = int(input("How many numbers you want the average of : "))
collectnumbers(num)
average = average()
print("The average is ",average)




