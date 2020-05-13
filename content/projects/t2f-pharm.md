---
title: T²F-Pharm
date: 2020-03-03
publishdate: 2020-03-03
menu:
    main:
        parent: Projects
weight: 10
nav: false
people:
- key: pratik.dhakal
- key: jeremie.mortier
- key: andrea.volkamer
external_resources:
- name: ratar
  link: https://github.com/volkamerlab/ratar
  icon: github
  more: Binding site comparison tool (WIP)
funding:
- name: Bundesministerium für Bildung und Forschung, grant ID 031A262C
  link: "#"
publications:
- t2f2018
---

Pharmacophore models are an accurate and minimal tridimensional abstraction of intermolecular interactions
between chemical structures, usually derived from a group of molecules or from a ligand-target complex.
Only a limited amount of solutions exists to model comprehensive pharmacophores using the information
of a particular target structure without knowledge of any binding ligand.
In the T²F-Pharm project, we developed an automated and customable tool for truly target-focused pharmacophore modeling.
Key molecular interaction fields of a macromolecular structure are calculated using the AutoGRID energy functions.
The most relevant points are selected by a newly developed filtering cascade and clustered to pharmacophore features
with a density-based algorithm.
This method represents an extremely valuable instrument for drug design in a situation of scarce ligand information
available, but also in the case of underexplored therapeutic targets,
as well as to investigate protein allosteric pockets and protein-protein interactions.

<span class="image object">
    <img src="/images/research/t2fpharm.png" alt="T2F-Pharm" />
</span>
