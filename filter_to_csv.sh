#!/bin/sh
echo "OPTIMIZATION,RESULT" > results.csv
cat  execution_results.txt | grep RESULT | sed  "s/b'//g"| sed "s/'//g" | sed 's/\\n//g' | sed "s/RESULT://g" >> results.csv
