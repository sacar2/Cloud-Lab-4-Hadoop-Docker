def mapper():
	for line in sys.stdin:
		data = line.strip().split(“\t”) # strip whitespaces then split on tab delimiters
		#CHECK IF LINE HAS 6 FIELDS
		if len(data) == 6:
			date, time, store, item, cost, payment = data # assign data into vars
			print “{0}\t{1}”.format(store, cost)

