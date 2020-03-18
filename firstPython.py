""""
docstring
"""
import sys


def fib(n):
    a, b, c = 0, 1, 0
    while a < n:
        # print(a, end=' ')
        a, b = b, a + b
        c = c + 1
        print("a:", a, "b:", b, "c:", c)
    print("你好！！！")


fib(10)


# 测试range函数
str1 = range(1, 9)
print(str1.index(3))  # value=3的index为2

str2 = range(1, 9, 2)
print(str2.index(3))  # value=3的index为1

# sort dictionary
D = dict(name='xixibaishui', job='IT', gender='male', age=31)
for x in D.keys():
    print(x, '=>', D[x])

D3 = {}
x1 = [x for x in D]
x1.sort()  # 利用列表的排序对字典排序
# 20200318:python增加了内置函数sorted,此函数可对字典的keys排序，而不必再通过如上的列表转换

for x3 in x1:
    print(x3, D.get(x3))
    D3.setdefault(x3, D.get(x3))

print(D3)

# 20170526:jinzi:利用x1.sort后可直接通过set赋值字典,而不必使用for循环:不对set赋值后是set而非字典
D4 = set(x1)
print(D4)  # set赋值后是set而非字典:{'age', 'gender', 'job', 'name'}

#  集合可以交/并/加/减
set1 = set(D.keys())
set2 = set1.copy()
set2.pop()
set2.pop()
set2.update(set(D.values()))
print('set1:=>', set1)
print('set2:=>', set2)

print(set1 & set2, set1 | set2)  # python不支持+
print(set1 - set2)
print(set2 - set1)

# enumerate枚举函数:字符串，列表，字典，set集合及元组
str1 = 'xixibaishui'
list1 = ['aa', 'bb', 'cc', 'dd', 'd', 'd', 'd']
dict1 = {'name': 'Xixibaishui', 'job': 'IT', 'gender': 'male', 'age': 31}  # 默认只枚举字典的key

# 字符串
print('字符串--------------------------')
for k, v in enumerate(str1):
    print(k, v)

# 列表
print('列表--------------------------')
for k, v in enumerate(list1):
    print(k, v)

# 字典(默认只枚举key)
print('字典--------------------------')
for k, v in enumerate(dict1):
    print(k, v)

for k, v in enumerate(dict1.values()):
    print(k, v)

# set集合
print('set集合--------------------------')
for k, v in enumerate(set(str1)):
    print(k, v)
for k, v in enumerate(set(list1)):
    print(k, v)

# 元组
print('元组--------------------------')
for k, v in enumerate(tuple(str1)):
    print(k, v)

for k, v in enumerate(tuple(list1)):
    print(k, v)

# 20170529:十进制,八进制与十六进制
int('0100'), int('0100', 8), int('0100', 16)  # int可把字符串转化为指定进制的数字

print("%o %x %X" % (64, 64, 255))  # 十进制数字转化为指定进制
# 小数类型 from decimal import Decimal

# 20170531
# 类型属于以对象而非变量
# 共享引用和在原处修改:列表/字典等在原处修改不仅仅修改本身变量，其共享引用的变量也会被修改
# 如何破解：切片/copy/import copy


# 字符串
# 二进制转换为十进制1
B = '1101'
I = 0
while B:
    # I = I * 2 + (ord(B[0]) - ord('0'))
    I = I * 2 + int(B[0])
    print(I, B)
    B = B[1:]
print(I, B)

# 二进制转换为十进制2
B2 = '1101'
I1 = 0
I2 = I1
while B2:
    I2 = I2 + int(B2[-1]) * (2 ** I1)
    print(I2)
    I1 += 1
    print(I1)
    B2 = B2[:-1]
    print(B2)
print(I1, I2, B2)

# 20170601:jinzi:元组:本身不含方法，可通过列表对其排序
t1 = 'efg', 'cd', 'ab'
tmp = list(t1)
tmp.sort()
t1 = tuple(tmp)
print(t1)

