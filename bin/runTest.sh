# List of processes to be tested
ProcList=('e+e-to2a' 'e+e-to3a' 'e+e-to4a' 'mu+mu-to2a' 'mu+mu-to3a' 'mu+mu-to4a' 'ta+ta-to2a' 'ta+ta-to3a' 'ta+ta-to4a')

# Clear old results
cp /dev/null testres.txt

# For every process in list: clear old output data, run process in mg5_aMC,
#   use comparefiles to check results with reference data 
for i in "${ProcList[@]}"; do
  cp /dev/null testdata.txt
  ./mg5_aMC testcards/card$i
  python3 comparefiles.py <<< $i
done
