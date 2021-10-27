---
title: "MIAME"
date: 2020-05-29T09:17:30+02:00
nav: false
draft: false
# Uncomment sections below to enable them in your project
# external_resources:
# - name: Software name
#   link: https://github.com/volkamerlab/KinFragLib
#   icon: github # (use fa-* FontAwesome icons)
people:  # take from /data/team/members.yml (`key` entry)
- key: david.schaller
- key: jaime.rodriguez
  more: "([KinoML](/projects/kinoml/))"
- key: talia.kimber
  more: "([KinoML](/projects/kinoml/))"
- key: andrea.volkamer
collaborators:
- name: John D. Chodera
  link: http://choderalab.org
  more: MSK, Einstein BIH Visiting Fellow
- name: Clara Christ
  link: https://www.bayer.com/
  more: Head of Computational Molecular Design, Berlin, Bayer AG
- name: Sikander Hayat
  link: https://www.broadinstitute.org/bios/sikander-hayat
  more: Joint Bayer-Broad cardiovascular precision medicine group
- name: Mark-Christoph Ott
  link: https://www.bayer.com/
  more:
- name: Torben Broemstrup
  link: https://www.bayer.com/
  more:
funding:
- name: We thank Bayer AG for financial support (PostDoc position).
#   link: external website
#   more: free text
# publications:  # take from (or add to) /data/publications/publications.yml
# - citation_key
# - citation_key
summary: |
  In this collaboration with Bayer and the Chodera Lab, we aim to advance and apply [KinoML](/projects/kinoml/) to address pharmaceutically relevant drug design challenges. Special emphasis is put on the effect of point mutations on binding affinity and how these can be exploited to expand the indications of already approved drugs and to guide molecular design.
---

### Mutation Impact Annotation using Modeling and Evolution

In this collaboration with Bayer and the Chodera Lab, we aim to advance and apply [KinoML](/projects/kinoml/), an open source framework integrating structure-informed machine learning and alchemical free energy calculations developed in our group, to address pharmaceutically relevant drug design challenges. Special emphasis is put on the effect of point mutations on binding affinity and how these can be exploited to expand the indications of already approved drugs and to guide molecular design.

#### Extended description

Identifying kinase mutations that could be potential cancer drivers or help tackle drug resistance is a significant challenge in the development of effective cancer treatments. Point mutations in the target of therapy are a major mechanism of resistance, including (1) reducing inhibitor affinity via mutation of residues in direct contact, (2) modulating populations of conformations competent for binding the inhibitor, (3) increasing the affinity for orthosteric substrates that the inhibitor must compete with, or (4) increasing basal activity.

In this research collaboration, we will extend the open source computational tool [KinoML](/projects/kinoml/), which aims to exploit the available structural kinase data, evolutionary information and well-characterized biophysical mechanisms underlying resistance to evaluate the functional impact of point mutations. To do this, we utilize four key technologies: Automated structural modeling to generate conformations that may be significantly populated by the target-inhibitor complex; alchemical free energy calculations to make quantitative predictions regarding the impact of point mutations on affinities, conformational populations, and thermostabilities; structure-enabled machine learning to learn the results of these calculations to rapidly make new predictions.

This project will utilize expertise in structural modeling and structure-enabled machine learning from the Volkamer Lab, and in open source alchemical free energy calculations from the Chodera Lab, combined with real life application knowledge from Bayer.

