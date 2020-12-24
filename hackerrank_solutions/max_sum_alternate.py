def find_max_sum(arr): 
	incl = 0
	excl = 0
	
	for i in arr: 
		
		# Current max excluding i
		new_excl = max(excl,incl)
		
		# Current max including i 
		incl = excl + i 
		excl = new_excl 
	
	# return max of incl and excl 
	return max(excl,incl)
