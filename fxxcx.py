def f(x):	if x==0:		return x	else:		return f(x-1)*2+x*x x = int(raw_input ('请输入x：'))	#需要用int，否则为strprint f(x)