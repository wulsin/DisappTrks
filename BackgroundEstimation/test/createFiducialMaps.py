#!/usr/bin/env python3

import math
from DisappTrks.BackgroundEstimation.FiducialMapCalculator import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors, gStyle
import os

gROOT.SetBatch()
gStyle.SetPalette(56)

dirs = getUser()
canvas = TCanvas("c1", "c1", 800, 800)

selectionNames = ['FiducialCalcBefore', 'FiducialCalcAfter']

# Will use Dataset_runPeriod.root
runPeriods = ['2015']
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    runPeriods = ['2016']
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    runPeriods = ['2017B', '2017C', '2017D', '2017E', '2017F', '2017']
    selectionNames = ['FiducialCalcBeforeOldCuts', 'FiducialCalcAfterOldCuts']
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    runPeriods = ['2018A', '2018B', '2018C', '2018D', '2018']
    selectionNames = ['FiducialCalcBeforeOldCuts', 'FiducialCalcAfterOldCuts']

for runPeriod in runPeriods:

    print "********************************************************************************"
    print "Calculating electron fiducial map in search region", runPeriod
    print "--------------------------------------------------------------------------------"

    condorDirectory = dirs['Brian'] + "2015/eleHotSpots"
    datasetName = "SingleEle"
    if '2016' in runPeriod:
        condorDirectory = dirs['Brian'] + "2016_final/eleHotSpots"
    if '2017' in runPeriod:
        condorDirectory = dirs['Brian'] + "2017/fromLPC/eleHotSpots"
    if '2018' in runPeriod:
        condorDirectory = dirs['Brian'] + "2018/fromLPC/eleHotSpots"
        datasetName = "EGamma"
        
    fout = TFile.Open("newElectronFiducialMap_" + runPeriod + ".root", "recreate")
    
    electronMap = FiducialMapCalculator()
    #electronMap.setVerboseComparison(True)
    electronMap.addTFile(fout)
    electronMap.addTCanvas(canvas)
    electronMap.addLuminosityInInvPb(lumi[datasetName + "_" + runPeriod])
    electronMap.addChannel("Denominator", "Electron" + selectionNames[0], datasetName + "_" + runPeriod, condorDirectory)
    electronMap.addChannel("Numerator",   "Electron" + selectionNames[1], datasetName + "_" + runPeriod, condorDirectory)
    electronMap.CalculateFiducialMap()
    electronMap.MakePlots()
    electronMap.CompareFiducialMap()
    print "********************************************************************************"
    print "\n\n"
        
    fout.Close()

    condorDirectory = dirs['Brian'] + "2015/muonHotSpots"
    if '2016' in runPeriod:
        condorDirectory = dirs['Brian'] + "2016_final/muonHotSpots"
    if '2017' in runPeriod:
        condorDirectory = dirs['Brian'] + "2017/muonHotSpots"
    if '2018' in runPeriod:
        condorDirectory = dirs['Brian'] + "2018/fromLPC/muonHotSpots"

    print "********************************************************************************"
    print "Calculating muon fiducial map in search region", runPeriod
    print "--------------------------------------------------------------------------------"
    
    fout = TFile.Open("newMuonFiducialMap_" + runPeriod + ".root", "recreate")
    
    muonMap = FiducialMapCalculator()
    #muonMap.setVerboseComparison(True)
    muonMap.addTFile(fout)
    muonMap.addTCanvas(canvas)
    muonMap.addLuminosityInInvPb(lumi["SingleMuon_" + runPeriod])
    muonMap.addChannel("Denominator", "Muon" + selectionNames[0], "SingleMu_" + runPeriod, condorDirectory)
    muonMap.addChannel("Numerator",   "Muon" + selectionNames[1], "SingleMu_" + runPeriod, condorDirectory)
    muonMap.CalculateFiducialMap()
    muonMap.MakePlots()
    muonMap.CompareFiducialMap()
    print "********************************************************************************"
    print "\n\n"
    
    fout.Close()

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_7_6_"):
    remakePayload('Electron', '2015')
    remakePayload('Muon',     '2015')
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    remakePayload('Electron', '2016')
    remakePayload('Muon',     '2016')
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    remakePayload('Electron', '2017', ['B', 'C', 'D', 'E', 'F'])
    remakePayload('Muon', '2017', ['B', 'C', 'D', 'E', 'F'])
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    remakePayload('Electron', '2018', ['A', 'B', 'C', 'D'])
    remakePayload('Muon',     '2018', ['A', 'B', 'C', 'D'])
