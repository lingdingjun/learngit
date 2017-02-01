#排序x,y,z   int,raw_input
#x与y比较，大的变成x。
#y与z比较，小的变成z。
#x再与y进行比较。

x = int (raw_input('x:\n'))
y = int (raw_input('y: \n'))
z = int (raw_input('z:\n'))

if x > y:
	if y < z:
		a = y
		y = z
		z = a
		if x < y:
			a = x 
			x = y
			y = a
else:
	a = x
	x = y
	y = a
	if y < z :
		a = y
		y = z 
		z = a 
		if x < y:
			a = x 
			x = y
			y = a
print x,y,z 
