import numpy as np
L = []
n = int(input("Enter number of student: "))
for i in range (1,n+1):
    print("Student",i,"Marks: ")
    m = []
    for i in range(1,6):
        marks = int(input())
        m.append(marks)
    L.append(m)
    print(np.array(L))
    arr = np.array(L)
    total = np.sum(arr)
    total_marks = arr.size
    avg = total/total_marks
    print("The average is: ",avg)
    if avg>=90 and avg <=100:
        print("Your grade is : A")
        print("outstanding")
    elif avg>=80 and avg <90:
        print("Your grade is : B")
        print("Very Good")
    elif avg>=70 and avg <79:
        print("Your grade is : C")
        print("Average")
    elif avg>=60 and avg <=69:
        print("Your grade is : D")
        print("Work on your self")
    elif avg <60:
        print("Your grade is : E")
        print("TUMHARA padhne likhne ka koi fayada nhi h")
