---
title: Historical Virtual Control Groups
date: 2021-12-01
publishdate: 2021-12-01
weight: 10
nav: false
draft: false
people:  # take from /data/team/members.yml (`key` entry)
- key: alexander.gujarnov
- key: andrea.volkamer
collaborators:
- name: Joerg Wichard
  link: https://www.bayer.com/
  more: In-silico Toxicology department, Pharmaceutical division, Berlin, Bayer AG
- name: Lea Vaas
  link: https://www.bayer.com/
  more: Senior statistician, Berlin, Bayer AG
- name: Annika Kreuchwig
  link: https://www.bayer.com/
  more: Digital Expert Toxicology, Berlin, Bayer AG
- name: Thomas Steger-Hartmann
  link: https://www.bayer.com/
  more: Head of Investigational Toxicology, Berlin, Bayer AG
- name: Gerhard Wolber
  link: https://www.bcp.fu-berlin.de/pharmazie/faecher/pharmazeutische_chemie/wolber/index.html
  more: Professor, Molecular Design Lab, Freie Universität Berlin
- name: The partners of the eTRANSAFE team
  link: https://etransafe.eu/partners-etransafe/
  more:  
funding:
- name: Innovative Medicines Initiative (IMI), eTRANSAFE project, Grant 777365.

---

Historical Virtual Control Groups: one step forward into the future of animal testing in toxicology. Our goal is to reduce the number of animals used in experiments. Starting with an exceptional dataset provided by members of the eTRANSAFE consortium we start the journey into the future of animal testing via derivation and incorporation of virtual control groups in animal testing approaches and thus enabling a 3R strategy.

<!--more-->

Historical control databases are established by many companies (i) enabling contextualization of results from single studies against previous studies performed under similar conditions, (ii) to properly design studies and/or (iii) to come up with quality control instruments. Although the use of historical control data in supporting inferences varies across different assays; one major opportunity is the derivation of so-called Virtual Control Groups (VCGs [Wichard, 2020](https://www.altex.org/index.php/altex/article/view/1728)) for replacement of animals in the control groups and thus enabling a 3R strategy for future animal testing approaches.

A multi-disciplinary cross-industry and cross-academic team of statisticians, toxicologists and data-scientists from Merck, Roche, Novartis, Bayer und Sanofi has been established and coordinates the data collection process among the eTRANSAFE partners. A thorough quality control will be performed to identify, extract, and purify all the datapoints which will then be used for the model building (see Steger-Hartmann et. al (2020)). The model itself will be benchmarked and evaluated with concurrent data to determine its reliability and applicability domain. Finally, we will approach regulatory authorities in order to discuss VCGs as an acceptable method to replace control-group-animals in toxicity studies.

{{< xfigure src="/images/research/VCGs.png" caption="Workflow of the implementation of the VCG project, taken from the [eTRANSAFE](https://etransafe.eu/virtual-control-groups-one-step-forward-into-the-future-of-animal-testing-in-toxicology/). After a quality control of the database, various models for generating virtual control groups will be developed and their performance will be benchmarked to determine the reliability of the models with respect to the applicability domain. In parallel to the development, advice from the regulatory authorities will be searched in order to ensure an early-on acceptance for implementing virtual control groups." imageclass="fit" >}}

[Back to machine-learning based research](/research/machine-learning/)