def reducer():
	totalSales = 0
	prevKey = None
	
	for line in sys.stdin:
		data = line.strip().split(“\t”) # strip whitespaces then split on tab delimiters
		if len(data) != 2: #expecting value and key, so expect only 2 items
			continue
		currKey, currSale = data #store key and value into variables

		if prevKey and prevKey!= thisKey: # if this isn’t the very first key & old!=current …
			print “{0}\t{1}”.format(prevKey,salesTotal) #… key just changed so print rslt 4 store
			salesTotal = 0 #reset sales total
		prevKey = currKey #prev key is the current key 
		totalSales += float(currSale) #add sale to running total
	
	if oldKey !=None: #if we’re on the very last line of data
		print “{0}\t{1}”.format(prevKey, totalSales)
