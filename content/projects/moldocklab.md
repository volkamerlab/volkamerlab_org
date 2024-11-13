---
title: MolDockLab
date: 2023-04-15
weight: 10
nav: false
# Uncomment sections below to enable them in your project
external_resources:
- name: MolDockLab Repository
  link: https://github.com/volkamerlab/MolDockLab
  icon: github
people:
- key: hamza.ibrahim
- key: michael.backenkoehler 
- key: lacour.antoine
- key: andrea.volkamer
collaborators:
- name: Ioulia Antonia Exapicheidou
  link: https://www.helmholtz-hips.de/en/research/teams/team/drug-design-and-optimisation/
  more: HIPS
- name: Mostafa Hamed
  link: https://www.helmholtz-hips.de/en/research/teams/team/drug-design-and-optimisation/
  more: HIPS
- name: Anna K. H. Hirsch
  link: https://www.helmholtz-hips.de/en/research/teams/team/drug-design-and-optimisation/
  more: HIPS
---

Finding the optimal docking pipeline for consensus structure-based virtual screening (SBVS) and the diversity nature of protein are challenging. To address this challenge, we introduce MolDockLab, a novel framework designed to identify the most convenient combination of docking tools, scoring functions, and consensus ranking methods tailored for a target of interest. 

<!--more-->
Consensus structure-based virtual screening (SBVS) has demonstrated high performance in hit identification, as shown in DockM8 [[1]](https://chemrxiv.org/engage/chemrxiv/article-details/669e53ee01103d79c5324046). By leveraging a small data set of approximately 200 molecules, MolDockLab offers a fully automated pipeline. It identifies the most efficient combination of docking tools, scoring functions, and ranking methods for consensus SBVS, which is then applied to larger datasets. The top compounds are further processed to select the most promising candidates, as illustrated in Figure 1.

Energy-coupling factor transporters (ECF-T) are novel and promising antimicrobial targets that mediate micronutrient transport into the cell [[2]](https://doi.org/10.1039/D3CC04738E). As a case study, MolDockLab was deployed for ECF-T hit identification, leading to the discovery of two promising hits in in vitro assays. Testing similar compounds resulted in the identification of nine additional hits, demonstrating the efficacy of MolDockLab.

{{< figure src="/images/research/moldocklab.png" caption="Figure 1: Overview of MolDockLab Pipeline" >}}
