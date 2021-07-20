---
title: "KinoML"
date: 2020-03-05T22:14:45+01:00
nav: false
draft: false
# Uncomment sections below to enable them in your project
external_resources:
- name: KinoML repository
  link: https://github.com/openkinome/kinoml
  icon: github
- name: KinoML documentation
  link: https://openkinome.github.io/kinoml/
  icon: book
people:
- key: jaime.rodriguez
- key: talia.kimber
- key: david.schaller
  more: "([MIAME](/projects/miame/))"
- key: corey.taylor 
- key: andrea.volkamer
collaborators:
- name: John D. Chodera
  link: http://choderalab.org
  more: MSKCC
funding:
- name: The Einstein Foundation & Stiftung Charité
  link: https://www.einsteinfoundation.de/en/programmes/einstein-bih-visiting-fellow/
  more: BIH Einstein Visiting Fellowship
publications:
# - proteinsplus2017
---

In this project, we aim to combine structure-enabled machine learning and alchemical free energy calculations to develop a predictive quantitative model to rapidly assess kinase inhibitor affinity and selectivity, design ligands with desired selectivity profiles and assess the impact of clinical point mutations on inhibitor binding.

<!--more-->

{{< xfigure src="/images/research/kinoml.jpg" caption="Small inhibitors targeting kinases can have a wide scope of activity given the conserved ATP-binding pocket across the kinome. Using structure-informed machine learning, we intend to decode the interactions driving the design of promising compounds with intended polypharmacology." imageclass="fit" >}}

The resulting `kinoml` package provides a modern Python library to help build flexible pipelines for machine learning in the context of structural bioinformatics. More information on how to use install it and use it for your research can be found on the {{< external "official documentation" "https://openkinome.github.io/kinoml/" >}}.
