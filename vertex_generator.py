gluons = ['g','gLI','gRI','gL','gR']
tops = ['tM', 'tP','t']
antitops = ['tM__tilde__', 'tP__tilde__', 't__tilde__']
part_to_name_dict = {'g': 'N_g', 'gLI': 'N_gli', 'gRI': 'N_gri', 'gL': 'N_gl', 'gR': 'N_gr', 'tM': 'N_tm', 'tP': 'N_tp', 't': 'N_t', 'tM__tilde__': 'N_tm_bar','tP__tilde__': 'N_tp_bar', 't__tilde__': 'N_t_bar'}
n = len(gluons)

vertex = 99
for i in range(3):
	for j in range(3):
		for k in range(5):
			#print("V_" + str(vertex) + " = Vertex(name = 'V_" + str(vertex) + "', \n\t\t particles = [ P."+str(antitops[i])+", P."+str(tops[j])+", P."+str(gluons[k])+" ],\n\t\t color = [ 'T(3,2,1)' ], \n\t\t lorentz = [ L.FFV1 ], \n\t\t couplings = {(0,0):C.GC_11})")
			
			print("if " + part_to_name_dict[antitops[i]] + " == 1 and " + part_to_name_dict[tops[j]] +" == 1 and " + part_to_name_dict[gluons[k]] + " == 1:\n\t\t lastvx.set('id', " + str(vertex) +  ")")
			vertex += 1	



					#print("V_" + str(vertex) +" = Vertex(name = 'V_" + str(vertex) + "',\n\tparticles = [ P." + gluons[i] + ", P." + gluons[j] + ", P." + gluons[k] + ", P."+ gluons[l] + "],\n\tcolor = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],\n\tlorentz = [ L." + Lorentz +"1, L." + Lorentz +"3, L." + Lorentz + "4 ],\n\tcouplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})")

