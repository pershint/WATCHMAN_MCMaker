#When run, this script will output a ROOT file containing events randomly
#shot using the data files given into the program.

import ROOT
from ROOT import gDirectory
import glob
import numpy as np
import lib.FitterTools as ft
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
    ch.Draw("good_pos>>h1_good_pos(100,0.1,1.0)","","goff")
    h1_good_pos = gDirectory.Get("h1_good_pos")
    gfitter = ft.FitEngine(TH1=h1_good_pos,distribution="Gauss")
    gfitter.setFitRange([0.1,1.0])
    gfitter.setParameters([10000.0,0.5,0.5])
    gfitter.MakeFit()
    gfitter.DrawFit()
    time.sleep(4)
    ch.Draw("good_dir>>h1_good_dir(100,0.1,1.0)","","goff")
    h1_good_dir = gDirectory.Get("h1_good_dir")
    gfitter.setHistogramToFit(h1_good_dir)
    gfitter.MakeFit()
    gfitter.DrawFit()
    time.sleep(4)
    ch.Draw("pe>>h1_pe(300,5.0,100.0)","","goff")
    h1_pe = gDirectory.Get("h1_pe")
    gfitter.setHistogramToFit(h1_pe)
    gfitter.setFitRange([0.0,100.0])
    gfitter.setDistribution("Landau")
    gfitter.MakeFit()
    gfitter.DrawFit()
    time.sleep(4)
    print("HERE WE GO")
