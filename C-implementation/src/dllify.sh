#!/bin/bash

CFILES=(lacoperon.c engine.c sir.c)

for f in `echo ${CFILES[*]}`; do gcc -c -DBUILD_DLL -fPIC "$f"; done;

for f in `echo ${CFILES[*]}`; do gcc -shared -o `echo ${f/.c/.dll}` `echo ${f/.c/.o}`; done;

mv *.dll ../lib/;
rm *.o;