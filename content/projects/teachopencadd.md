---
title: TeachOpenCADD
date: 2020-03-03
publishdate: 2020-03-03
nav: false
weight: 1
menu:
    main:
        parent: Education
external_resources:
- name: TeachOpenCADD website
  link: https://projects.volkamerlab.org/teachopencadd/
  icon: globe
  more: Main website for the TeachOpenCADD platform
- name: TeachOpenCADD for Jupyter
  link: https://github.com/volkamerlab/TeachOpenCADD
  icon: github
  more: Jupyter notebooks on computer-aided drug design tasks using open resources
- name: TeachOpenCADD for KNIME
  link: https://hub.knime.com/volkamerlab/spaces/Public/latest/TeachOpenCADD/TeachOpenCADD
  icon: globe
  more: KNIME workflows on computer-aided drug design tasks using open resources
people:
# List here everyone who co-authored TOC publications and is/was a Volkamer Lab member
- key: dominique.sydow
- key: jaime.rodriguez
- key: andrea.volkamer
- key: talia.kimber
- key: david.schaller
- key: corey.taylor
- key: yonghui.chen
- key: michele.wichmann
- key: mareike.leja
- key: sakshi.misra
- key: andrea-lilian.morger
- key: maximilian.driller
- key: armin.ariamajd
- key: michael.backenkoehler
- key: paula.kramer
- key: floriane.odje
- key: hamza.ibrahim
collaborators:
# List here everyone who co-authored TOC publications outside of the Volkamer Lab
- name: Greg Landrum
  more: KNIME
- name: Daria Goldmann
  more: KNIME
- name: Joschka Groß
- name: Gerrit Großmann
- name: Roman Joeres
- name: Azat Tagirdzhanov
- name: Verena Wolf
funding:
- name: Note that the TeachOpenCADD project has been a group effort and has received no explicit funding, while the positions of individual authors were supported by diverse funding agencies, see the individual projects' pages.
publications:
- bachenkoehler_chemrxiv_2023		
- sydow_nar_2022
- teachopencaddknime
- teachopencadd
- sydow_acs_2021
# You can use this keyword for the brief introductions to the article in category listings
# This will replace the first 70 words found in the main article. use | <newline> to use multiline strings!
summary: |
  TeachOpenCADD is a teaching platform offering tutorials on central topics in cheminformatics and structural bioinformatics.
  The tutorials contain theoretical background and practical implementations using open source data and software.
  Implementations are available in two formats: Python-based Jupyter notebooks and GUI-based KNIME workflows.
---

Open source data and software are increasingly generated, developed and used in computer-aided drug design (CADD).
This development allows to build modular pipelines for reproducible and reusable research as well as
to explore and contribute to open software code.
While code and usage of such software is usually well documented,
its full potential for CADD projects often remains unreached, especially for beginners,
due to the lack of application examples combining different toolkits.

TeachOpenCADD is a teaching platform offering tutorials on central topics in cheminformatics and structural bioinformatics.
The tutorials contain theoretical background and practical implementations using open source data and software.
Implementations are available in two formats: On the one hand, interactive *Jupyter notebooks* demonstrate how to set up code-based pipelines (Python).
On the other hand, the same topics are transformed into *KNIME workflows*, an alternative to code-based workflows.
Here, an intuitive, drag-and-drop style graphical interface is used to string together pre-implemented code units
(nodes) with standardized functionalities.

TeachOpenCADD is suitable for self-study training and classroom teaching, but can also serve as a starting point in
research projects.
The platform is freely available on GitHub and open to contributions from the community.

{{< xfigure src="/images/research/teachopencadd_topics.png" caption="The TeachOpenCADD platform offers tutorials covering a step-by-step pipeline to propose novel EGFR kinase inhibitors with concepts from cheminformatics (green), structural bioinformatics (orange) and online webserver queries (blue). Talktorials also cover different kinase similarity measures (yellow) and an introduction to deep learning (purple)." imageclass="fit" >}}
