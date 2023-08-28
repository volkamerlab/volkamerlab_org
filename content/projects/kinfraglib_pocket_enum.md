---
title: "Subpocket-Based Docking for Kinases"
date: 2023-05-05
nav: false
weight: 10
# Uncomment sections below to enable them in your project
#external_resources:
#- name: KinFragLib_PocketEnum Repository
#  link: https://github.com/volkamerlab/KinFragLib_PocketEnum
#  icon: github
people:
- key: katharina.buchthal
- key: paula.kramer
- key: andrea.volkamer
---

The majority of signal transduction in eukaryotic cells is mediated by protein kinases, whereas dysregulation is often associated with cancer. Fragment-based drug design strategies have already shown promising results for developing novel kinase inhibitors. Typically, these approaches consider the structural information about the target but do not take the kinase-specific prior knowledge into account, although the kinase binding pocket is highly conserved and well-studied.

<!--more-->

This project aims to generate ligands for Kinases  in silico  in a fragment-based manner, using KinFragLib, a kinase-specific fragment library.  By letting a ligand grow within the binding pocket, greedy search was performed to reduce the enormous space of fragment-combinations. Thereby, we guide the search, using the information on functional relevant subpockets, such that we only place specific fragments into specific regions of the binding pocket. Accordingly, we efficiently generate ligands for kinases utilizing the structural and functional information about the binding pocket. 
