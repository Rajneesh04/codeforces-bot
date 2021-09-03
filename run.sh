#!/bin/bash
contest_id=$1
problem_id=$2

cd $contest_id/$problem_id
#echo $(pwd)

g++ -std=c++17 $problem_id.cpp -o a.out || { echo "$problem_id.cpp failed to build....."; exit 1; }
echo Compiled successfully.....

./a.out < input.txt > yout.txt
#echo Ouput saved to yout.txt

cd ..
cd ..

./check.sh $contest_id $problem_id



