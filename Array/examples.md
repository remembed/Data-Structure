一、一维数组的例题：
1、假设A为一个具有1000个元素的数组，每个元素为4个字节的实数，若A[500]的位置为1000（16进制的），请问A[1000]的地址为多少？
解答：先把16进制的1000转换为10进制的=1×16^3+0×16^2+0×16^1+0×16^0=4096
注意：知识点（16进制转换为10进制）：给个位数×16的零次方，十位数×16的一次方，百位数×16的二次方，以此类推。
2、有一个PASCAL数组A:ARRAY[6..99]of REAL(假设REAL元素占用的内存空间大小为4)，如果已知数组A的起始地址为500，那么元素A[30]的地址是多少？
解答：Loc(A[30])=A(Loc[6])+(30-6)x4=500+96=596
二、二维数组的例题：
1、现有一个二维数组A，有3×5个元素，数组的起始位址A(1,1)是100，以行为主存储，每个元素占2个字节的内存空间，请问A(2,3)的地址是多少？
解答:直接代入公式，Loc(A(2,3))=100+(2-1)×5×2+(3-1)×2=114 {100为起始位置，2是所求数组的行，1是起始行，5是总列数，
2是每个元素站占得字节，3是所求数组的列，1是起始列，2是每个元素站占得字节}
2、A(-3:5,-4:2)起始地址A(-3,-4)=1200,以行为主存储，每个元素占1个字节的内存空间，请问A(Loc(1,1))的值为多少？
解答：假设A数组以行为主存储，且α=Loc(A(3,4))=1200,m=5-(-3)+1=9(行)，n=2-(-4)+1=7(列)，则A(1,1)=1200+1×7×(1-(-3))+1×(1-(-4))=1233
