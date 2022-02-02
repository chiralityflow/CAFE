##############################################
# TODO: Put your own directory here!!
co_dir=~/Physics/ChiralityFlowMG/ChiralityFlowMG
#############################################
cd $co_dir
python  card_write.py
# get list of cards and folders to consider
cList=$(python -c 'import card_write as c; print(c.getCList())')
fList=$(python -c 'import card_write as c; print(c.getFList())')
# echo "$cList"
# proc=$(cat $cList)
# echo "$proc"
# dir=$(cat $fList)
# echo "$dir"

# loop over processes
while [ -s $cList ]; do
  # get first process
  cardUsed=$(tail -1 $cList)
  printf "\n-----------------------------"
  printf "\nProcessing ${cardUsed}\n"
  printf "-----------------------------\n"
  #echo "$cardUsed"

  # generate the process
  dir=$(tail -1 $fList)
  # echo "$dir"
  printf "\nTesting time to generate files"
  # time (./bin/mg5 cards/$cardUsed > log; cd ${co_dir}/${dir}; caffeinate -i make check > log)
  time ./bin/mg5_amc cards/$cardUsed > log; 

  # for the first subprocess check how long it takes to compile and evaluate
  printf "\nTesting time to compile subprocess"
  cd ${co_dir}/${dir}
  time make check > log
  printf "\nTesting time to evaluate subprocess"
  cd ${co_dir}/${dir}
  time ./check > log
  # print matrix element to screen
  tail -2 log
  cd ${co_dir}

  # remove subprocess from flist
  ghead -n -1 $fList > temp
  mv temp $fList

  # loop through all other subprocesses
  for i in {1..100}; do
    # get the subprocess
    dir=$(tail -1 $fList)
    printf "\n$dir"
    # check if the subprocesses has finished, if it has, remove it and end this loop
    if [ "$dir" == "endProc" ]
    then
      ghead -n -1 $fList > temp
      mv temp $fList  
      break
    fi   
    # test compile and evaluation time for this subprocess
    printf "\nTesting time to compile subprocess"
    cd ${co_dir}/${dir}
    time make check > log
    printf "\nTesting time to evaluate subprocess"
    cd ${co_dir}/${dir}
    time ./check > log
    # print matrix element to screen
    tail -2 log
    # remove subprocess from flist
    cd ${co_dir}
    ghead -n -1 $fList > temp
    mv temp $fList
  done
  # remove process from list
  ghead -n -1 $cList > temp
  mv temp $cList  
done
