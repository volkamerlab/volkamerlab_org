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
publications:
- agha_npjdrugdiscov_2026
people:
- key: hamza.agha
- key: michael.backenkoehler 
- key: lacour.antoine
- key: andrea.volkamer
collaborators:
- name: Youssef Ibrahim
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
Consensus SBVS has shown strong hit-identification performance, as demonstrated by DockM8 [[1]](https://chemrxiv.org/engage/chemrxiv/article-details/669e53ee01103d79c5324046). Building on this idea, MolDockLab systematically explores combinations of five docking engines, 15 scoring functions, and three consensus ranking strategies. Using a calibration set of roughly 200 compounds with known bioactivity, it selects the workflow whose scores correlate best with experiment and applies it to the much larger screening library. Final hit selection from the top 1% integrates protein-ligand interaction profiler (PLIP)-derived interaction fingerprints, structural-diversity assessment, and expert visual inspection, as illustrated in Figure 1.

In a retrospective evaluation on the epidermal growth factor receptor (EGFR), the selected pipeline reached a Spearman correlation of 0.36 and an enrichment factor at 10% of 1.57, consistent with its calibration performance. It was then applied prospectively to the energy-coupling factor transporters (ECF-T) [[2]](https://doi.org/10.1039/D3CC04738E), a challenging transmembrane antimicrobial target with a cryptic binding site and no co-crystallized ligand, where it reached a correlation of 0.45 and an enrichment of 3.13. Post-processing enabled the in vitro confirmation of two chemically novel ECF-T inhibitors that rival the most potent ECF-T inhibitors reported to date.

<figure style="width: 92%; max-width: 1100px; margin: 2.5em auto;">
  <img src="/images/research/moldocklab.png" alt="Overview of the MolDockLab pipeline" style="width: 100%; border-radius: 0.375em;">
  <figcaption style="margin-top: 0.75em; text-align: center;">Figure 1: Overview of the MolDockLab pipeline</figcaption>
</figure>
