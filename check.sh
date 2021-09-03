#!/bin/bash
contest_id=$1
problem_id=$2

cd $contest_id/$problem_id
#echo $(pwd)

out="out.txt"
yout="yout.txt"

echo Given output
cat $out && echo
echo Your output
cat $yout && echo


if cmp -s "$out" "$yout"; then
	echo Correct output!!!
else
	echo Wrong output...
fi


