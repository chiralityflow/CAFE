def getCList():
    return cList

def getFList():
    return fList

########################

# TODO: Uncomment the procs, cList, fList as needed, and choose desired number of gluons/colour orders below

########################

### Uncomment these for single lepton pair amps/MEs
# procs=['2lQED']
# cList='cardListee'
# fList='folderListee'

### Uncomment these for two lepton pairs amps/MEs
procs=['4lDiffQED', '4lSameQED']
cList='cardList4e'
fList='folderList4e'

### Uncomment these for three lepton pairs amps/MEs
# procs=['6lDiffQED', '6l4Same2DiffQED']
# cList='cardList6e'
# fList='folderList6e'



###################

# TODO: Choose suffix of output PROC folders

###################

suffix = 'test_220105'


f = open(cList,'w')
f.close()
f = open(fList,'w')
f.close()


#####################

# TODO: Choose number of photon (a) needed

#####################

naMin = 2
naMax = 3

for proc in procs:
  for na in range(naMin,naMax+1):
    folders = []
    numPho = str(na)+'a'
    card_name = 'card_' + numPho + '_' + proc + '_' + suffix
    name = numPho + '_' + suffix
      
    #print(card_name)
    f = open(cList,'a')
    f.write(card_name+'\n')
    f.close()
    f = open('cards/'+card_name, 'w')
      
    # 2l processes
    if proc == '2lQED':
      f.write("import model cf;\ngenerate e+ e- > " + numPho + ";\noutput standalone " + proc + "/PROC" + name + ";")
      folders.append('endProc')
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_elperm_' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_erpelm_' + 'a'*na)
      
    # 4l processes
    if proc == '4lDiffQED':
      f.write("import model cf;\ngenerate e+ e- > mu+ mu- " + numPho + ";\noutput standalone " + proc + "/PROC" + name + ";")
      folders.append('endProc')
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_elperm_mulpmurm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_erpelm_mulpmurm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_elperm_murpmulm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_erpelm_murpmulm' + 'a'*na)
    if proc == '4lSameQED':
      f.write("import model cf;\ngenerate e+ e- > e+ e- " + numPho + ";\noutput standalone " + proc + "/PROC" + name + ";")
      folders.append('endProc')
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_elperm_elperm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_erpelm_elperm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_elperm_erpelm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_erpelm_erpelm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_elpelm_erperm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_erperm_elpelm' + 'a'*na)
      
    # 6l processes
    if proc == '6lSameQED':
      f.write("import model cf;\ngenerate e+ e- > e+ e- e+ e-" + numPho + ";\noutput standalone " + proc + "/PROC" + name + ";")
      # TODO: Get names of folders in SubProcesses and copy these below into the folders
      folders.append('endProc')
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_elperm_elpermelperm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_erpelm_elpermelperm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_elperm_erpelmelperm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_erpelm_erpelmelperm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_elpelm_erpermelperm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_erperm_elpelmelperm' + 'a'*na)
    if proc == '6l4Same2DiffQED':
      f.write("import model cf;\ngenerate e+ e- > e+ e- mu+ mu-" + numPho + ";\noutput standalone " + proc + "/PROC" + name + ";")
      # TODO: Get names of folders in SubProcesses and copy these below into the folders
      folders.append('endProc')
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_elperm_elpermmulpmurm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_erpelm_elpermmulpmurm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_elperm_erpelmmulpmurm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_erpelm_erpelmmulpmurm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_elpelm_erpermmulpmurm' + 'a'*na)
      folders.append(proc + '/PROC' + name + '/SubProcesses/P1_erperm_elpelmmulpmurm' + 'a'*na)
 
    f.close()
    f = open(fList, 'a')
    for folder in folders:
      f.write(folder+'\n')
    f.close()
    # print(folders)
    # print(cList)
    # print(fList)
