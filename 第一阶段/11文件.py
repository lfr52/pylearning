# 编码 常用utf-8

# 打开-->读写-->关闭
# 1.文件的读取
# 1.1打开文件 open(name, mode, encoding)
f = open("test.txt", "r", encoding="UTF-8-sig")
print(type(f))
# 1.2读操作 文件对象.read(num)  num为读取的数据长度   文件对象.readlines()  返回列表，每一行数据为一个元素
# print(f.read(10))
# print(f.readlines())
# 文件对象.readline()  一次读取一行
# print(f.readline())
# print(f.readline())
# print(f.readline())
# for循环
for line in f:
    print(line)

# 1.3文件关闭 文件对象.close()
f.close()

# with open 语法  可以自动关闭文件
with open("test.txt", "r", encoding="UTF-8-sig") as f:
    for line in f:
        print(line, type(line))


# 2.文件的写入
# f.write()  先写到缓冲区  f.flush()  写到硬盘
# f = open("test1.txt", "w", encoding="UTF-8-sig")
# f.write("hello word!")
# # f.flush()
# f.close()
f = open("test1.txt", "w", encoding="UTF-8-sig") # 覆盖内容
f.write("黑马程序")
f.close()

# 3.文件的追加  把"w"换成"a"即可
