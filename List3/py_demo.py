from os import remove

#  列表可以用一个变量来存储成千上万的数据 ，与单独的变量存在量级差异

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 列表是有序集合，根据索引即可获取索引对应的值

print(bicycles[0])

print(bicycles[0].title())

print(bicycles[-1])

message = f" This is my first bicycle : {bicycles[0].title()}"
print(message)



# 练习
# 3-1  姓名
names = ['ali','Google', 'Meta', 'Ten']

print(names)
print(names[0].title())
for name in names:
    print(name)

# 3-2 问候语
print(f"{names[0].title()} , 你好")
print(f"{names[1].title()}, 零零六年")


# 自己的列表
travel = ['bicycle', 'motorcycle', 'car', 'airpoeds']

print(f"我最喜欢的交通工具就是：{travel[1].upper()}")
print(f"我最喜欢的交通工具就是：{travel[1].lower()}")
print(f"我最喜欢的交通工具就是：{travel[1].title()}")


# 3.2.1 修改列表元素

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# 3.2.2 在列表中添加元素
# append（）  方法 ： 你可以在已有数据的列表中进行追加数据 2、 你也可以在空列表中进行追加数据内容

motorcycles = ['hhhh']
motorcycles.append('gggg')
print(motorcycles)


m2 = []
m2.append('1211')
print(m2)
# insert 在列表中插入数据  使用insert（）可以在列表的任意位置进行插入数据  使用索引指定位置即可

m3 = ["1",'2', '4']
m3.insert(2, 3)
print(m3)

# 3.2.3 从列表中删除元素
# 我们经常需要从列表中删除一个或者多个元素，比如用户注销那就要把用户的数据进行清空，可以根据用户在列表中的位置来进行删除。
# del m4[2]
m4 = [1, 2, 3, 4, 5]
print(m4)
del m4 [1]
print(m4)

# pop()方法  可以用来删除列表末尾的元素
print("__________________________________________")
m5 = [1, 2, 3, 4, 5]
print(m5)

popped_m5 = m5.pop()
print(m5)
print(popped_m5)

popped_m5_1 = m5.pop(3)
print(popped_m5_1)
print(m5)

print(f"My favorite number is： {m5.pop(0)}")
print(m5)
    # 根据值进行删除   remove()

print("____________________________")
m6 = [215, 5645, 3, 223, 565]

print(m6)
m6.remove(215)
print(m6)















































