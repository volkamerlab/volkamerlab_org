---
title: "KnowTox"
date: 2020-05-20T16:27:08+02:00

weight: 10
nav: false

people:
- key: andrea-lilian.morger
- key: andrea.volkamer

collaborators:
- name: Miriam Mathea
  link: https://www.basf.com/
- name: Janosch Achenbach
  link: https://www.basf.com/
- name: Robert Landsiedel
  link: https://www.basf.com/
- name: Roland Buesen
  link: https://www.basf.com/
- name: Antje Wolf
  link: https://www.basf.com/
- name: Klaus-Juergen Schleifer
  link: https://www.basf.com/


publications:
- morger_2020_knowtox

external_resources:
- name: knowtox_manuscript_SI
  link: https://github.com/volkamerlab/knowtox_manuscript_SI
  icon: github
  more: SI notebook - build & evaluate conformal predictor and apply to external data

funding:
- name: Bundesministerium für Bildung und Forschung, grant ID 031A262C
- name: HaVo-Stiftung
- name: We thank BASF for supporting this project by providing financial resources

summary: |
  KnowTox is a novel pipeline that combines three different _in silico_ toxicology approaches to allow for confident prediction of potentially toxic effects of novel chemical entities, i.e. machine learning models, alerts for toxic substructures and computational support for read-across.
---

Computational tools for toxicity prediction are promising in the process of reducing, refining and replacing animal testing. To assess the toxicity of novel chemical entities, regulatory agencies require in vivo testing for several toxic endpoints. In 2010, roughly 2.9 million laboratory animals have been deployed in Germany, with an increase of 6% since 2008. Thus, the establishment of alternative methods, and with it the reduction of animal testing, is of utmost importance.

KnowTox is a novel pipeline that combines three different _in silico_ toxicology approaches to allow for confident prediction of potentially toxic effects of novel chemical entities, i.e. machine learning models, alerts for toxic substructures and computational support for read-across.

{{< xfigure src="/images/research/knowtox.png" caption="Overview of KnowTox. Combining toxicity information from different sources, the complementary outputs of the KnowTox tool help to generate a holistic toxicity prediction picture for a novel query compound. (Figure taken from [Morger, 2020](/publications/#morger_2020_knowtox.)" imageclass="fit" >}}

When applying machine learning models, applicability and reliability of predictions for new chemicals are of utmost importance. This was approached using conformal prediction. Several adaptions of the framework were investigated to improve the model performance (i.e. KNN normalization and balancing of proper training set). The different model set-ups were validated using androgen receptor antagonism datasets.

<!-- TODO : add something about read across and structural alerts? -->

#### Excursus on Conformal Prediction

Conformal prediction is a recently promoted method for confidence estimation. A conformal predictor returns, whether enough evidence is given to reliably assign the query substance to a certain class. The conformal prediction framework is built on top of machine learning models, and includes an additional calibration step. Thus, predictions made for a query compound are compared to those made for the calibration set compounds.

{{< xfigure src="/images/research/conformal_prediction.jpg" caption="Overview of the conformal prediction (classification) framework. The green bar highlights the KNN Regressor normaliser model introduced in KnowTox. (Figure taken from [Morger, 2020](/publications/#morger_2020_knowtox.)" imageclass="fit" >}}