# 元组的列表解析list comprehension
t2 = (1, 4, 7, 2, 5, 8)
list2 = [x ** 2 + x for x in t2]
d3 = {x: x ** 2 + x for x in t2}
t3 = (x ** 2 + x for x in t2)
print('列表====>', list2)
print('字典====>', d3)
print('元组====>', t3)
# 列表====> [2, 20, 56, 6, 30, 72]
# 字典====> {1: 2, 4: 20, 7: 56, 2: 6, 5: 30, 8: 72}
# 元组====> <generator object <genexpr> at 0x00000148DA6C6938>

# 为何元组未成功解析？经查询，原因为：generator comprehension
t4 = tuple(x ** 2 + x for x in t2)  # 列表解析的结果默认都是列表，所以需使用tuple转换之
print('元组2====>', t4)

"""
列表解析是名副其实的序列操作--它们总会创建新的列表，但也可以用于遍历包括元组、字符串以及其他列表在内的任何序列对象。
列表解析甚至可以用在某些实际并非储存的序列之上--任何可遍历的对象都可以，包括可自动逐行读取的文件
"""

# 交互
while True:
    reply = input('Enter whatever you want:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('What you enter [', reply, ' ] is not digit,please reEnter')
    else:
        print(int(reply) ** 2)
print('Bye')

# 20170602 循环
# 同一个结果的不同循环形式
# 1:while
x = 'spam'
while x:
    print('while=====>', x)
    x = x[1:]

# 2 for
x = 'spam'
for y in range(4):
    print('for=====>', x[y:])

# 根据输入的数字判断是否是质数
list3 = []

while True:
    is_prime = input('Enter your num,so we can judge whether it\'s a prime\n')
    if not is_prime.isdigit():
        print('What you Enter is not a digit,reenter please!')
    else:
        break

xx = int(is_prime) // 2
while xx > 1:
    if int(is_prime) % xx == 0:
        print(is_prime, 'has the factor ', xx)
        list3.append(xx)
    xx -= 1

if len(list3) > 0:
    print(is_prime, 'has factors as follows:', list3)
else:
    print(is_prime, ' is a prime')

# 注意while中的else:除非while与else间含break，否则无论while执行几遍(即使0遍)，else部分也会执行

# 20170605：循环总结
"""
循环大致分为:while循环,for循环,迭代,列表解析等
1:while循环
while <test>:
    statement1
else:
    statement2
其中，
else语句是可选的；
若statement语句中含break,则会直接跳出while循环，且不会执行else语句，否则一定会执行else语句；
continue：跳至最近循环所在的开头(即不再执行此次循环的后续语句)
pass:什么都不做，只是空占位语句


2:for循环
同while一样，可遍历任何有序的序列对象内的元素(字符串，列表，元组，其他内置可迭代对象等)


3:迭代
for循环，列表解析，in成员关系测试及map内置函数等:可迭代对象包括实际序列及按需求而计算的虚拟序列
文件迭代器：next()
对象内置迭代器：如字典等，含内置迭代器
map，zip，range等内置函数（其中range可实现非完备遍历）
sorted,sum,any,all,list,tuple,''.join等内置工具
用户自定义迭代器
并行遍历：zip和map可实现并行遍历
enumerate:偏移与元素兼得


4:列表解析
虽然结果可能与for循环语句等相同，但列表解析却是创建了新的列表对象(若原始列表有多个引用值)
语句简明，且比手工的for循环等要快，效率更高
另，列表解析可扩展为多个for循环且每个for循环均可添加if判断语句

"""


# 20170605 函数
def intersect(seq1, seq2):
    ret = []
    for x in seq1:
        if x in seq2:
            ret.append(x)
    return ret

print(intersect('asdf','fghj'))
print(intersect('12345','54321'))


# 20170606:jinzi:python关键字:import keyword;keyword.kwlist:列表
# import keyword
# for x,y in enumerate(keyword.kwlist):
#     print('Num ', x + 1, '==>', y)



# 20170606 作用域与参数
# sys.modules背景
# for x in sys.modules:  # sys.modules是一个dict
#     print(x, '=====>', sys.modules[x])

"""
变量名解析规则：LEGB 本地->函数内->全局->内置，其中内置作用域可通过import __builtin__可看

最小化全局变量：函数内声明全局变量会导致变量值的不可控，因为变量值取决于函数调用的顺序，而函数是任意顺序排列的，这样就会引起程序调试困难

最小化文件修改：一个模块一旦被导入，其全局变量就变成了此模块的属性，导入者自动获得了被导入模块的所有全局变量的访问权，
    此时若变更其属性(如赋值等操作)，实际上就是修改了被导入模块的全局变量，而其他人在维护被导入模块时，根本不会知晓会有其它地方修改了其全局变量

其它访问全局变量的方法：见part1:“ThisMod”

作用域与嵌套函数：见part2/part3
"""

# part1:通过import ThisMod，测试各类访问全局变量的方法:
# 1 直接声明global;2 import自身;3 import sys，然后赋值sys.modules[modules_name]给变量
import ThisMod
ThisMod.test()
print(ThisMod.var)


# part2:作用域与嵌套函数：嵌套作用域
def f1():
    x = 123

    def f2():
        print(x)
    f2()    # 此处f1直接调用f2
# 若在此处调用f1，f1会调用f2，从而直接打印出x的值


def f1():
    x = 123

    def f2():
        print(x)
    return f2   # 此处f1返回f2而非直接调用
# 若在此处调用f1，f1会返回f2，必须再次调用才会打印出x的值：即f1()()



# part3:工厂函数:一个能记住嵌套作用域的值的函数，尽管那个作用域或许已不存在
def maker(m):

    def action(n):
        print(n ** m)
    return action   # 返回嵌套的函数却不调用此函数

f = maker(2)    # 赋值m=2
f(3);f(5);f(7)  # 分别传参3,5,7给嵌套函数action:此函数已记住m=2

g = maker(3)    # 赋值m=2
g(3);g(5);g(7)  # 分别传参3,5,7给嵌套函数action:此函数已记住m=3


# part4:默认参数
# 默认传值给嵌套的函数：def f2(x=x)
# 但仍尽量避免使用嵌套函数，或拆分嵌套函数


# part5 嵌套作用域与lambda
# lambda:匿名函数/行表达式函数
# 1 python lambda会创建一个函数对象，但不会把这个函数对象赋给一个标识符，而def则会把函数对象赋值给一个变量。
# 2 python lambda它只是一个表达式，而def则是一个语句。

# 若def或lambda嵌套在一个循环中，且引嵌套引用了上层作用域的变量，变量被循环所改变，在这个循环中产生的函数均会有相同的值：最后一次循环完成时引用变量的值
def func1():
    list4 = []
    for i in range(5):
        list4.append(lambda x:i ** x)
    return list4

ff = func1()    # 赋值给ff,同时传值ff.x=2
for i in range(5):
    print(i, '==>', ff[i](2))   # 注意此处的格式：ff[i](2):赋值的2是在最后的
# 结果：所有的节点的值均为引用最后一次循环的变量的值
# 如何破解？lambda中传值默认参数即可:list4.append(lambda x, i=i:i ** x)

# 或者,map+lambda破之
def func2(times):
    map1 = map(lambda x:x ** times,range(5))    # 破之
    return map1

for x in func2(3):
    print(x)


# 20170607:传递参数
# 参数的传递是通过自动将对象赋值给本地变量来实现的
# 在函数内部的参数名的赋值不会影响调用者
# 改变函数的可变对象参数的值也许会对调用者有影响：譬如有些参数涉及共享引用，此时应注意拷贝传参等

# part1:特定的参数匹配模型：
# 位置：从左至右进行匹配
# 关键字参数：通过参数名进行匹配
# 默认参数：为没有传入值的参数定义默认值
# 可变参数：分为函数定义参数和调用传参两类：
#       1 函数定义：收集任意多基于位置或关键字的参数
#       2 调用传以参：传递任意多基于位置或关键字的参数


# 任意参数实例： *对应元组，**对应字典
arg1 = (1, 3, 2, 4)
arg2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


def f(a, *b, **c):  # 参数顺序：元组必须在字典前？？？
    print(a,b,c)

f(0, *arg1, *arg2)
f(*arg1, **arg2)
f(**arg2)   # 为何不能成功调用
# 注意以下情况
f(*arg1)                # 1 (3, 2, 4) {}:此处把1补充给了x,剩余的值给了y
f(0, 0, *arg1, **arg2)  # 0 (0, 1, 3, 2, 4) {'a': 1, 'b': 2, 'c': 3, 'd': 4}:把第2个0并入了y
f(*arg1, 0, *arg1, 0)    # 1 (3, 2, 4, 0, 1, 3, 2, 4, 0) {}:注意(！！！)查看结果
# f(*arg1, 0, *arg1, **arg2,0)  #但**后是不能再接一般参数的(SyntaxError: positional argument follows keyword argument unpacking)
f(*arg1, 0, *arg1, *arg2, 0, **arg2, **{'e':5}) # 1 (3, 2, 4, 0, 1, 3, 2, 4, 'a', 'b', 'c', 'd', 0) {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

"""
参数匹配细节：
若使用并法例特定的参数匹配模型，Python遵循以下顺序法则
1:在函数调用中，所有的非关键字参数(name)必须首先出现，其后跟随所有的关系字参数(name=value)，
    后面跟*name的形式，如果有需要的话，最后是**name
2:在函数头部，参数必须以相同的顺序出现：一般参数，默认参数，*name，**name

Python内部按以下步骤在赋值前进行参数匹配：
1:通过位置分配非关键字参数
2:通过匹配变量名分配关键字参数
3:其他额外的非关键字参数分配到*name元组中
4:其他额外ide关键字分配到**name字典中
5:用默认值分配给在头部未得到分配的参数
"""


# part2:处理可变参数，以取得最小参数为例 min1,min2,min3
def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res


def min2(first, *rest): # 注意：此处为两个参数，第1个相当于min1中的args[0]，第2个相当于args[1:]
    for arg in rest:
        if arg < first:
            first =arg
    return first


def min3(*args):
    tmp = list(args)    # 直接把元组参数转为List，然后使用了list的sort函数
    tmp.sort()
    return tmp[0]


# 更进一步，把min,max函数作为一个参数传给函数
def minmax(min_max, *args):
    tmp = args[0]
    for arg in args[1:]:
        if not min_max(tmp,arg):    # 或者：if min_max(arg,tmp):
            tmp = arg
    return tmp


def min_x(x, y):return x < y
def max_x(x, y):return x > y


# 20170608:函数的高级话题
# 1:匿名函数lambda ：lambda argument1,argument2,...,argumentN:expressions using arguments
lam1 = (lambda x='hi ', y='i\'m ', z='lambda':x + y + z)    # lambda语句中可有默认值
lam1()  # hi i'm lambda
lam1('hello')   # hello i'm lambda
# lambda的功能总可以使用def来替换，但lambda直到了函数速写的作用，可使执行代码更简洁；lambda是表达式而非语句，故可用在不能使用def的地方(如列表解析等)

# lambda嵌套和作用域：lambda能获得任意上层lambda变量：但要尽量避免嵌套!!!!!!
action1 = (lambda x:(lambda y: x ** y)) # 1层嵌套
action1(2)(3)   # 2 ** 3 =8

action2 = (lambda x:(lambda y:(lambda z: x * (z + y))))     # 2层嵌套
action2(2)(3)(4)    # 2 * (3 + 4) =14


# 2:作为参数来应用函数：apply函数：apply(func,args):即预先并不清楚func可能的参数数量,故apply第2个参数为func的参数元组
# apply执行单个函数的调用，把参数传入该函数，只进行一次。而map会替序列中每个元素都调用函数，进行多次
# apply函数在Python3已取消了


# 3:在序列中映射函数：map：仍保留在Python3.5中
# map(func, seq):其中，func可被lambda替换


# 4:函数式编程工具：filter和reduce:filter仍在用，reduce已取消
filter((lambda x:x > 0),range(-5,5))  # 从(-5,-4,-3,-2,-1,0,1,2,3,4)中滤出>0的元素
# reduce((lambda x,y:x + y),[1,2,3,4])  # 累加列表元素
# reduce((lambda x,y:x * y),[1,2,3,4])  # 累乘列表元


# 5:重访列表解析：映射
# [x ** 2 for x in range(10) if x % 2 ==0]
# for xxxx in map((lambda xxx: xxx ** 2), filter((lambda xxx: xxx % 2 == 0), range(10))):
#     print(xxxx)

# 6:增加测试和嵌套循环
# 7:列表解析和矩阵
# 8:重访迭代器：生成器
# 9:函数设计概念
# 10:函数陷阱