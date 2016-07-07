#!/usr/bin/python
import sys, os
import subprocess

testfile = sys.argv[1]

benchstats = "Benchmark Results for " + testfile + "\nEnemy - - - - - - - - - - - W L T\n"

tests = ["paper-time0000.red", "paper-nobody00.red", "paper-paperone.red", "paper-marcia13.red",
         "scisr-irongate.red", "scisr-pswing00.red", "scisr-rave0000.red", "scisr-thermite.red",
         "stone-bluefunk.red", "stone-cannon00.red", "stone-fstorm00.red", "stone-tornado0.red"]

for enemy in tests:
    results = subprocess.Popen(["./pmars", "-@", "bench.opt", testfile, enemy], stdout=subprocess.PIPE)
    for line in results.stdout:
        if "Results" in line:
		benchstats = benchstats + enemy + " " + line
print benchstats
