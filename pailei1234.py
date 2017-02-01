for x in range(1,5):
	for y in range(1,5):
		for z in range(1,5):
			if (x!=y) and (y!=z) and (z!=x):
				print 100*x+10*y+z