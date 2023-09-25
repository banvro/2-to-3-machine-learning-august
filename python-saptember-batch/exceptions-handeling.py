# errors   
    # 1) compile time error
    # 2) logicAL ERRORS 
    # 3) RUN TIME ERROR

# if 10 ==10
#     print("hello")
# a 10


# logical errors 

# a = 10
# b = 0
# c = a/b

# print(c)


# run time error 


# age = int(input("ENter your age : "))

# print(age)

# excaptio handeling 

# try :

# except Exception:

# else:

# finally:
# a = 10
# b = 0
# age = int(input("Enter your age : "))

# try:
#     age = int(input("Enter your age : "))
#     print(a/b)
# except ZeroDivisionError:
#     print("it is not possible to devide with zero")

# except ValueError:
#     print("please enter valid age..")
# else:
#     print("the age is : ", age)

# finally:
#     print("i am finnly")







# a = 10
# b = 0

# try:
#     c = a/b
#     age = int(input("Enter your age : "))

# except Exception as e:
#     print(e)

# else:
#     print("the age is : ", age)

# finally:
#     print("i am finnly")
    
    
# print("runningg.......")



a = 10
b = 0
try:
    age = int(input("Enter your age : "))
    print(a/b)
except ZeroDivisionError:
    print("it is not possible to devide with zero")

except ValueError:
    print("please enter valid age..")
else:
    print("the age is : ", age)

finally:
    print("i am finnly")
