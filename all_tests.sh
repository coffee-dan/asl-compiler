#!/bin/bash
# written by dan tbh
tests="$(find Tests/ -regex '.*asl')"
for test in $tests
do
	python3 miniFrontEnd.py $test
	test_output=${test%.asl} #
	correct_output=${test_output#Tests/} #
	echo 'Comparing to correct answer with diff...'
	diff_output="$(diff ${test_output}.parse Correct/${correct_output}.parse)"
	if [[ ! -z "$diff_output" ]]
	then
		echo "$diff_output"
		break
	fi
done

#echo ''
#python3 miniFrontEnd.py Tests/$test_name.asl
#echo 'Comparing to correct answer with diff...'
#diff Tests/$test_name.parse Correct/$test_name.parse
