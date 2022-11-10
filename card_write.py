import time
def getCList():
    return cList

########################

# TODO: Uncomment the procs, cList, as needed, and choose desired number of photons and exact process below

########################

### Uncomment these for single lepton pair amps/MEs
procs=['2lQED']
cList='cardListee'

### Uncomment these for two lepton pairs amps/MEs
# procs=['4lDiffQED', '4lSameQED']
# cList='cardList4e'

### Uncomment these for three lepton pairs amps/MEs
# procs=['6lDiffQED', '6l4Same2DiffQED']
# procs = ['eeto4muQED']
# procs =['6l4Same2DiffQED']
# cList='cardList6e'



###################

# TODO: Choose suffix of output PROC folders

###################

suffix = 'test_' + time.strftime('%Y-%m-%d_%H.%M.%S')


f = open(cList,'w')
f.close()


#####################

# TODO: Choose number of photons (a, alr) needed

#####################

naMin = 4
naMax = 4

for proc in procs:
  for na in range(naMin,naMax+1):
    # here choose type of photon
    # numPho = str(na)+'a'
    numPho = str(na) + 'alr'
    card_name = 'card_' + numPho + '_' + proc + '_' + suffix
    name = '_' + numPho + '_' + suffix
      
    #print(card_name)
    f = open(cList,'a')
    f.write(card_name+'\n')
    f.close()
    f = open('cards/'+card_name, 'w')
      
    # 2l processes
    if proc == '2lQED':
      f.write("import model cf;\ngenerate e+ e- > " + numPho + ";\noutput standalone " + proc + "/PROC" + name)
      
    # 4l processes
    if proc == '4lDiffQED':
      f.write("import model cf;\ngenerate e+ e- > mu+ mu- " + numPho + ";\noutput standalone " + proc + "/PROC" + name)
    if proc == '4lSameQED':
      f.write("import model cf;\ngenerate e+ e- > e+ e- " + numPho + ";\noutput standalone " + proc + "/PROC" + name)
    
    # 6l processes
    if proc == '6lSameQED':
      f.write("import model cf;\ngenerate e+ e- > e+ e- e+ e- " + numPho + ";\noutput standalone " + proc + "/PROC" + name)
    if proc == '6l4Same2DiffQED':
      # f.write("import model cf;\ngenerate e+ e- > 2mu+ 2mu- " + numPho + ";\noutput standalone " + proc + "/PROC" + name)
      # f.write("import model cf;\ngenerate e- mu- > 2e- mu- e+ " + numPho + ";\noutput standalone " + proc + "/PROC" + name)
      f.write("import model cf;\ngenerate e+ e- > e+ e- mu+ mu- " + numPho + ";\noutput standalone " + proc + "/PROC" + name)
    f.close()
