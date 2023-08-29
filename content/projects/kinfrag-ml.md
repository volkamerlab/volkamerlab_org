---
title: "KinfragML"
date: 2023-08-25T09:28:13+02:00
weight: 10
nav: false
# Uncomment sections below to enable them in your project
# external_resources:
# - name: Software name
#   link: https://github.com/volkamerlab/KinFragLib
#   icon: github # (use fa-* FontAwesome icons)
people:  # take from /data/team/members.yml (`key` entry)
- key: paula.kramer
- key: andrea.volkamer
# collaborators:
# - name: Firstname Lastname
#   link: http://university.website
#   more: (Department X this is free text)
funding:
- name: NextAID
  link: https://nextaid.cs.uni-saarland.de/
#   more: free text
# publications:  # take from (or add to) /data/publications/publications.yml
# - citation_key
# - citation_key
---

In this project, we work with the protein kinase family, since they are involved in many diseases which make them an interesting drug target. The aim is to generate novel ligands as potential drug candidates for kinases using generative deep learning. The model includes structural information on the kinase binding pocket, since it is well studied and well conserved across protein kinases. We tackle the problem of ligand generation in a fragment-based approach by including domain-knowledge to increase kinase affinity and synthesizability in general.

<!--more-->

We take the fragment library [KinFragLib](https://volkamerlab.org/projects/kinfraglib/)  as a starting point, which fragments kinase ligands and assigns a subpocket to each fragment. We then extended the fragmentation library with [kinodata](https://volkamerlab.org/projects/kinoml/), where we docked and fragmented ligands known to interact with kinases. Finally we use graph-based deep learning for the recombination of fragments in a step-by-step manner. With this approach we incorporate subpocket information in the model to generate kinase-focused ligands. 

