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
  more: (<a href="https://www.basf.com/" target="_blank" class="external">BASF</a>)
- name: Janosch Achenbach
  more: (<a href="https://www.basf.com/" target="_blank" class="external">BASF</a>)
- name: Robert Landsiedel
  more: (<a href="https://www.basf.com/" target="_blank" class="external">BASF</a>)
- name: Roland Buesen
  more: (<a href="https://www.basf.com/" target="_blank" class="external">BASF</a>)
- name: Antje Wolf
  more: (<a href="https://www.basf.com/" target="_blank" class="external">BASF</a>)
- name: Klaus-Juergen Schleifer
  more: (<a href="https://www.basf.com/" target="_blank" class="external">BASF</a>)


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
- name: We thank BASF for financial support

summary: |
  KnowTox is a novel pipeline that combines three different _in silico_ toxicology approaches to allow for confident prediction of potentially toxic effects of novel chemical entities, i.e. machine learning models, alerts for toxic substructures and computational support for read-across.
---

Computational tools for toxicity prediction are promising in the process of reducing, refining and replacing animal testing. To assess the toxicity of novel chemical entities, regulatory agencies require in vivo testing for several toxic endpoints. In 2017, roughly 9.39 million laboratory animals have been deployed in the European Union, of which 2.19 million were used for regulatory testing purposes (~11% of those for testing industrial chemicals; source: {{< external "European Commision Report" "https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1581689520921&uri=CELEX:52020DC0016">}}). Thus, the establishment of alternative methods, and with it the reduction of animal testing, is of utmost importance.

While grouping of molecules and read-across are already the most widely used non-animal methods ({{< external "ECHA" "https://echa.europa.eu/-/alternatives-to-animal-testing-continue-to-be-widely-used" >}}), *KnowTox* is a novel pipeline that combines three different _in silico_ toxicology approaches to allow for confident prediction of potentially toxic effects of novel chemical entities. KnowTox combines machine learning models, alerts for toxic substructures and computational support for read-across.

{{< xfigure src="/images/research/knowtox.jpg" caption="Overview of KnowTox. Combining toxicity information from different sources, the complementary outputs of the KnowTox tool help to generate a holistic toxicity prediction picture for a novel query compound (figure taken from [Morger, 2020](/publications/#morger_2020_knowtox))." imageclass="fit" >}}

When applying machine learning models, applicability and reliability of predictions for new chemicals are much needed. This was approached using conformal prediction. Several adaptions of the framework were investigated to improve the model performance (i.e. KNN normalization and balancing of proper training set). The different model set-ups were validated using androgen receptor antagonism datasets.

<!-- TODO : add something about read across and structural alerts? -->

#### Excursus on Conformal Prediction

Conformal prediction is a recently promoted method for confidence estimation. A conformal predictor returns, whether enough evidence is given to reliably assign the query substance to a certain class. The conformal prediction framework is built on top of machine learning models, and includes an additional calibration step. Thus, predictions made for a query compound are compared to those made for the calibration set compounds.

{{< xfigure src="/images/research/conformal_prediction.jpg" caption="Overview of the conformal prediction (classification) framework. The green bar highlights the KNN Regressor normaliser model introduced in KnowTox (figure taken from [Morger, 2020](/publications/#morger_2020_knowtox))." imageclass="fit" >}}
