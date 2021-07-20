'''
number_input =input("Please Enter a fast number: ")

print("divided by 2:",int(number_input)/2)


number_input_1 =input("Please Enter a number of 1: ")
number_input_2 =input("Please Enter a number of 2: ")

try:
    print("result:",int(number_input_1)*int(number_input_2)) 
except:
    print("En error occurd, please enter another number")


number_input_3 =input("Please Enter a number of 1: ")
number_input_4 =input("Please Enter a number of 2: ")

try:
    print("result:",int(number_input_3)*int(number_input_4)) 
except Exception as r:
    print("Error:",str(r))
    print("En error occurd, please enter another number")
    



number_input_3 =input("Please Enter a number of 1: ")
number_input_4 =input("Please Enter a number of 2: ")

try:
    print("result:",int(number_input_3)*int(number_input_4)) 
except Exception as r:
    print("Error:",str(r))
    print("En error occurd, please enter another number")
finally:
    print("done!")
'''



#try:
#    print(a)
#except NameError:
#    print("variable is not defined")


try:
    int("mahdi hasan")
except NameError:
    print("variable is not defined")
except ValueError:
    print("can't convert a string to an integer")


try:
    #print(a)
    int("mahdi hasan")
except NameError:
    print("variable is not defined")
except ValueError:
    print("can't convert a string to an integer")



try:
    print("MAHDI HASAN")
except NameError:
    print("variable is not defined")
except ValueError:
    print("can't convert a string to an integer")
else:
    print("There is no error")

