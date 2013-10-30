#/usr/bin/python27

def bairoch_to_list(file_name):
	fr = open(file_name, 'rU').readlines()
	restrictname = []
	sitenuc = []
	for element in fr:
		if element[0:2] == 'ID':
			list = element.split()
			restrictname.append(list[1])
		if element[0:2] == 'RS':
			list = element.split()
			sitenuc.append(list[1][:-1])
	return restrictname, sitenuc

restrictname, sitenuc = bairoch_to_list('lab_restrictases_all.bairoch')
merge = zip(restrictname, sitenuc)
allsites = ''.join(sitenuc)
newdict = {}
for letter in allsites:
	try:
		newdict[letter] += 1
	except:
		newdict[letter] = 1
print newdict


#D = G A T (all but C)
#H = A C T (all but G)
#N = A G T C
#S = G C (strong bonds)
#R = G A (purine)
#W = A T (weak bonds)
#Y = T C (pyrimidine)
nonstanddict = {'D':['G', 'A', 'T'], 'H':['A', 'T', 'C'], 'N':['G', 'A', 'T', 'C'], 'S':['G', 'C'], 'R':['G', 'A'], 'W':['A', 'T'], 'Y':['T', 'C']}


good_restr = []
bad_restr = []
strange_dna = ['D', 'H', 'N', 'S', 'R', 'W', 'Y']
for restline in merge:
	check = True
	for letter in strange_dna:
		if check:
			if letter in restline[1]:
				bad_restr.append(restline)
				check = False
	if check:
		good_restr.append(restline)

print bad_restr
print good_restr
		