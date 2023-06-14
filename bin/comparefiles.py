# take process lable as input
proc, compare_type  = input().split()

# read results from file
with open('testdata.txt') as f:
	testlines = f.readlines()
f.close()

#set whether to compare to mg5 or MadCAFE
#compare_type = "MadCAFE"

#works
if compare_type == "mg5":
	# read reference data for the process
	with open('test_comp_data/comp_data_mg5_' + proc + '.txt') as f:
			comparelines = f.readlines()
	f.close()

	# Add the results for each subprocess to get total result for process
	proc_total = 0.0
	for i in range(len(testlines)):
		proc_total += float(testlines[i][:-1]) 

	# calculate the error compared to reference data
	error = abs(1-(proc_total)/(float(comparelines[0][:-1])))

	# record results in file.
	no_error = True
	test_res = open('testres.txt', 'a') 

	if error > 10**(-14):
		no_error = False
	if no_error:
		test_res.write(proc + ":  all tests passed, error:" + str(error) + '.   Res:  ' + str(proc_total) + "\n")
	else:
		test_res.write(proc + ":  test failed, error:" + str(error) + '.   Res:  ' + str(proc_total) + "\n")
	test_res.close()

#needs to be tested
if compare_type == "MadCAFE":
	# read reference data for each subprocess
	with open('test_comp_data/comp_data_MadCAFE_' + proc + '.txt') as f:
			comparelines = f.readlines()
	f.close()
	
	# record results in file.
	test_res = open('testres.txt', 'a')
	
	for i in range(len(testlines)):
		error = abs(1-(float(testlines[i][:-1]))/(float(comparelines[i][:-1])))
			
		no_error = True
		
		if error > 10**(-14):
			no_error = False
		if no_error:
			test_res.write(proc + "_subproc_" + str(i+1) + ":  all tests passed, error:" + str(error) + '.   Res:  ' + str(testlines[i][:-1]) + "\n")
		else:
			test_res.write(proc + "_subproc_" + str(i+1) + ":  test failed, error:" + str(error) + '.   Res:  ' + str(testlines[i][:-1]) + "\n")
	test_res.close()
