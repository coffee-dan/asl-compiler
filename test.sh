#!/bin/bash
python3 miniFrontEnd.py Tests/testCase_01.asl
fromdos Tests/testCase_01.parse
echo "Comparing to correct answer with diff..."
diff Tests/testCase_01.parse Correct/testCase_01.parse
python3 miniFrontEnd.py Tests/testCase_02.asl
fromdos Tests/testCase_02.parse
echo "Comparing to correct answer with diff..."
diff Tests/testCase_02.parse Correct/testCase_02.parse
