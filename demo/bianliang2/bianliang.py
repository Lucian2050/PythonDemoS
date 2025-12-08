
# message = "a"
# print(message)
# message = "b"
# print(message)

# print(
# "This is a string.\n"
# 'This is also a string.\n'
# 'I told my friend, "Python is my favorite language".\n'
# "The language 'Python' is named after Monty Python, not the snake.\n"
# "Tom is Alin's friend"

# )

# # title()	首字母大写
# name = "ada lovelaca"
# print(name.title())

# name1= "ADA lovelaca"
# print(name.title())

# # upper()	全部大写
# name = 'aAa Bbbb'
# print(name.upper())
# print(name.lower())

# # 2.3.2 字符串中使用变量
# # f字符串 f= format（设置格式）的简写，python把{}李的变量替换为其值。
# # f字符串用来组合字符串，对组合的字符串作为一个整体使用字符串的内置函数进行整体的修改

# first_name = "ada"
# last_name = "Love"
# full_name = first_name + " "+last_name
# # print(full_name.title())
# full_name = f"{first_name} {last_name}"
# print(f"Hello, {full_name.title()}")
# # full_name = f"{first_name} {last_name}"
# # print(full_name.title())

# # print(first_name, last_name)



# # 2.3.3 空格 " "  制表符 \t  换行符 \n

# print("My favorite language is : \n\t C \n\t C++ \n\t Java \n\t Go ")


# # 2.3.4 删除空白
# # python字符串中间空格位置与是否存在空格，会导致字符串完全不一样，
# # 	在大多数情况下，我们无法控制用户的输出，需要在用户输出的基础上进行空格的处理，使的数据格式符合规范
# #	python提供了针对字符串首尾空白进行删除的内置方法 rstrip()

# favorite_language = "python "
# print(favorite_language)
# print(favorite_language.rstrip())
# favorite_language = favorite_language.rstrip()
# print(favorite_language)

# # 2.3.5 使用字符串时避免语法错误

# message = " i love 's'ss"
# print(message)


# # 练习
# # 2-3 个性化消息
# name = "Eric"
# # print(f"Hello, {name}, would you like to learn some Python today?")
# print(f"Hello, {name.title()}")

# # 2-4 调整名字大小
# my_name = 'Wang Ming'
# print(my_name.upper())
# print(my_name.title())
# print(my_name.lower())

# # 2-5 名言
# print("我们终将覆灭，\n我们要做好现在")

# # 2-6 名言2
# famous_person = 'chenhao'
# message = f"{famous_person} 芝兰生于幽谷，不以无人而不芳"
# print(message)

# # 2-7 剔除空白
# name = ' Zhu\t y \t n '
# print(name)
# print(name.rstrip())
# print(name.lstrip())
# print(name.strip())

#2.4 数
# 2.4.1 整数 整数支持加减乘除 乘方 运算次序修改
# 2.4.2 浮点数  浮点数与整数做任何运算，结果都是浮点数。 浮点数
# 2.4.3 整数和浮点数  1、两个整数相除，结果总是浮点数 2、任何运算整数和浮点数，其结果总是浮点数 3、
# 2.4.1 数中的下划线
# 2.4.5 同时给多个变量赋值
# 2.4.6 常量  在程序的整个生命周期内保持不变。python没有内置的常量。常量名必须使用全大写来指定。

print (1 + 1)
print(0.1 + 0.1)
print(0.1 + 0.2)
print(4/2.0)

universe_age = 14_000_000_00
print(universe_age)
universe_age1 = 2_00_00_0
print(universe_age1)


x, y, z = 9, 1, 2
print(x)

# 常量
MAX_NUM = 301
print(MAX_NUM)




# 练习
# 2-8 数字8
print(1+7)
print(10-2)
print(32/4)
print(2*4)
print(2 ** 3)

# 练习2-9：最喜欢的数　用一个变量来表示你最喜欢的数，再使用这个变量创建一条消息，指出你最喜欢的数是什么，然后将这条消息打印出来。

