# class
# object
# self
# constructer
# attrebutes

# Concepts of OOps

# 1) Inharitance  
    # 1) single inharitance
    # 2) multipal inharitance
    # 3) multilevel inharitance
    # 4) hirarical inharitance
    # 5) hibrid inharitance

# single level inharitance

# class xyz:
#     def mthd1(self):
#         print("i am from class parent ")
    
#     def mthd2(self):
#         print("i am from class pprent and methd mhd 2")

# class child(xyz):
#     def mthd3(self):
#         print("i am from class child..")

# obj = child()

# obj.mthd2()






# # 2) multipal inharitance 
# class xyz:
#     def mthd1(self):
#         print("i am from class parent ")
    
#     def mthd2(self):
#         print("i am from class pprent and methd mhd 2")

# class child:
#     def mthd3(self):
#         print("i am from class child..")


# class cls(xyz, child):
#     def mthd4(self):
#         print("ib am from class cls")

# obj = cls()

# obj.mthd2()


# 3 multilevel inharitance

# class xyz:
#     def mthd1(self):
#         print("i am from class parent ")
    
#     def mthd2(self):
#         print("i am from class pprent and methd mhd 2")

# class child(xyz):
#     def mthd3(self):
#         print("i am from class child..")


# class cls(child):
#     def mthd4(self):
#         print("ib am from class cls")

# obj = child()

# obj.mthd4()




# hirarical inharitance
# class xyz:
#     def mthd1(self):
#         print("i am from class parent ")
    
#     def mthd2(self):
#         print("i am from class pprent and methd mhd 2")

# class child(xyz):
#     def mthd3(self):
#         print("i am from class child..")


# class cls(xyz):
#     def mthd4(self):
#         print("ib am from class cls")

# obj = child()

# obj.mthd4()

# 5) hibrid inharitance

# class xyz:
#     def mthd1(self):
#         print("i am from class parent ")
    
#     def mthd2(self):
#         print("i am from class pprent and methd mhd 2")

# class child(xyz):
#     def mthd3(self):
#         print("i am from class child..")

# class cls(child):
#     def mthd4(self):
#         print("ib am from class cls")

# class cls2(child, cls):
#     def mthd5(self):
#         print("I am from clas2")
        
# obj = child()

# obj.mthd4()





# class userinfo:
#     def __init__(self, a, b):
#         self.name = a
#         self.age = b
    
#     def savedata(self):
#         print(f""" username : {self.name}
#         age : {self.age}
#         """)

# obj = userinfo("kriss", 20)
# obj1 = userinfo("moris", 78)
# obj2 = userinfo("hlo", 10)

# class newdata(userinfo):
#     def __init__(self, a, b, c):
#         super().__init__(a, b)
#         self.number = c
    
#     def savedata(self):
#         print(f""" username : {self.name}
#         age : {self.age}
#         number : {self.number}
#         """)
    
# x = newdata("xyz", 10, 983498234)
# x.savedata()
# obj.savedata()
# obj1.savedata()


def a(**z):
    print(z)
    # for i in z:
    #     print(i,z[i])
        
a(name="anuj", age=10)














