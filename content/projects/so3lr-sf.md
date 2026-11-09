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

Accurate estimation of protein–ligand binding affinities is central to structure-based drug design. Classical force fields neglect important quantum-mechanical effects, while quantum-mechanical methods remain impractical for large biomolecular systems. To bridge this gap, we introduce SO3LR-SF, a fast and explainable physics-based scoring function built on the pretrained SO3LR machine-learned force field (MLFF) and its SO3LR-Tauri variants (SO3LR-T-S, SO3LR-T-M, SO3LR-T-L). Since it requires no training on binding-affinity data, it avoids the inflated performance that can arise for MLFFs trained on protein–ligand complexes.

<!--more-->
<figure style="width: 92%; max-width: 1100px; margin: 2.5em auto;">
  <img src="/images/research/so3lr-sf.png" alt="Overview of the SO3LR-SF workflow, performance and explainability tools" style="width: 100%; border-radius: 0.375em;">
  <figcaption style="margin-top: 0.75em; text-align: center;">Figure 1: Overview of the SO3LR-SF workflow (including optional trimming and constrained optimization), performance of SO3LR variants, and explainability tools</figcaption>
</figure>

SO3LR-SF combines an equivariant message-passing network for semi-local interactions with physically motivated terms for short-range repulsion, electrostatics, and long-range dispersion. On PLA15 (15 active-site models), it attains relative interaction errors of 2.1–5.8% against DLPNO-CCSD(T) references depending on the SO3LR model, with SO3LR-T-M (2.1%) the lowest of all tested methods. On the FEP benchmark (8 targets, 264 ligands), all SO3LR-SF variants reach an average Spearman correlation of about 0.50, on par with the best semi-empirical method tested (GFN-FF, 0.47) and MMGBSA (0.44), and surpassing Glide (0.27). On the Wang dataset (8 targets, 199 ligands), it reaches about 0.59, on par with molecular dynamics-based free-energy methods (0.59–0.62) at a fraction of their cost. Each complex is scored in 3–47 seconds on 12 CPU cores, and an 8 Å trimming protocol further reduces runtime without loss of accuracy.

A multi-level explainability framework adds energy decomposition, per-atom energy contributions reported for the ligand or as 2D protein–ligand interaction maps, and 3D binding site visualization. In addition, pocket descriptors such as the polar solvent accessible surface area (SASA) ratio (r = 0.74–0.81 across models) predict electrostatic scoring performance, allowing ranking accuracy to be estimated before scoring.
