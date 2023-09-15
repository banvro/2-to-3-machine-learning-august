# # fil = open("test.txt", 'r')

# # print(fil.read())
# # print(fil.readline())
# # print(fil.readline())

# a = 10
# b = 40
# c = a + b

# c = str(c)
# fil = open("x.txt", 'a')
# # fil = open("testtt.txt", 'w')

# fil.write(c)


# a = open("x.txt", 'w')
# print(a.write("20"))

# b = open("y.txt",'w')
# print(b.write("40"))

# a = open("x.txt", 'r')
# print(a.read())

# b = open("y.txt", 'r')
# print(b.read())

# c = a + b
# c = str(c)

# last = open("z.txt", 'a')
# last = open("z.txt", 'w')
# last.write(c)
# print(c.read())



zx = open("x.txt", 'r')
a = zx.read()

zx1 = open("y.txt", 'r')
b = zx1.read()

c = int(a) + int(b)
c = str(c)

zx2 = open("z.txt", 'w')
zx2.write(c)


