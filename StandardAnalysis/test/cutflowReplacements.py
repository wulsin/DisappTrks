#!/usr/bin/env python3

# List of replacements used for making cutflow tables
#
# In appropriate localOptions file, add the lines:
# from cutflowReplacements import *
# replacements_extra = replacements_extra_XX


# Standard replacements to use for AN
replacements_extra_AN = {
    "$>$= 1 event with FilterOutScraping $>$ 0": "%",
    "$>$= 1 primaryvertex with isGood $>$ 0 " : "%",
    "$>$= 1 Met with $p_{T}$ $>$ 100" : "$\\not\\!\\!{E}_{T}$ $>$ 100 GeV",
    "$>$= 1 secondary jet with $p_{T}$ $>$ 110" : "leading jet with $p_{T} >$ 110 GeV",
    "$>$= 1 secondary jet with fabs(eta) $<$ 2.4" : "leading jet with $|\eta| < 2.4$",
    "$>$= 1 secondary jet with chargedHadronEnergyFraction $>$ 0.2": "leading jet with charged hadron energy fraction $>$ 0.2",
    "$>$= 1 secondary jet with chargedEmEnergyFraction $<$ 0.5" : "leading jet with charged EM energy fraction $<$ 0.5",
    "$>$= 1 secondary jet with neutralHadronEnergyFraction $<$ 0.7" : "leading jet with neutral hadron energy fraction $<$0.7",
    "$>$= 1 secondary jet with neutralEmEnergyFraction $<$ 0.7" : "leading jet with neutral EM energy fraction $<$ 0.7",
    "$>$= 1 jet with disappTrkSubLeadingJetID $>$ 0" : "%",
    "= 0 jet-jet pairs with deltaPhi $>$ 2.5" : "0 jet pairs with $\Delta \phi > 2.5$",
    "$>$= 1 Met with fabs(deltaPhiMin2Jets) $>$ 0.5" : "$\Delta \phi > 0.5 - \\not\\!\\!{E}_{T} \&\&$ 2 highest $p_{T}$ jets",
    "$>$= 1 track with $p_{T}$ $>$ 50" : "track with $p_{T}$ $>$ 50 GeV",
    "$>$= 1 track with fabs(eta) $<$ 2.1" : "track with $|\eta| < 2.1$",
    "$>$= 1 track with fabs(eta) $<$ 1.42 | fabs(eta) $>$ 1.65" : "!in ECAL barrel-endcap crack, $1.42 < |\eta| < 1.65$",
    "$>$= 1 track with fabs(eta) $<$ 0.15 | fabs(eta) $>$ 0.35" : "!in DT Wheel 0 gap, $0.15 < |\eta| < 0.35$",
    "$>$= 1 track with fabs(eta) $<$ 1.55 | fabs(eta) $>$ 1.85" : "!in region of larger $\mu$ inefficiency, $1.55 <|\eta| < 1.85$",
    "$>$= 1 track with isMatchedDeadEcal == 0" : "!within $\Delta R < 0.05$ of dead or noisy ECAL cluster",
    "$>$= 1 track with isMatchedBadCSC == 0" : "!within $\Delta R < 0.25$ of errant CSC",
    "$>$= 1 track with fabs($d_{0}$wrtPV) $<$ 0.02" : "track with $|d_0| < 0.02$cm",
    "$>$= 1 track with fabs(dZwrtPV) $<$ 0.5" : "track with $|d_z| < 0.5$cm",
    "$>$= 1 track with numValidHits $>$= 7" : "track with $\geq 7$ valid hits",
    "$>$= 1 track with nHitsMissingMiddle == 0" : "track with no missing middle hits",
    "$>$= 1 track with nHitsMissingInner == 0" : "track with no missing inner hits",
    "$>$= 1 track with trkRelIsoRp3 $<$ 0.05" : "track with $(\Sigma p_T^{\Delta R<0.3} - p_T)/p_T < 0.05$",
    "$>$= 1 track with deltaRMinSubLeadJet $>$ 0.5" : "$\Delta R > 0.5$ between track and subleading jet",
    "$>$= 1 track with deltaRMinElecLooseMvaId $>$ 0.15" : "!within $\Delta R < 0.15$ of $e$, $\pt > 10$ GeV",
    "$>$= 1 track with deltaRMinTauLooseHadronicId $>$ 0.15" : "!within $\Delta R < 0.15$ of $\\tau$, $\pt > 30$ GeV, $|\eta| < 2.3$, loose tau ID",
    "$>$= 1 track with deltaRMinMuonLooseId $>$ 0.15" : "!within $\Delta R < 0.15$ of $\mu$, $\pt > 10$ GeV",
    "$>$= 1 track with deltaRMinSecMuonLooseId $>$ 0.15" : "%",
    "$>$= 1 track with caloTotDeltaRp5RhoCorr $<$ 10" : "$E_{calo}^{\Delta R < 0.5} < 10$ GeV",
    "$>$= 1 track with nHitsMissingOuter $>$= 3" : "track with $\geq$ 3 missing outer hits",
    "Weighted Yield" : "%",
    }

