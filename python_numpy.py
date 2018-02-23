# _*_coding:utf-8-*_
import numpy as np  
# 定义矩阵变量并输出变量的一些属性
# 用np.array()生成矩阵
arr=np.array([[1,2,3],
              [4,5,6]])  

print(arr)
print('number of arr dimensions: ',arr.ndim)
print('~    ~    ~   shape: ',arr.shape)
print('~    ~    ~   size: ', arr.size)

# 输出结果：
[[1 2 3]
 [4 5 6]]
number of arr dimensions:  2
~    ~    ~   shape:  (2, 3)
~    ~    ~   size:  6  

# 定义一些特殊矩阵
# 指定矩阵数据类型
arr=np.array([[1,2,3],
              [4,5,6]],
              dtype=np.float64) # 我的电脑np.int是int32，还可以使用np.int32/np.int64/np.float32/np.float64
print(arr.dtype)

# 用np.zeros()生成全零矩阵
arr_zeros=np.zeros( (2,3) )
print(arr_zeros)

# 用np.ones()生成全一矩阵
arr_ones=np.ones( (2,3) )
print(arr_ones)

# 生成随机矩阵np.random.random()
arr_random=np.random.random((2,3))
print(arr_random)

# 用np.arange()生成数列
arr=np.arange(6,12)
print(arr)

# 用np.arange().reshape()将数列转成矩阵
arr=np.arange(6,12).reshape( (2,3) )
print(arr)

# 用np.linspace(开始，结束，多少点划分线段)，同样也可以用reshape()
arr=np.linspace(1,5,3)
print(arr)

# 矩阵运算
arr1=np.array([1,2,3,6])
arr2=np.arange(4)

# 矩阵减法，加法同理
arr_sub=arr1-arr2
print(arr1)
print(arr2)
print(arr_sub)

# 矩阵乘法
arr_multi=arr1**3 # 求每个元素的立方，在python中幂运算用**来表示
print(arr_multi)

arr_multi=arr1*arr2 # 元素逐个相乘
print(arr_multi) 

arr_multi=np.dot(arr1, arr2.reshape((4,1))) # 维度1*4和4*1矩阵相乘
print(arr_multi)

arr_multi=np.dot(arr1.reshape((4,1)), arr2.reshape((1,4))) # 维度4*1和1*4矩阵相乘
print(arr_multi)

arr_multi=arr1.dot(arr2.reshape((4,1))) # 也可以使用矩阵名.doc(矩阵名)
print(arr_multi)

# 三角运算：np.sin()/np.cos()/np.tan()
arr_sin=np.sin(arr1)
print(arr_sin)

# 逻辑运算
print(arr1<3) # 查看arr1矩阵中哪些元素小于3，返回[ True  True False False]

# 矩阵求和，求矩阵最大最小值
arr1=np.array([[1,2,3],
               [4,5,6]])
print(arr1)
print(np.sum(arr1)) # 矩阵求和
print(np.sum(arr1,axis=0)) # 矩阵每列求和
print(np.sum(arr1,axis=1).reshape(2,1)) # 矩阵每行求和

print(np.min(arr1)) # 求矩阵最小值
print(np.min(arr1,axis=0))
print(np.min(arr1,axis=1))

print(np.max(arr1)) # 求矩阵最大值

print(np.mean(arr1)) # 输出矩阵平均值，也可以用arr1.mean()
print(np.median(arr1)) # 输出矩阵中位数

# 输出矩阵某些值的位置
arr1=np.arange(2,14).reshape((3,4))
print(arr1)

print(np.argmin(arr1)) # 输出矩阵最小值的位置，0
print(np.argmax(arr1)) # 输出矩阵最大值的位置，11

print(np.cumsum(arr1)) # 输出前一个数的和，前两个数的和，等等
print(np.diff(arr1)) # 输出相邻两个数的差值

arr_zeros=np.zeros((3,4))
print(np.nonzero(arr_zeros)) #输出矩阵非零元素位置，返回多个行向量，第i个行向量表示第i个维度
print(np.nonzero(arr1))

print(np.sort(arr1)) # 矩阵逐行排序
print(np.transpose(arr1)) # 矩阵转置，也可以用arr1.T

print(np.clip(arr1,5,9)) #将矩阵中小于5的数置5，大于9的数置9  

# numpy索引
arr1=np.array([1,2,3,6])
arr2=np.arange(2,8).reshape(2,3)

print(arr1)
print(arr1[0]) # 索引从0开始计数

print(arr2)
print(arr2[0][2]) # arr[行][列]，也可以用arr[行,列]
print(arr2[0,:]) # 用:来代表所有元素的意思
print(arr2[0,0:3]) # 表示输出第0行，从第0列到第2列所有元素
                   # 注意python索引一般是左闭右开

# 通过for循环每次输出矩阵的一行
for row in arr2:
    print(row)

# 如果要每次输出矩阵的一列，就先将矩阵转置
arr2_T=arr2.T
print(arr2_T)
for row in arr2_T:
    print(row)

# 将矩阵压成一行逐个输出元素
arr2_flat=arr2.flatten()
print(arr2_flat)

for i in arr2.flat: # 也可以用arr2.flatten()
    print(i)

# 矩阵合并与分割  
# 矩阵合并
arr1=np.array([1,2,3,6])
arr2=np.arange(4)
arr3=np.arange(2,16+1,2).reshape(2,4)
print(arr1)
print(arr2)
print(arr3)

arr_hor=np.hstack((arr1,arr2)) # 水平合并，horizontal
arr_ver=np.vstack((arr1,arr3)) # 垂直合并，vertical
print(arr_hor)
print(arr_ver)

# 矩阵分割
print('arr3: ',arr3)
print(np.split(arr3,4,axis=1)) # 将矩阵按列均分成4块
print(np.split(arr3,2,axis=0)) # 将矩阵按行均分成2块
print(np.hsplit(arr3,4)) # 将矩阵按列均分成4块
print(np.vsplit(arr3,2)) # 将矩阵按行均分成2块
print(np.array_split(arr3,3,axis=1)) # 将矩阵进行不均等划分  

# numpy复制：浅复制，深复制  
# 浅复制
arr1=np.array([3,1,2,3])
print(arr1)
a1=arr1
b1=a1
# 通过上述赋值运算，arr1,a1,b1都指向了同一个地址（浅复制）
print(a1 is arr1)
print(b1 is arr1)
print(id(a1))
print(id(b1))
print(id(arr1))

# 会发现通过b1[0]改变内容，arr1,a1,b1的内容都改变了
b1[0]=6
print(b1)
print(a1)
print(arr1)

# 深复制
arr2=np.array([3,1,2,3])
print('\n')
print(arr2)
b2=arr2.copy() # 深复制，此时b2拥有不同于arr2的空间
a2=b2.copy()
# 通过上述赋值运算，arr1,a1,b1都指向了不同的地址（深复制）
print(id(arr2))
print(id(a2))
print(id(b2))
# 此时改变b2,a2的值，互不影响
b2[0]=1
a2[0]=2
print(b2)
print(a2)
print(arr2)
