##############################################
# This implicitly assumes GenProc.sh sits in 
# and is run from the madgraph home directory
co_dir=$(pwd)
#############################################
cd $co_dir
# write the process cards
python3  card_write.py

# get list of cards (processes) to consider
cList=$(python3 -c 'import card_write as c; print(c.getCList())')

# echo "$cList"
# proc=$(cat $cList)
# echo "$proc"

# loop over processes
while [ -s $cList ]; do
  # get process
  cardUsed=$(tail -1 $cList)
  printf "\n-----------------------------"
  printf "\nProcessing ${cardUsed}"
  printf "\n-----------------------------\n"

  # get directory card outputted using last line of cardUsed
  cd $co_dir/cards
  dir=$(tail -1 $cardUsed)
  prefix="output standalone "
  dir="${dir#"$prefix"}/SubProcesses"

  # go back to main directory to run madgraph
  cd $co_dir

  # generate the process
  #printf "\nTesting time to generate files"
  # time (./bin/mg5 cards/$cardUsed > log; cd ${co_dir}/${dir}; caffeinate -i make check > log)
  #time ./bin/mg5_aMC cards/$cardUsed > log; 
  { time ./bin/mg5_aMC cards/$cardUsed > log ; } 2>>makeTime

  # go into all SubProcess folders (P1_...). For each folder run the subprocess
  cd $co_dir/$dir
  for d in */ ; do
    cd $co_dir/$dir/$d
    
    # tell user which process we are considering
    export d
    python3 $co_dir/write_proc_nicely.py

    # compile subprocess
    #printf "\nTesting time to compile subprocess"
    #time make check > log
    { time make check > log ; } 2>> $co_dir/makeTime

    # run subprocess
    #printf "\nTesting time to evaluate subprocess"
    # time ./check | cat > log
    # for some reason mac monterey doesn't always write to file, so quick workaround
    # was to pipe in cat first. Quicker is just to write to file so uncomment below instead if on Linux
    #time ./check  > log
    { time ./check  > log ; } 2>> $co_dir/runTime
    #tail -2 runTime 
    #tail -2 log
    rm log

  done

  # remove process from list
  cd $co_dir
  # To run on Mac
  #ghead -n -1 $cList > temp
  # To run on Linux
  head -n -1 $cList > temp
  mv temp $cList  
  python3 timeTest.py
  rm runTime makeTime
done
