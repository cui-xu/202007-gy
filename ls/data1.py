# from ls import  data2
# # from ls.data2 import a
# from ls.data2 import Text
#
# b = "我是data1中的变量"
# def name ():
#  print("我是DATA1文件中的方法")
#
# class Text():
#     print("我是DATA1内的class")
# print(b)
#
# print(data2.Text)

##类型转换
# a = [145]
# b= 141
# print(a+int(b))
# print(a+int(b))
#字符串转列表 元组 集合
# w = (1,2,4,5,6)
# print(set(w))

# f = open("bbb.txt","w")
# f.write("xieruneirong")
# f.close()
f = open("bbb.txt","a")
f.write("dsad\n,dasdsadas\n,dsadasdas\n,dasdasdasd\n")

f = open("bbb.txt","r")
# print (f.read(10))
# print(f.read())
# print(f.readline(1))
# print(f.readline(2))

f.close()

