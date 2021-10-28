---
title: "OpenCADD"
date: 2020-05-14T16:55:38+02:00
nav: false
draft: false
people:
  - key: jaime.rodriguez
  - key: dominique.sydow
  - key: julian.pipart
  - key: andrea.volkamer
collaborators:
  - name: Dennis Köser, Annie Pham, Enes Kurnaz, Julian Pipart
    more: Structural Alignment 2020 (FU)
  - name: Julian Pipart, Corey Taylor
    more: Benchmarking OpenCADD's structural superposition tool, bachelor thesis 2021 (FU)
external_resources:
  - name: OpenCADD repository
    link: https://github.com/volkamerlab/opencadd
    icon: github
  - name: OpenCADD documentation
    link: https://opencadd.readthedocs.io
    icon: book

summary: |
  A Python library for structural cheminformatics.
---

OpenCADD is a Python library for structural cheminformatics.

<!--more-->

{{< xfigure src="/images/research/opencadd.png" imageclass="fit" caption="The logo of the OpenCADD project." >}}

OpenCADD is a collection of independent Python modules:

- ``structure.superposition``: superimpose macromolecules using sequence and structural information.
- ``structure.pocket``: define and visualize protein (sub)pockets.
- ``databases.klifs``: query the [KLIFS](https://klifs.net/) database, offline or online.
