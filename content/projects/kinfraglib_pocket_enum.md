---
title: "Novel Kinase Ligand Generation using Subpocket-Based Docking"
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

The majority of signal transduction in eukaryotic cells is mediated by protein kinases, whereas dysregulation is often associated with cancer, making them an important drug target. Fragment-based drug design strategies have already shown promising results for developing novel kinase inhibitors. Typically, these approaches consider the structural information about the target but disregard the pre-existing knowledge concerning kinase ligands, although the kinase binding pocket is highly conserved and well-studied.
<!--more-->

This project aims to generate ligands for a given kinase structure _in silico_  in a fragment-based manner, using [KinFragLib](https://volkamerlab.org/projects/kinfraglib/), a kinase-specific fragment library.  By letting a ligand grow within the binding pocket using docking using <a href="https://www.biosolveit.de/flexx/" target="_blank" class="external">FlexX </a>, a greedy search can be performed to reduce the enormous space of fragment combinations. Thereby, we guide the search, using the information on functionally relevant subpockets, such that we only place fragments into specific regions of the binding pocket. Accordingly, we efficiently generate ligands for kinases utilizing the structural information about the binding pocket and the prior knowledge about kinase ligands. 
