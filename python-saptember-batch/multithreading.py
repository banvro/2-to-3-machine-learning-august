# [a-zA-Z][a-z]+[0-9]*[a-z]*[@][a-z]+\.[a-z]{2,3}


# a = 10
# b = 20

# c = a + b

# print(c)

# print("helloooo.....")

# import threading






# print("this is strat")

# class xyz:
#     def mthd1(self):
#         for i in range(100):
#             print("yessssssssss")
    
#     def mthd2(self):
#         for i in range(100):
#             print("noooooooooooo")

# obj = xyz()

# obj.mthd1()
# obj.mthd2()

# print("i am watting")

# print("runninggg")

# print("nw process")

# print("done....")

import threading

print("this is strat")

class xyz:
    def mthd1(self):
        for i in range(100):
            print("yessssssssss")
    
    def mthd2(self):
        for i in range(100):
            print("noooooooooooo")

obj = xyz()

# obj.mthd1()
# obj.mthd2()

th1 = threading.Thread(target = obj.mthd1)
th2 = threading.Thread(target = obj.mthd2)

th1.start()
th2.start()


print("i am watting")

print("runninggg")

print("nw process")

th1.join()
th2.join()

print("done....")






# a = 10
# b = 20

# c = a + b

# z = c + 100

# print(z)





