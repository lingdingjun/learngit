#判断是否为闰年，闰年2月加1天
#判断是第几个月，前n个月的天数相加
#第n日，有n天
year = int (raw_input ('请输入年：'))
mon = int (raw_input('请输入月：'))
day = int (raw_input('请输入日：'))

mons = [31,59,90,120,151,181,212,242,273,303,334]
if mon == 1:
	dayn = day
elif mon == 2:
	dayn = 31 + day
else:
	if (year % 4 == 0) and (year % 100 != 0) or year % 400 == 0:
		dayn = mons[mon-2] + day + 1
	else:
		dayn = mons[mon-2] + day 
print dayn