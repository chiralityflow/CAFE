# take process lable as input
proc = input()

# read results from file
with open('testdata.txt') as f:
	testlines = f.readlines()
f.close()

# read reference data for the process
with open('compdata/compdata' + proc + '.txt') as f:
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

if error > 10**(-11):
	no_error = False
if no_error:
	test_res.write(proc + ":  all tests passed, error:" + str(error) + "\n")
else:
	test_res.write(proc + ":  test failed, error:" + str(error) + "\n")
test_res.close()
