---
title: "Explore kinase pocket similarities with KiSSim!"
date: 2021-12-15T12:00:00+02:00
author: dominique.sydow
---

Kinases are an important drug target since their dysregulation can cause servere diseases such as cancer, inflammation, and neurodegeneration. Finding selective drugs, however, is challenging due to the highly conserved binding sites across the roughly 500 human kinases, leading to unwanted side-effects. The underlying off-targets are often not trivial to predict and explain from a sequence-based perspective.

We explored kinase similarity from a physicochemical and structural point of view in our [_KiSSim_](/projects/kissim/) project. We use a kinase-focused and subpocket-enhanced fingerprint to compare kinase pockets across the structurally covered kinome.
Take a look at our [ChemRxiv preprint](xxx) "KiSSim: Predicting off-targets from structural similarities in the kinome" to find out more.
We publish our code as `kissim` Python package available at [GitHub](https://github.com/volkamerlab/kissim) and as `conda` package (check out our [documentation](https://kissim.readthedocs.io/) for more details). All data and analyses are integrated in the `kissim_app` [GitHub](https://github.com/volkamerlab/kissim_app) repository.

Thanks to all co-authors for working together on realizing this project: {{< person "dominique.sydow" >}}, {{< person "eva.assmann" >}}, [Albert Kooistra](https://drug.ku.dk/staff/?pure=en/persons/612712) (University of Copenhagen), Friedrich Rippmann (Merck), and {{< person "andrea.volkamer" >}}.