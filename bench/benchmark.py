#!/usr/bin/python
import sys, os
import subprocess

testfile = sys.argv[1]

pmarsopt = "pmars.opt"

papertests = ["paper-time0000.red", "paper-nobody00.red", "paper-paperone.red", "paper-marcia13.red"]
scisrtests = ["scisr-irongate.red", "scisr-pswing00.red", "scisr-rave0000.red", "scisr-thermite.red"]
stonetests = ["stone-bluefunk.red", "stone-cannon00.red", "stone-fstorm00.red", "stone-tornado0.red"]

benchtesttypes = ["papertests", "scisrtests", "stonetests"]
benchheaders = {"papertests" : "Paper Enemies- - - W  L  T \n", "scisrtests" : "Scissor Enemies- - W  L  T \n", "stonetests" : "Stone Enemies- - - W  L  T \n"}

print "Benchmark Results for " + testfile + "\n"

for testtype in benchtesttypes:
    tests = eval(testtype)
    benchstats = benchheaders[testtype]
    for enemy in tests:
        results = subprocess.Popen(["./pmars", "-@", pmarsopt, testfile, enemy], stdout=subprocess.PIPE)
        for line in results.stdout:
            if "Results" in line:
                lineseg = line.split()
                benchstats = benchstats + enemy + " " + lineseg[1].zfill(2) + " " + lineseg[2].zfill(2) + " " + lineseg[3].zfill(2) + "\n"
    print benchstats


