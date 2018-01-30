#!/bin/bash

ls *.b6 |
    while read b6
    do
	python3 b6maPNG.py "$b6"
    done