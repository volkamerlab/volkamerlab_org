---
title: "Cytotoxicity"
date: 2020-05-14T16:55:38+02:00
nav: false
draft: false
people:
- key: talia.kimber
- key: henry.webel
- key: andrea.volkamer
collaborators:
- name: Silke Radetzki
  link: https://www.leibniz-fmp.de/home
  more: FMP
- name: Martin Neuenschwander
  link: https://www.leibniz-fmp.de/home
  more: FMP
- name: Marc Nazaré
  link: https://www.leibniz-fmp.de/home
  more: FMP
funding:
- name: Bundesministerium für Bildung und Forschung, Grant 031A262C
- name: Stiftung Charité (Einstein BIH Visiting Fellow Project)
publications:
- webel_2019_cytotox

summary: |
  In this project, cytotoxicity prediction, one of the earliest handles in drug discovery, is investigated using a deep learning approach trained on a large and highly consistent in-house data set from the FMP. While neural networks are often described as a black box, we try to overcome the lack of interpretability. Thus, a Deep Taylor Decomposition method is investigated to identify substructures that may be responsible for the cytotoxic effects.
---

In drug development, late stage toxicity issues of a compound are the main cause of failure in clinical trials. _In silico_ methods are therefore of high importance to guide the early design process to reduce time, costs and animal testing.

In this project, cytotoxicity prediction, one of the earliest handles in drug discovery, is investigated using a deep learning approach trained on a highly consistent in-house data set of over 34,000 compounds from the <a href="https://www.leibniz-fmp.de/home" target="_blank" class="external">FMP</a>.
Albeit yielding good results, neural networks are often described as a black box lacking deeper mechanistic understanding of the underlying model. To overcome this lack of interpretability, a Deep Taylor Decomposition method is investigated to identify substructures that may be responsible for the cytotoxic effects, the so-called toxicophores.

This approach could be helpful in drug development to predict the potential toxicity of a compound as well as to generate new insights into the toxic mechanism. Moreover, it could also help to de-risk and optimize compounds.

{{< xfigure src="/images/research/cytotoxicity.png" caption="Workflow for identifying potential toxicophores." imageclass="fit" >}}
