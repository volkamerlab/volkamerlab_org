---
title: SO3LR-SF
date: 2026-09-08
weight: 10
nav: false
# Uncomment sections below to enable them in your project
external_resources:
- name: SO3LR-SF Repository
  link: https://github.com/volkamerlab/so3lr-sf
  icon: github
publications:
- agha_chemrxiv_2026
people:
- key: hamza.agha
- key: andrea.volkamer
collaborators:
- name: Sergio Suárez-Dou
  more: University of Luxembourg
- name: Adil Kabylda
  more: University of Luxembourg
- name: Alexandre Tkatchenko
  more: University of Luxembourg
---

Accurate estimation of protein–ligand binding affinities is central to structure-based drug design. Classical force fields neglect important quantum-mechanical effects, while quantum-mechanical methods remain impractical for large biomolecular systems. To bridge this gap, we introduce SO3LR-SF, a fast and explainable physics-based scoring function built on the pretrained SO3LR machine-learned force field (MLFF).

<!--more-->
<figure style="width: 92%; max-width: 1100px; margin: 2.5em auto;">
  <img src="/images/research/so3lr-sf.png" alt="Overview of the SO3LR-SF workflow, performance and explainability tools" style="width: 100%; border-radius: 0.375em;">
  <figcaption style="margin-top: 0.75em; text-align: center;">Figure 1: Overview of the SO3LR-SF workflow, performance and explainability tools</figcaption>
</figure>

SO3LR-SF combines an equivariant message-passing network for semi-local interactions with physically motivated terms for short-range repulsion, electrostatics, and long-range dispersion. On PLA15 (15 active-site models), it attains a relative interaction error of 5.8% against DLPNO-CCSD(T) references, the lowest of all tested methods. On the FEP benchmark (8 targets, 264 ligands), it reaches an average Spearman correlation of 0.51, on par with the best semi-empirical method tested (GFN-FF, 0.47) and MMGBSA (0.44), and surpassing Glide (0.27). On the Wang dataset (8 targets, 199 ligands), it reaches 0.51, approaching the 0.60 average of molecular dynamics-based free-energy methods at a fraction of their cost. Each complex is scored in 1–10 seconds on 12 CPU cores, and an 8 Å trimming protocol further reduces runtime without loss of accuracy.

A multi-level explainability framework adds energy decomposition, per-atom energy contributions reported for the ligand or as 2D protein–ligand interaction maps, and 3D binding site visualization. In addition, pocket descriptors such as the polar solvent accessible surface area (SASA) ratio (r = 0.81 with performance) flag applicability before scoring.
