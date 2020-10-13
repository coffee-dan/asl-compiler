#!/bin/bash
# written by dan tbh
for fName in Tests/*.asl
do
	python3 miniFrontEnd.py $fName
	
	test_output=${fName%.asl} # Remove '.asl'
	correct_output=${test_output#Tests/} # Remove 'Tests/'
	
	echo 'Comparing to correct outputs with diff...'
	diff_output="$(diff ${test_output}.parse Correct/${correct_output}.parse)"
	if [[ ! -z "$diff_output" ]]
	then
		echo "*** Incorrect parse of ${fName}."
		echo "$diff_output"
		break
	fi

	diff_output="$(diff ${test_output}.ast Correct/${correct_output}.ast)"
	if [[ ! -z "$diff_output" ]]
	then
		echo "*** Incorrect semantic of ${fName}."
		echo "$diff_output"
		break
	fi

done
