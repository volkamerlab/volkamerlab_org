---
title: PLIPify
date: 2020-10-25
weight: 10
nav: false
people:
- key: jaime.rodriguez
- key: franziska.fritz
- key: david.schaller
- key: andrea.volkamer
external_resources:
  - name: PLIPify repository
    link: https://github.com/volkamerlab/plipify
    icon: github

summary: |
  Protein-Ligand Interaction Frequencies across Multiple Structures.
---

Protein-ligand interactions are an essential part of research in structural bioinformatics and drug discovery. Tools such as the Protein-Ligand Interaction Profiler ([PLIP](https://github.com/pharmai/plip)) enable us to get detailed interaction profiles for single structures. However, combining this data for multiple structures of a protein to identify possible interaction hotspots across them, e.g. when bound to different ligands, remains difficult. The aim of PLIPify is to create and visualize a fingerprint that represents the protein-ligand interaction frequencies over multiple structures of the same protein.

Note that full credits for protein-ligand profile computation go to [PLIP](https://github.com/pharmai/plip) ([Salentin et al. 2015](https://doi.org/10.1093/nar/gkv315), [Adasme et al. 2021](https://doi.org/10.1093/nar/gkab294)). PLIPify provides a wrapper around PLIP, which allows to digest multiple structures at once, performs the mapping of the individual profiles to fingerprints and reports protein-ligand interaction frequencies.
