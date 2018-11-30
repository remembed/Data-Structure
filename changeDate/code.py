#encoding=utf-8
#传址调用：
def change(data):
        data[0],data[1]=data[1],data[0]
        print('函数内交换位置后')
        for i in range(2):
                print('data[%d]=%3d'%(i,data[i]))
#主程序
data=[16, 25]
print('原始数据为：')
for i in range(2):
        print('data[%d]=%3d' %(i,data[i]))
print('\n----------------------------------------')
change(data)
print('\n----------------------------------------')
print('排序后数据为：')
for i in range(2):
        print('data[%d]=%3d' %(i,data[i]))
#传值调用：
def fun(a,b):
    a,b=b,a
    print('函数内交换数值后：a=%d,\tb=%d\n'%(a,b))

a = 11
b = 21
print('调用函数前的数值：a=%d,\tb=%d\n'%(a,b))
#调用函数
print('\n-----------------------------------')
fun(a,b)
print('\n-----------------------------------')
print('调用函数后的数值：a=%d,\tb=%d\n'%(a, b))
