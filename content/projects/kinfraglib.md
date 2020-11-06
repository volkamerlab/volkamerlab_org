---
title: KinFragLib
date: 2020-03-03
publishdate: 2020-03-03
weight: 10
nav: false
publications:
- sydow_2020_kinfraglib
people:
- key: paula.schmiel
- key: dominique.sydow
- key: jeremie.mortier
- key: andrea.volkamer
external_resources:
- name: KinFragLib
  link: https://github.com/volkamerlab/KinFragLib
  icon: github
  more: A kinase-focused fragment library
funding:
- name: Bundesministerium für Bildung und Forschung, grant ID 031A262C
- name: Deutsche Forschungsgemeinschaft (DFG), grant ID VO 2353 / 1-1
  link: "https://gepris.dfg.de/gepris/projekt/391684253?language=en&the="
---

The *KinFragLib* project allows to explore and extend the chemical space of kinase inhibitors using
data-driven fragmentation and recombination, built on available structural kinome data from the <a href="https://klifs.vu-compmedchem.nl/" target="_blank" class="external">KLIFS </a> database
for over 2,500 kinase complexes. The computational fragmentation method splits known non-covalent
kinase inhibitors into fragments with respect to their 3D proximity to six predefined subpockets relevant for binding.

<!--more-->

The resulting fragment library consists of six subpocket fragment pools with over 7,000 fragments and
offers two main applications: 
1. In-depth analyses of the chemical space of known kinase inhibitors allow to investigate
subpocket characteristics and connections.
2. Subpocket-informed recombination of fragments enumerates new combinations of known fragments
in order to generate potential novel inhibitors.


{{< xfigure src="/images/research/kinfraglib.png" caption="Ligands co-crystalized with kinases are fragmented with respect to important kinase subpockets, resulting in a kinase-focused fragment library (*KinFragLib*) used for chemical space analysis and recombination." imageclass="fit" >}}
