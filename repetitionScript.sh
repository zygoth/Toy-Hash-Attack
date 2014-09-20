#! /bin/bash

echo "" > preimage_attacks.txt

for j in `seq 4 4 24`;
do
	for i in `seq 1 100`;
	do
		python $1 $j >> preimage_attacks.txt
	done

done
