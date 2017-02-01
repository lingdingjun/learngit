#编写一个两两排序的函数
#通过函数两两比较

def paixu(x,y):
	if x < y:
		a = x 
		x = y
		y = a
	return x,y
		
x = int (raw_input('x:\n'))
y = int (raw_input('y: \n'))
z = int (raw_input('z:\n'))

x,y = paixu(x,y)
y,z = paixu(y,z)
x,y = paixu(x,y)
print x,y,z
