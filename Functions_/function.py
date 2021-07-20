# function
# input, process, output
# parameter

def mah (has):
    pass

print(type(mah))

def wellcome (person):
    print(f"Hi {person}, wellcome to python master class")

wellcome("MAHDI HASAN")
wellcome("MASNUN HASAN")
wellcome("SHAFI KING")

def add (a ,b):
    total = a + b
    return total

print("add:",add (34 , 45))



def add_1 (a ,b):
    total = a + b
    return total

add_1_two_number = add_1(34 , 45)

print("add_1_two_number:",add_1_two_number)



def add_2 (a , b , c):
    total = a + b + c
    return total

add_2_two_number = add_2(34 , 45 , 67)

print("add_2",add_2(34 , 45 , 67))

print("add_2_two_number",add_2_two_number)




def student_result (marks):
    if marks >= 80:
        if marks >= 90:
            if marks >= 95:
                print("Result: Super Golden A+")
            else:
                    print("Result: Golden A+")
        else:
            print("Result: A+")
    elif marks >= 70 and marks <= 79:
        print("Result: A")
    elif marks >= 60 and marks <= 69:
        print("Result: A-")
    elif marks >= 50 and marks <= 59:
        print("Result: B")
    elif marks >= 40 and marks <= 49:
        print("Result: C")
    elif marks >= 33 and marks <= 39:
        print("Result: D")
    else:
        print("Result: F")  


student_result(92)

student_marks= [45, 78, 90, 98, 93, 56,23, 12, 72 ]

for mark in student_marks:
    student_result(mark)










