---
title: "Knowtox"
date: 2020-05-20T16:27:08+02:00

menu:
    main:
        parent: Projects
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
  more: In the notebook it is demonstrated how a conformal predictor is built, applied to make predictions for external
   data, and how to evaluate the internal (crossvalidation) and external predictions.

funding:
- name: Bundesministerium für Bildung und Forschung, grant ID 031A262C
  link: "#"
- name: HaVo-Stiftung
  link: "#"
---
((Move this part to the research page 'in silico toxicity' or 'toxicity prediction':)) 
The project is part of the BMBF-funded BB3R initiative. One major goal of the BB3R initiative is the establishment of 
alternative methods for preclinical drug development and basic research. To assess the toxicity of novel chemical 
entities, regulatory agencies require in-vivo testing for several toxic endpoints. In 2010, roughly 2.9 million 
laboratory animals have been deployed in Germany, with an increase of 6% since 2008. Thus, the establishment of
 alternative methods, and with it the reduction of animal testing, is of utmost importance. Determining the toxicity 
 of compounds is vital to identify their harmful effects on humans, animals, plants and the environment.
 
((Move this part to the research page 'machine learning' or 'conformal prediction' - including the figure:))
Machine learning models should not only be well-performing. It is also important to know if the models can be applied 
to a certain dataset and if (how much) we can trust the predictions. This can be approached with conformal prediction,
a recently promoted method for confidence estimation. A conformal predictor returns, whether enough evidence is given
to reliably assign the query substance to a certain class. The conformal prediction framework is built on top of 
machine learning models, but includes an additional calibration step. Thus, predictions made for a query compound
are compared to those made for the calibration set compounds.
{{< xfigure src="/images/research/conformal_prediction.png" caption="Conformal Prediction" imageclass="fit" >}}


KnowTox is a novel pipeline that combines three different in silico toxicology approaches to allow for confident 
prediction of potentially toxic effects of query compounds, i.e. machine learning models, alerts for toxic 
substructures and computational support for read-across. When applying machine learning models, applicability
and reliability of predictions for new chemicals are of utmost importance. This was approached using conformal
prediction. Several adaptions of the framework were investigated and proposed (i.e. KNN normalisation and 
balancing of proper training set) to improve the model performance. The model set-ups were validated using androgen 
receptor antagonism datasets.

The KnowTox pipeline is available within our group and we are happy to apply it in collaboration projects.


{{< xfigure src="/images/research/knowtox.png" caption="KnowTox" imageclass="fit" >}}
