# a = "qwewreresadsadsad"
# print(a[0:5])
# print(a[8:-1])
# print(a[::3])
# print(a[::-2])
# print(a[-1:0:-1])
# q = "qwewreresadsadsad"
# print()
# for i in range(1, 10):
#     for j in range(1, i +1):
#         print("%d X %d = %d"%(j,i,i*j), end="\t")
#     print()

# for i in range (1,10):
#     for j in range (1, i + 1):
#         print("{} X {} = {}".format(j,i,i*j), end= "\t")
#     print()
# l = [1,5,4.6,1,3,5,4,2]
# l[0:2]= 5,6
# print(l)
l = [1,5,4,8,2,1]
# l.append("新增数据")
# l.insert(1,"新增")
# l.extend(("新增1","新增2","新增3"))
# print(l)
# print(l.pop(2))
# print(l)
# l.remove(5)
# # print(l)
# l.clear()
# print(l)
# l = []
# d = {"name":"蛮吉","age":"20","学历":"本科","地址":"上海市" }
# print(d)
# # d["name"] = "伊泽瑞尔"
# # print(d)
# d["性别"] = "男"
# print(d )

# def div(a,b):
#     try:
#         return(a/b)
#     except:
#         return
# print(div(10,20))

# try:
#     a = int(input("输入被除数："))
#     b = int(input("输入除数："))
#     c = a / b
#     print("您输入的两个数相除的结果是：", c )
# except (ValueError, ArithmeticError):
#     print("程序发生了数字格式异常、算术异常之一")
# except :
#     print("未知异常")
# print("程序继续运行")

# try:
#     result = 20 / int(input('请输入除数:'))
#     print(result)
# except ValueError:
#     print('必须输入整数')
# except ArithmeticError:
#     print('算术错误，除数不能为 0')
# else:
#     print('没有出现异常')
# print("继续执行")

# class CustomExoeption(Exception):
#     def __init__(self,value="值不能为0"):
#         self.value = value
#     def __str__(self):
#         return  self.value
# a = 1
#
# try:
#     if a ==0:
#         print("a = {} 触发异常".format(a) )
#         raise   CustomExoeption
#     print("a={} 未触发异常".format(a))
# except CustomExoeption as  e :
#     print(e)