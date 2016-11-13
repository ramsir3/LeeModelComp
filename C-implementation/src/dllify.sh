#!/bin/bash

CFILES=(lacoperon.c engine.c sir.c)

for f in `echo ${CFILES[*]}`; do gcc -c -Wall -Werror -fpic "$f"; done;

for f in `echo ${CFILES[*]}`; do gcc -shared -o `echo ${f/.c/.so}` `echo ${f/.c/.o}`; done;

mv *.so ../lib/;
rm *.o;