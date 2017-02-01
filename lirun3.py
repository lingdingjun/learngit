l = int (raw_input ('shu ru:'))
lilv = [0.01,0.015,0.03,0.05,0.075,0.1]
benjin = [100,60,40,20,10,0]
r=0
for idx in range (0,6):
	if l > benjin[idx]:
		r += lilv[idx]*(l-benjin[idx])
		l=benjin[idx]
	print r
