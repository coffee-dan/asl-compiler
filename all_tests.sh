#!/bin/bash
# written by dan tbh
tests="$(find Tests/ -regex '.*asl')"
for test in $tests; do
	python3 miniFrontEnd.py $test
	test_output=${test%.asl}
	correct_output=${test_output#Tests/}
	echo 'Comparing to correct answer with diff...'
	
	if ! diff ${test_output}.parse Correct/${correct_output}.parse; then
		break
	fi
done
