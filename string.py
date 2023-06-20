# str1 = "welcome"
# print(str1)
# print(type(str1))
#
# print(str1[0])
# print(str1[2])
# print(str1[-1])
# print(str1[-4])
# for i in str1:
#     print(i,end='')
# for i in str1:
#     print(i,end='\n')
# print(dir(str))
# print(help(str))
#       123456789101112
# str2 = "Enthusiasm"
# print(str2[1:7])
# print(str2[0:4]+str2[-6:-1])
# print(str2[4:6])
# print(str2[1::2]) #***
# print(str2[0::2]) #***
# print(str2[-1:-5:-1])
# print(str2[7:1:-1])

# String concatenation
# s1 = "Mukesh"
# s2 = "Kumar"
# print(s1+" "+s2)
# print((s1+" ")*3)
# print(("Mohan"+" ")*3)

# String split (***)
# s = "Python is very easy language"
# #print(s)
# #print(type(s))
# s1 = s.split(' ')
# print(s1)
# s1 = s.split(' ',3)
# #print(s1)
# print(type(s1))
#
# for i in s1:
#     print(i)

# capitalize
# s = "pyThon IS vEry eaSy"
# print(s)
# s1 = s.capitalize()
# print(s1)
# s1 = s.title()
# print(s1)

# Upper and Lower
# str3 = "Welcome"
# s3 = str3.upper()
# print(s3)
# s4 = str3.lower()
# print(s4)

# #String count
# str4 = "Python is very easy and it is oop and it is interpreter"
# substring = "is"
# s4=str4.count(substring)
# print(s4)
# print(str4.count("very"))
# print(str4.count("easy"))
# print(str4.count("t"))
# print(str4.count(""))

# string replace
# str5 = "My name is Mukesh Kumar"
# s5 = str5.replace("Mukesh","timcook")
# print(s5)

# string join ***
# str1 = "Mohan"
# print(", ".join("Mohan"))
# print(" ".join(["Sai","Mohan","Raj","Durga"])) #Value can be any form List, Tuple, Set

# String reverse ***
# print(" ".join(reversed("Welcome")))
# print("".join(reversed(str1)))
# print(str1[::-1])

# String sort
# str7 = "Python is very easy language"
# s7 = str7.split(" ")
# print(s7)
# print(type(s7))
# s7.sort()
# print(s7)

s = "python is very easy"


# # print(s)
# s1 = s.split(" ")
# print(s1)
# print(type(s1))
# s1.sort()
# print(s1)
# s1.sort(reverse=True)
# print(str(s1))
#
# #for i in s1[::-1]:
# #    print(i,end=" ")
#
#
# for i in s1:
#     print(i[::-1],end=" ")

# s3 = "nohtyp si yrev ysae"
# s4 = s3.split(" ")
# print(s4)
# for i in str(s4[::-1]):
#      print(i,end="")

# String swapcase
# s = "DuRgasOFT"
# print(s)
# print(s.swapcase())


# String strip, lstrip, rstrip
# s = "  India  "
# print(s)
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())
#
# #String length
# print(len(s))

# String find, index, rindex
# s = "python is very easy and it is oop and it is interpreter"
# #print(s.find("is"))
# print(s.find("x"))
# # print(s.index("is"))
# #print(s.index("x"))
# print(s.rindex("is"))


# String max, min
# print(ord('D'))
#
# s = "Durgasoft"
# print(max(s))
# print(min(s))

# String partition
# s = "python is very easy and it is oop"
# s1 = s.partition("a")
# print(s1)
# print(type(s1))
#
# str1 = 'welcome'
# z = ''
# for i in str1:
#     z = i + z
# print(z)


# def reverse_str(str1):
#     z = ''
#     for i in str1:
#         z = i + z
#
#     return z
#
#
# print(reverse_str('India'))


def reverse_str(str1):
    z = ''
    for i in str1:
        z = i + z

    if str1 == z:
        print('Palindrome')

    else:
        print('Not palindrome')


reverse_str(input("Enter the value :").lower())

# str1 = input("Enter the string:").casefold()
# if str1 == str1[::-1]:
#     print('Palindrome')
# else:
#     print('Not palindrome')

# str1 = (input("Enter the value: ").casefold())
# s1 = str1.split()
# s1.sort()
# print(s1)