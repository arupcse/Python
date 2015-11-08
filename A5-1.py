mx = None
mn = None
while True:
	var = raw_input('Enter Number: ')
	if var == 'done': break
	elif len(var) < 1: break
	
	else:
		try:
			num = int(var)
			if mx is None or num > mx: # 'is' is exactly same in type and value
				mx = num
							
			if mn is None or num < mn: # 'is' is exactly same in type and value
				mn = num
		except:
			print 'Invalid input'
			continue
print 'Maximum is', mx 
print 'Minimum is', mn 