favorite_num = 301
message = f"我最喜欢的数字是：{favorite_num}"
print(message)




# message = "a"
# print(message)
# message = "b"
# print(message)

# print(
# "This is a string.\n"
# 'This is also a string.\n'
# 'I told my friend, "Python is my favorite language".\n'
# "The language 'Python' is named after Monty Python, not the snake.\n"
# "Tom is Alin's friend"

# )

# # title()	首字母大写
# name = "ada lovelaca"
# print(name.title())

# name1= "ADA lovelaca"
# print(name.title())

# # upper()	全部大写
# name = 'aAa Bbbb'
# print(name.upper())
# print(name.lower())

# # 2.3.2 字符串中使用变量
# # f字符串 f= format（设置格式）的简写，python把{}李的变量替换为其值。
# # f字符串用来组合字符串，对组合的字符串作为一个整体使用字符串的内置函数进行整体的修改

# first_name = "ada"
# last_name = "Love"
# full_name = first_name + " "+last_name
# # print(full_name.title())
# full_name = f"{first_name} {last_name}"
# print(f"Hello, {full_name.title()}")
# # full_name = f"{first_name} {last_name}"
# # print(full_name.title())

# # print(first_name, last_name)



# # 2.3.3 空格 " "  制表符 \t  换行符 \n

# print("My favorite language is : \n\t C \n\t C++ \n\t Java \n\t Go ")


# # 2.3.4 删除空白
# # python字符串中间空格位置与是否存在空格，会导致字符串完全不一样，
# # 	在大多数情况下，我们无法控制用户的输出，需要在用户输出的基础上进行空格的处理，使的数据格式符合规范
# #	python提供了针对字符串首尾空白进行删除的内置方法 rstrip()

# favorite_language = "python "
# print(favorite_language)
# print(favorite_language.rstrip())
# favorite_language = favorite_language.rstrip()
# print(favorite_language)

# # 2.3.5 使用字符串时避免语法错误

# message = " i love 's'ss"
# print(message)


# # 练习
# # 2-3 个性化消息
# name = "Eric"
# # print(f"Hello, {name}, would you like to learn some Python today?")
# print(f"Hello, {name.title()}")

# # 2-4 调整名字大小
# my_name = 'Wang Ming'
# print(my_name.upper())
# print(my_name.title())
# print(my_name.lower())

# # 2-5 名言
# print("我们终将覆灭，\n我们要做好现在")

# # 2-6 名言2
# famous_person = 'chenhao'
# message = f"{famous_person} 芝兰生于幽谷，不以无人而不芳"
# print(message)

# # 2-7 剔除空白
# name = ' Zhu\t y \t n '
# print(name)
# print(name.rstrip())
# print(name.lstrip())
# print(name.strip())

#2.4 数
# 2.4.1 整数 整数支持加减乘除 乘方 运算次序修改
# 2.4.2 浮点数  浮点数与整数做任何运算，结果都是浮点数。 浮点数
# 2.4.3 整数和浮点数  1、两个整数相除，结果总是浮点数 2、任何运算整数和浮点数，其结果总是浮点数 3、
# 2.4.1 数中的下划线
# 2.4.5 同时给多个变量赋值
# 2.4.6 常量  在程序的整个生命周期内保持不变。python没有内置的常量。常量名必须使用全大写来指定。

print (1 + 1)
print(0.1 + 0.1)
print(0.1 + 0.2)
print(4/2.0)

universe_age = 14_000_000_00
print(universe_age)
universe_age1 = 2_00_00_0
print(universe_age1)


x, y, z = 9, 1, 2
print(x)

# 常量
MAX_NUM = 301
print(MAX_NUM)




# 练习
# 2-8 数字8
print(1+7)
print(10-2)
print(32/4)
print(2*4)
print(2 ** 3)

# 练习2-9：最喜欢的数　用一个变量来表示你最喜欢的数，再使用这个变量创建一条消息，指出你最喜欢的数是什么，然后将这条消息打印出来。

favorite_num = 301
message = f"我最喜欢的数字是：{favorite_num}"
print(message)



