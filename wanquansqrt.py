import math	#加载math模块
for i in range (1,10000):
	x=int(math.sqrt(i+100))
	y=int(math.sqrt(i+268))
	if (x*x==i+100) and (y*y==i+268):
		print i