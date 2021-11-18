---
title: Maxsmi
date: 2021-11-01
publishdate: 2021-11-01
weight: 10
nav: false
people:
- key: talia.kimber
- key: andrea.volkamer
collaborators:
- name: Maxime Gagnebin
external_resources:
- name: maxsmi
  link: https://github.com/volkamerlab/maxsmi
  icon: github
  more: Data augmentation for molecular property prediction using deep learning
funding:
- name: The Einstein Foundation & Stiftung Charité
  link: https://www.einsteinfoundation.de/en/programmes/einstein-bih-visiting-fellow/
  more: BIH Einstein Visiting Fellowship
publications:
- kimber_ailsci_2021
---

Accurate molecular property or activity prediction is one of the main goals in computer-aided drug design. Quantitative structure-activity relationship (QSAR) modeling and machine learning, more recently deep learning, have become an integral part of this process. Such algorithms require lots of data for training, which, in the case of physico- chemical and bioactivity data sets remains scarce.

<!--more-->

To address the lack of data, augmentation techniques are sought. Here, we exploit that one compound can be represented by various SMILES strings as means of data augmentation and we explore several augmentation techniques. The best strategies lead to the Maxsmi models, the models that <b>max</b>imize the performance in <b>SMI</b>LES augmentation. These models are trained on four data sets, including experimental solubility, lipophilicity, and bioactivity measurements.


{{< xfigure src="/images/research/maxsmi.png" caption="Given a compound represented by its canonical SMILES, the Maxsmi model produces a prediction for each of the SMILES variations. The aggregation of these values leads to a per compound prediction and the standard deviation to an uncertainty in the prediction. The Maxsmi model predicts lipophilicity of semaxanib to 3.109, with an uncertainty of 0.442." imageclass="fit" >}}
