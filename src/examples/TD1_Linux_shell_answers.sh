#!/bin/bash

# extract the places for Derbyshire and save to a file (easier to debug)
curl -s https://opendomesday.org/api/1.0/county/ | grep -oP '\{.*?\[.*?\]\}' | grep Derbyshire > derbyshire.json
# the regexp captures a block for a county
# -o means we want to grep each occurrence (not the full line)
# -P uses perl expression syntax, required for lazy match

# remove our temporary file (not really required, just easier to debug)
rm manors.json

# for each place id in derbyshire
for place in `grep -oP '\d+' derbyshire.json`
do
  # for each manor in that place (regex is similar to the one to extract the places from county data)
  for manor in `curl -s https://opendomesday.org/api/1.0/place/$place/ | grep -oP '\[(\{"id":\d+\})+]' | grep -oP '\d+'` ;
  do
    # output the manor data
    curl -s https://opendomesday.org/api/1.0/manor/$manor/ >> manors.json
    # end current line
    echo '' >> manors.json
  done
done

# json files are geld and totalploughs
# {"id":13079,...,"geld":1.5,..,"totalploughs":4.0,...}
# then using sed to extract the values (assuming we dumped all data in the manors.json file)
# - remove " to have simpler regex
# - in our case null = 0.0, and will be easier to match
# - then match the fields we want and copy their value to a CSV format
sed 's/"//g' manors.json | sed -E 's/null/0.0/g' | sed -E 's/\{id:([0-9]+),.*,geld:([0-9\.]+),.*,totalploughs:([0-9\.]+),.*/\1,\2,\3/g' > manors.csv
