#!/bin/bash

python_code=$(cat <<- END

import pathlib

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST =   DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"

def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        data = f.read().splitlines()
        return data 

data = read_file(DATA_TEST)


# Part 1



# Part 2



END

)


mkdir 2020
cd 2020

for i in {01..25}; do
    
    folder="day_$i"
    
    mkdir $folder
    cd $folder
    
    mkdir data
    cd data
    touch input.txt input_test.txt
    cd ..
    
    mkdir py go ts
    for j in py go ts; do
        cd $j
        touch script.$j
        if [ $j == "py" ]; then
            echo "$python_code" > script.$j
        fi
        cd ..
    done
    
    cd ..
done