---
title: "OpenCADD-KLIFS module: KLIFS meets Python!"
date: 2022-02-17T00:00:00+02:00
author: dominique.sydow
---

The [KLIFS](https://klifs.net/) database is a rich resource for datasets focused on kinase pockets, ranging from 
annotated pockets and ligand interaction patterns in experimental PDB structures 
to ligand bioactivity values from the ChEMBL database.

It is possible to explore the KLIFS resource via their web interface online ([NAR 2021](https://doi.org/10.1093/nar/gkaa895)) or locally using dedicated KNIME nodes ([JCIM 2017](https://doi.org/10.1021/acs.jcim.6b00686) and [ChemMedChem 2018](https://doi.org/10.1002/cmdc.201700754) developed by the KLIFS authors.

With OpenCADD-KLIFS, we now add a Python solution for easy and quick integration of KLIFS datasets
into Python-based pipelines. The setup and usage is straight-forward!

1. Install the ``opencadd`` package from ``conda-forge`` and activate the environment:
    ```
    mamba create -n opencadd opencadd
    conda activate opencadd
    ```
2. Set up a KLIFS session:
    ```
    from opencadd.databases.klifs import setup_remote
    session = setup_remote()
    ```
3. All KLIFS resources are now at your fingertips. For example, you can fetch the metadata to all KLIFS-deposited kinases or kinase structures:
    ```
    session.kinases.all_kinases()
    session.structures.all_structures()
    ```

Read more about all OpenCADD-KLIFS features in our [JOSS publication](https://joss.theoj.org/papers/10.21105/joss.03951) and our [OpenCADD-KLIFS documentation](https://opencadd.readthedocs.io/en/latest/databases_klifs.html).

This Python package was developed in the Volkamer Lab by {{< person "dominique.sydow" >}}, {{< person "jaime.rodriguez" >}}, and {{< person "andrea.volkamer" >}}. Special thanks to Albert Kooistra for his work on the KLIFS database and his support with questions we encountered during the developement of OpenCADD-KLIFS.
