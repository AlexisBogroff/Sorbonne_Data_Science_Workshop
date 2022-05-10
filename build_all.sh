#!/bin/bash

cd src

ls Lecture_[1-6]*.tex > filelist.txt
# ls TD[1-6]*.tex >> filelist.txt

for file in `cat filelist.txt`
do
  echo "---------------------------------------------------"
  echo "start building tex file $file"
  source build.sh $file
  echo "end building tex file $file"
  echo "---------------------------------------------------"
done

rm filelist.txt

cd ..
