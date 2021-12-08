---
title: "TeachOpenCADD 2021 release is out!"
date: 2021-12-07T00:00:00+02:00
author: dominique.sydow
---

## Have you heard of TeachOpenCADD?

- Yes? Perfect, we have good news! We are back with more content (12 fresh new notebooks!), a new website, simplified installation options, and much, much more.

- No, you haven't? Well, we are happy you found your way here!

We will show you what TeachOpenCADD as to offer and tell you more about the exciting details on the new release!

## How did it start?

In 2019, [we launched TeachOpenCADD](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x), a teaching platform for cheminformatics and structural bioinformatics that show-cases how to perform central tasks in computer-aided drug design.

- We are using only open source Python packages and data resources. **This setup makes the material accessible to everyone.**
- Each topic is covered in a Jupyter notebook always following the same aim-theory-code-discussion-quiz scheme. **This all-in-one approach makes the topics comprehensible to users from all backgrounds.** Thanks to this setup, these tutorials are also suitable for oral presentations, hence we call them talktorials (talk + tutorial).
- TeachOpenCADD is used by students and scientists who seek to learn or [teach](https://pubs.acs.org/doi/abs/10.1021/bk-2021-1387.ch010) these topics, or who need a workflow template for their own research.
- For users who prefer GUI-based pipelines, we offer [TeachOpenCADD-KNIME](https://pubs.acs.org/doi/10.1021/acs.jcim.9b00662) workflows for some of the topics on the [KNIME Hub](https://hub.knime.com/volkamerlab/spaces/Public/latest/TeachOpenCADD/TeachOpenCADD).

## TeachOpenCADD's 2021 release

These are the top 3 major updates in this release:

- New [website](https://projects.volkamerlab.org/teachopencadd/) for read-only browsing of our content!
- More topics &mdash; [now in total 22](https://projects.volkamerlab.org/teachopencadd/all_talktorials.html) &mdash; covering cheminformatics, structural bioinformatics, and online queries!
- Easy local [installation](https://projects.volkamerlab.org/teachopencadd/installing.html) via our `conda` package for users who want to execute and modify the talktorials!

You heard enough? Great, enjoy our website! &mdash; You are interested in more details? Wonderful, please read on.

## New website and content

Since 2019, we have been working a lot on extending and improving our material. Let's start with the feature that will make all our material much easier and quicker to access - our new [website](https://projects.volkamerlab.org/teachopencadd/)!

The website hosts a static view of all our Jupyter notebooks, which makes browsing through the TeachOpenCADD content convenient, fast, and searchable. We extended our cheminformatics-focused 2019 release with a lot of new topics from structural bioinformatics; and we demonstrate in detail how to query different online resources from within a Python pipeline.

### Querying online APIs/servers from Python

- `T011` Querying online API webservices
- `T001` Data acquisition from ChEMBL
- `T008` Data acquisition from PDB
- `T012` Data acquisition from KLIFS
- `T013` Data acquisition from PubChem

### Cheminformatics

Mostly powered by the [RDKit](https://www.rdkit.org/)!

- `T002` ADME and lead-likeness criteria
- `T003` Unwanted substructures
- `T004` Compound similarity
- `T005` Compound clustering
- `T006` Maximum common substructure
- `T007` Ligand-based screening: Machine learning
- `T009` Ligand-based pharmacophores
- `T021` One-hot encoding
- `T022` Ligand-based screening: Neural networks

### Structural bioinformatics

- `T010` Binding site similarity and off-target prediction
- `T014` Binding site detection ([Proteins.Plus](https://proteins.plus/))
- `T015` Protein ligand docking ([smina](https://sourceforge.net/p/smina/discussion/))
- `T016` Protein-ligand interactions ([PLIP](https://github.com/pharmai/plip))
- `T017` Advanced NGLview usage ([NGLview](https://github.com/nglviewer/nglview))
- `T018` Automated pipeline for lead optimization
- `T019` Molecular dynamics simulation ([OpenMM](https://openmm.org/))
- `T020` Analyzing molecular dynamics simulations ([MDAnalysis](https://www.mdanalysis.org/))


## TeachOpenCADD and FAIR principles

Since the platform has been growing and will continue to grow, we set up a continuous integration (GitHub Actions) that tests all notebooks &mdash; thank you `pytest` and `nbval` &mdash; on a regular basis to ensure functional, reusable, and reproducible pipelines.

We love open research. We comply with the FAIR principles for for [data](https://www.nature.com/articles/sdata201618) and [software](https://content.iospress.com/articles/data-science/ds190026) as follows:

- findable &mdash; our code is registered on GitHub and `conda-forge`
- accessible &mdash; our code and all its dependencies are free to download
- interoperable &mdash; we support Windows, Linux, and MacOS for Python >= 3.7; dependencies are defined and managed within the `conda` ecosystem
- reusable &mdash; re-use is easy thanks to our `conda` package (CY BB 4.0 licence); maintenance is monitored by our continuous integration

## Contributors

This new TeachOpenCADD release was possible thanks to  huge contributions from Jaime Rodríguez-Guerra, Talia B. Kimber, David Schaller, Corey J. Taylor, Yonghui Chen, Mareike Leja, Sakshi Misra, Michele Wichmann, Armin Ariamajd, and Andrea Volkamer. It was a pleasure working with you all on this next milestone!

Futhermore, we thank Piedro Gerletti, Ahmed Atta, Melanie Vogel, Abishek Laxmanan Ravi Shankar, and Maria Trofimova for their work on initial drafts for new talktorials; and we thank Jeffrey R. Wagner, Richard Gowers, and Floriane Montanari for their support on improving code and testing of TeachOpenCADD.

TeachOpenCADD relies on external resources; we thank the Patrick Kunzmann (biotite), Albert Kooistra (KLIFS), and Hai Nguyen (NGLview) for their help with questions and issues.