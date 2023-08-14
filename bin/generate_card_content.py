gluons = ['gl', 'gr']
initial_gluons = ['gli','gri']
quarks = ['tM','tP']
anti_quarks = ['tM~','tP~']
up = ['ul', 'ur']
anti_up = ['ul~', 'ur~']

stringlist = []

for a in range(2):
	for b in range(2):
		for c in range(2):
			for d in range(2):
				for e in range(2):
					for f in range(2):
						for g in range(2):
							stringlist.append(quarks[a] + ' ' + anti_quarks[b] + ' > ' + gluons[c] + ' ' + gluons[d] + ' ' + gluons[e] + ' ' + gluons[f] + ' ' + gluons[g])
					
final_stringlist = []

for string in stringlist:
	placed_left_initial = False
	placed_right_initial = False
	new_string = ''
	for particle in string.split(' '):
		if not placed_left_initial and particle == 'gl':
			new_string += 'gli '
			placed_left_initial = True
		elif not placed_right_initial and particle == 'gr':
			new_string += 'gri ' 
			placed_right_initial = True
		else:
			new_string += particle + ' '
	final_stringlist.append(new_string)
	
i = 0
print('import model gauge_cf')
for string in final_stringlist:
	if i == 0:
		print('generate ' + string)
		i += -1
	else:
		print('add process ' + string)
		
print('output standalone')
print('launch')
