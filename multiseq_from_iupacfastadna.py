#/usr/bin/python2.7

def multiseq_from_iupacfastadna(str_sequence):
	'''
	in: string with DNA sequence in IUPACK/FASTA coding
	out: list of all possible sequences
	'''
	nonstanddict = {'D':['G', 'A', 'T'], 'H':['A', 'T', 'C'], 'N':['G', 'A', 'T', 'C'], 'S':['G', 'C'], 'R':['G', 'A'], 'W':['A', 'T'], 'Y':['T', 'C'], 'K':['G', 'T'], 'M':['A', 'C'], 'V':['A', 'C', 'G']}
	ready_list = []
	start_list = []
	unamblet = 'DHNSRWYKMV'
	start_list.append(str_sequence)
	while len(start_list) > 0:
		working_seq = start_list.pop()
		check = True
		for letter in unamblet:
			if letter in working_seq:
				check = False
				pos = working_seq.find(letter)
				for i in range(0, len(nonstanddict[letter])):
					start_list.append(working_seq[:pos]+nonstanddict[letter][i]+working_seq[pos+1:])
		if check:
			if working_seq not in ready_list:
				ready_list.append(working_seq)
	return ready_list

if __name__ == "__main__":
	start_seq = 'CCANNNNNTGG'
	ready_list = multiseq_from_iupacfastadna(start_seq)
	for ele in ready_list:
		print ele


