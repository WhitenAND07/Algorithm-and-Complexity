SHELL:=/bin/bash

test :
	for i in $$(seq 2 2 16);\
	do \
	   python generator.py $$i $$i > cargo.txt 2> sol1.txt; \
	   python ilerda.py cargo.txt > sol2.txt; \
	   if $$(python checker.py cargo.txt sol1.txt sol2.txt); then echo OK; else echo KO; exit; fi \
	done
