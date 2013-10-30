"""
idea = using lists of nuc_seq with separate nucl as lists ['G'], ['A'] etc.
each round we look at unamb nucl - count lenth of this letter in dict{'D'=[['A'],['G'], ['T'], ..}
and multiply starting lists to the len(dict['D']) and appending letter-lists from dict
at the end all lists are joining with ''.join()

restrictase = they have to be palindromes
[ [['C'], ['T'], ['C'], ['G'], ['G'], ['G']]
  [['C'], ['C'], ['C'], ['G'], ['G'], ['G']]
  [['C'], ['T'], ['C'], ['G'], ['A'], ['G']]
  [['C'], ['C'], ['C'], ['G'], ['A'], ['G']]
]

"""

#nonstanddict = {['D']:[['G'], ['A'], ['T']], ['H']:[['A'], ['T'], ['C']], ['N']:[['G'], ['A'], ['T'], ['C']], ['S']:[['G'], ['C']], ['R']:[['G'], ['A']], ['W']:[['A'], ['T']], ['Y']:[['T'], ['C']]}
nstanddict = {'D':[['G'], ['A'], ['T']], 'H':[['A'], ['T'], ['C']], 'N':[['G'], ['A'], ['T'], ['C']], 'S':[['G'], ['C']], 'R':[['G'], ['A']], 'W':[['A'], ['T']], 'Y':[['T'], ['C']], 'A':['A'], 'G':['G'], 'C':['C'], 'T':['T']}


start_seq = 'CYCGRG'

def prepare_seq_list(string):
	'''
	converting 'AGTCAG' to [['A'], ['G'] ...] list
	'''
	result = []
	for char in string:
		result.append([char])
	return result

start_list = prepare_seq_list(start_seq)
print start_list

def multisequence(list_seq):
	result = [[], [], [], [], [], []]
	for element in list_seq:
		for i in range(0, len(nstanddict[element])):
			result[i].append([element])
	return result

res_list = multisequence(start_seq)
print res_list