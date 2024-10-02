---
title: Kinodata-3D
date: 2022-01-01
publishdate: 2023-08-20
weight: 10
nav: false
people:
- key: michael.backenkoehler
- key: andrea.volkamer
collaborators:
- name: Joschka Groß
  link: http://mosi.uni-saarland.de/people/joschka
- name: Verena Wolf
  link: http://mosi.uni-saarland.de/people/verena
external_resources:
- name: kinodata-3D
  link: https://github.com/volkamerlab/kinodata-3D
  icon: github
- name: kinodata-3D-affinity-prediction
  link: https://github.com/volkamerlab/kinodata-3D-affinity-prediction
  icon: github
funding:
- name: NEDD
  link: https://nedd.cs.uni-saarland.de/
---

Machine learning - and especially deep learning - models require large datasets for training. As such datasets, especially those containing protein-ligand-complex information - are more rare in the drug design landscape, we assess the use of _in silico_ structural docking data for machine learning.

To this end, we perform template docking using the [OpenEye](https://www.eyesopen.com) software on a large kinase activity dataset ([kinodata](https://github.com/openkinome/kinodata)) following the complex generation pipeline developed in [kinoml](/projects/kinoml).

<!--more-->

To asses the performance gain of using generated structural data, we extensively compare affinity prediction models with access to the 3D complexes to various baseline models without access to this structure. Overall, we observe an increased performance of the model trained on the docked complexes.

The dataset is also intended as a basis for the [KinfragML](/projects/kinfrag-ml) project.
