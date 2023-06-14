# List of processes to be tested
ProcList=('uu~to2g' 'uu~to3g' 'uu~to3g')
#ProcList=('uu~to2g')

#reset file with previous test results. This file must be present in bin.
cp /dev/null testres.txt
#cp /dev/null testzeros.txt

#set whether to compare to mg5 or MadCAFE
#compare_type='MadCAFE'
compare_type='mg5'

# For every process in list: clear old output data, run process in mg5_aMC,
#   use comparefiles to check results with reference data 
for i in "${ProcList[@]}"; do
  cp /dev/null testdata.txt
  cp /dev/null test.txt
  cp /dev/null testzeros.txt
  ./mg5_aMC test_cards/card_$i
  
  python3 comparefiles.py <<< $i' '$compare_type
#  python3 zero_amp_sum.py
done

