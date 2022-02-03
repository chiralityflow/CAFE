##############################################
# This implicitly assumes GenProc.sh sits in 
# and is run from the madgraph home directory
co_dir=$(pwd)
#############################################
cd $co_dir
# write the process cards
python  card_write.py

# get list of cards (processes) to consider
cList=$(python -c 'import card_write as c; print(c.getCList())')

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
  printf "\nTesting time to generate files"
  # time (./bin/mg5 cards/$cardUsed > log; cd ${co_dir}/${dir}; caffeinate -i make check > log)
  time ./bin/mg5_amc cards/$cardUsed > log; 

  # go into all SubProcess folders (P1_...). For each folder run the subprocess
  cd $co_dir/$dir
  for d in */ ; do
    cd $co_dir/$dir/$d
    
    # tell user which process we are considering
    export d
    python $co_dir/write_proc_nicely.py

    # compile subprocess
    printf "\nTesting time to compile subprocess"
    time make check > log

    # run subprocess
    printf "\nTesting time to evaluate subprocess"
    time ./check | cat > log
    # for some reason mac monterey doesn't always write to file, so quick workaround
    # was to pipe in cat first. Quicker is just to write to file so uncomment below instead if on Linux
    # time ./check > log
    tail -2 log

  done

  # remove process from list
  cd $co_dir
  ghead -n -1 $cList > temp
  mv temp $cList  
done
