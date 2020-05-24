---
title: "Cptox21"
date: 2020-05-20T17:53:27+02:00
weight: 10
nav: false

people:
- key: andrea-lilian.morger
- key: andrea.volkamer

collaborators:
- name: Ola Spjuth
  link: https://katalog.uu.se/profile?id=N2-878
- name: Ulf Norinder
  link: "#"
- name: Fredrik Svensson
  link: https://iris.ucl.ac.uk/iris/browse/profile?upi=FSVEN25
- name: Niharika Gauraha
  link: https://www.kth.se/profile/niharika?l=en
- name: Staffan Arvidsson
  link: https://katalog.uu.se/profile/?id=N15-1564

funding:
- name: FUBright Mobility Allowance for Research Stay
  link: "https://www.fu-berlin.de/en/sites/drs/international/fubright/fubright-mobilitaet/index.html"
- name: HaVo-Stiftung
  link: "#"
---

<!-- ((Move this part to the research page 'machine learning' or 'conformal prediction' - including the figure:)) -->

Machine learning models should not only be well-performing. It is also important to know if the models can be applied
to a certain dataset and if (how much) we can trust the predictions. This can be approached with conformal prediction,
a recently promoted method for confidence estimation. A conformal predictor returns, whether enough evidence is given
to reliably assign the query substance to a certain class. The conformal prediction framework is built on top of
machine learning models, but includes an additional calibration step. Thus, predictions made for a query compound
are compared to those made for the calibration set compounds.
{{< xfigure src="/images/research/conformal_prediction.png" caption="Conformal Prediction" imageclass="fit" >}}


ML algorithms and thus also CP are only intended to be applied to data where training data and data to predict are
drawn from the same distribution. This is often not the case. In this project, we show how CP calibration plots can
be used to diagnose any deviations from exchangeability. This is introduced specificly to the field of computational
toxicology and applied to Tox21 datasets: An approach to improve applicability of CP models to new data by updating
the calibration set with more recent data.
