---
title: Machine Learning methods
date: 2020-03-03
publishdate: 2020-03-03
menu:
    main:
        parent: Research
        name: Machine Learning
weight: 20
nav: false
---

{{< box "Some more general ML info here!" >}}

Machine learning models should not only be well-performing. It is also important to know if the models can be applied
to a certain dataset and if (how much) we can trust the predictions. This can be approached with conformal prediction,
a recently promoted method for confidence estimation. A conformal predictor returns, whether enough evidence is given
to reliably assign the query substance to a certain class. The conformal prediction framework is built on top of
machine learning models, but includes an additional calibration step. Thus, predictions made for a query compound
are compared to those made for the calibration set compounds.

{{< xfigure src="/images/research/conformal_prediction.png" caption="Conformal Prediction" imageclass="fit" >}}


## [ML-based toxic endpoint prediction](/research/machine-learning/toxicity/)

{{% intro "/research/machine-learning/toxicity.md" %}}

## [Deep learning based virtual screening](/projects/deeplearning-vs/)

{{% intro "/projects/deeplearning-vs.md" %}}

## See also

* [KinoML](/projects/kinoml/)