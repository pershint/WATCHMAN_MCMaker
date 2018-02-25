#When run, this script will output a ROOT file containing events randomly
#shot using the data files given into the program.

import ROOT
import glob
import numpy as np
import time
import os

MAINDIR = os.path.dirname(__file__)
DATADIR = os.path.abspath(os.path.join(MAINDIR,"data"))

if __name__ == '__main__':
    rootfiles = glob.glob(DATADIR+"/*.root")
    ch = ROOT.TChain("CombSingles")
    for f in rootfiles:
        print(f)
        ch.Add(f)
    print(ch)
    ch.Draw("good_pos")
    time.sleep(10)
    print("HERE WE GO")
