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
- name: TeachOpenCADD for Jupyter
  link: https://github.com/volkamerlab/TeachOpenCADD
  icon: github
  more: Jupyter notebooks on computer-aided drug design tasks using open resources
- name: TeachOpenCADD for KNIME
  link: https://hub.knime.com/volkamerlab/spaces/Public/latest/TeachOpenCADD/TeachOpenCADD
  more: KNIME workflows on computer-aided drug design tasks using open resources
people:
- key: dominique.sydow
- key: jaime.rodriguez
- key: michele.wichmann
- key: andrea-lilian.morger
- key: maximilian.driller
- key: andrea.volkamer
collaborators:
- name: Gregory Landrum
  more: KNIME AG
- name: Daria Goldmann
  more: KNIME GmbH
funding:
- name: Bundesministerium für Bildung und Forschung, grant ID 031A262C
- name: Deutsche Forschungsgemeinschaft (DFG), grant ID VO 2353 / 1-1
- name: HaVo-Stiftung, Ludwig-shafen, Germany
- name: Open Access Publication Fund of Charité – Universitätsmedizin Berlin
- name: Stiftung Charité (Einstein BIH Visiting Fellow Project)
- name: “SUPPORT für die Lehre” program (Förderung innovativer Lehrvorhaben) of Freie Universität Berlin.
publications:
- teachopencaddknime
- teachopencadd
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

{{< xfigure src="/images/research/teachopencadd_topics1-10.png" caption="Topics 1-10 have been designed as a step-by-step pipeline" imageclass="fit" >}}

### TeachOpenCADD topics

TeachOpenCADD offers teaching material on common tasks in computer-aided drug design. Currently, the following topics are available:

##### Cheminformatics

1. Compound data acquisition: ChEMBL
2. Molecular filtering: ADME and lead-likeness criteria
3. Molecular filtering: Unwanted substructures
4. Ligand-based screening: Compound similarity
5. Compound clustering
6. Maximum common substructures
7. Ligand-based screening: Machine learning

##### Structural bioinformatics

8. Protein data acquisition: Protein Data Bank (PDB)
9. Ligand-based pharmacophores
10. Binding site similarity

<!-- 11. Structure-based CADD using online APIs/servers -->
<!-- * Querying KLIFS & PubChem for potential kinase inhibitors -->
<!-- * Docking the candidates against the target -->
<!-- * Visualizing the results and comparing against known data -->

<!-- {{< xfigure src="/images/research/teachopencadd_topics11.png" caption="Topic 11" >}} -->

Topics 1-10 are available as Python-based Jupyter notebooks and topics 1-8 can additionally be used in the form of KNIME workflows.
