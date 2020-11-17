---
title: KiSSim
date: 2020-03-03
publishdate: 2020-03-03
weight: 10
nav: false
people:
- key: dominique.sydow
- key: eva.assmann
- key: andrea.volkamer
collaborators:
- name: Albert Kooistra
  link: https://drug.ku.dk/staff/?pure=en/persons/612712
  more: University of Copenhagen
- name: Friedrich Rippmann
  more: Merck
external_resources:
- name: kissim
  link: https://github.com/volkamerlab/kissim
  icon: lock
  more: Subpocket-based fingerprint for structural kinase comparison (WIP)
funding:
- name: Bundesministerium für Bildung und Forschung, grant ID 031A262C
- name: Deutsche Forschungsgemeinschaft (DFG), grant ID VO 2353 / 1-1
  link: "https://gepris.dfg.de/gepris/projekt/391684253?language=en&the="
---

Kinases are important and well studied drug targets for cancer and inflammatory diseases.
Due to the highly conserved structure of kinases, especially at the ATP binding site,
the main challenge when developing kinase inhibitors is achieving selectivity,
which requires a comprehensive understanding of kinase similarity.
In our *KiSSim* (kinase structural similarity) project, we developed a subpocket-focused kinase fingerprint to investigate kinome-wide pocket similarity.

<!--more-->

The *KiSSim* fingerprint is based on the <a href="https://klifs.net/" target="_blank" class="external">KLIFS </a> pocket alignment, which defines 85 pocket residues for all kinase structures.
This enables a residue-by-residue comparison of spatial and physicochemical features
without the need for a computationally expensive alignment step.
We aim to use the *KiSSim* method to detect potential off-targets at an early stage of inhibitor design and to conduct structure-informed polypharmacology studies.

{{< xfigure src="/images/research/kissim.png" caption="Kinase structural similarity (*KiSSim*) is calculated by pairwise comparisons of subpocket-based kinase fingerprints, considering each pocket residue's physicochemical properties and spatial arrangement towards important subpockets and the pocket center." imageclass="fit" >}}