# For table in PAS summarizing signal efficiencies after different stages of the selection
replacements_extra_EffSigPAS = {
    "Total" : "%Total",
    "$>$= 1 event with FilterOutScraping $>$ 0": "%",
    "$>$= 1 primaryvertex with isGood $>$ 0 " : "%",
    "$>$= 1 Met with $p_{T}$ $>$ 100" : "%",
    "$>$= 1 secondary jet with $p_{T}$ $>$ 110" : "%",
    "$>$= 1 secondary jet with fabs(eta) $<$ 2.4" : "%",
    "$>$= 1 secondary jet with chargedHadronEnergyFraction $>$ 0.2": "%",
    "$>$= 1 secondary jet with chargedEmEnergyFraction $<$ 0.5" : "%",
    "$>$= 1 secondary jet with neutralHadronEnergyFraction $<$ 0.7" : "%",
    "$>$= 1 secondary jet with neutralEmEnergyFraction $<$ 0.7" : "%",
    "$>$= 1 jet with disappTrkSubLeadingJetID $>$ 0" : "%",
    "= 0 jet-jet pairs with deltaPhi $>$ 2.5" : "%",
    "$>$= 1 Met with fabs(deltaPhiMin2Jets) $>$ 0.5" : "basic selection",
    "$>$= 1 track with $p_{T}$ $>$ 50" : "%",
    "$>$= 1 track with fabs(eta) $<$ 2.1" : "%",
    "$>$= 1 track with fabs(detectorEta) $<$ 1.42 | fabs(detectorEta) $>$ 1.65" : "%",
    "$>$= 1 track with fabs(eta) $<$ 1.42 | fabs(eta) $>$ 1.65" : "%",
    "$>$= 1 track with fabs(eta) $<$ 0.15 | fabs(eta) $>$ 0.35" : "%",
    "$>$= 1 track with fabs(eta) $<$ 1.55 | fabs(eta) $>$ 1.85" : "%",
    "$>$= 1 track with isMatchedDeadEcal == 0" : "%",
    "$>$= 1 track with isMatchedDeadEcalDet == 0" : "%",
    "$>$= 1 track with detectorEta $>$ -1.14018 || detectorEta $<$ -1.1439" : "%",
    "$>$= 1 track with detectorEta $>$ -0.791884 || detectorEta $<$ -0.796051" : "%",
    "$>$= 1 track with detectorEta $>$ -0.44356 || detectorEta $<$ -0.447911" : "%",
    "$>$= 1 track with detectorEta $>$ 0.00238527 || detectorEta $<$  -0.00330793" : "%",
    "$>$= 1 track with detectorEta $>$ 0.446183 || detectorEta $<$ 0.441949" : "%",
    "$>$= 1 track with detectorEta $>$ 0.793955 || detectorEta $<$ 0.789963" : "%",
    "$>$= 1 track with detectorEta $>$ 1.14164 || detectorEta $<$ 1.13812" : "%",
    "$>$= 1 track with isMatchedBadCSC == 0" : "%",
    "$>$= 1 track with fabs($d_{0}$wrtPV) $<$ 0.02" : "%",
    "$>$= 1 track with fabs(dZwrtPV) $<$ 0.5" : "%",
    "$>$= 1 track with numValidHits $>$= 7" : "%",
    "$>$= 1 track with nHitsMissingMiddle == 0" : "%",
    "$>$= 1 track with nHitsMissingInner == 0" : "%",
    "$>$= 1 track with trkRelIsoRp3 $<$ 0.05" : "%",
    "$>$= 1 track with deltaRMinSubLeadJet $>$ 0.5" : "high-\\pt isolated track",
    "$>$= 1 track with deltaRMinElecLooseMvaId $>$ 0.15" : "%",
    "$>$= 1 track with deltaRMinTauLooseHadronicId $>$ 0.15" : "%",
    "$>$= 1 track with deltaRMinMuonLooseId $>$ 0.15" : "%",
    "$>$= 1 track with deltaRMinSecMuonLooseId $>$ 0.15" : "candidate track",
    "$>$= 1 track with caloTotDeltaRp5RhoCorr $<$ 10" : "%",
    "$>$= 1 track with nHitsMissingOuter $>$= 3" : "disappearing track",
    "Weighted Yield" : "%",
    }
