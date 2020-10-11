#!/bin/bash
# written by dan tbh
if [ -z "${1}" ]
then
	ls -x --ignore='*.c' --ignore='*.parse' Tests/
	echo 'Choose test case for miniFrontEnd [ no file extenstion ]: '
	read test_name
else
	test_name=$1
fi

python3 miniFrontEnd.py Tests/$test_name.asl
#fromdos Tests/$test_name.parse
echo 'Comparing to correct answer with diff...'
diff Tests/$test_name.parse Correct/$test_name.parse
