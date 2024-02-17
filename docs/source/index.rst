.. RSU Project documentation master file, created by
   sphinx-quickstart on Sat Feb 17 16:15:43 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: _static/images/header.png
   :align: center

RSU Project
=======================================

.. toctree::
   :maxdepth: 1
   :hidden:

   installation
   reprod
   rsuanalyzer


About
----------------------------------------
This is a Python project developed by Hiraoka Laboratory at The University of Tokyo for the scientific paper titled: **Rational design of metal-organic cages to increase the number of components via dihedral angle control** by T. Abe, K. Takeuchi, and S. Hiraoka. (DOI: `10.26434/chemrxiv-2024-m8m60 <https://doi.org/10.26434/chemrxiv-2024-m8m60>`_)

This project focuses on analyzing Ring Strain per Unit (RSU), which acts as an indicator for estimating purely geometric strains in M\ :sub:`n`\ L\ :sub:`n`\  subcomponent rings in M\ :sub:`6`\ L\ :sub:`4`\ , M\ :sub:`9`\ L\ :sub:`6`\ , and M\ :sub:`12`\ L\ :sub:`8`\  assemblies, where L is 1,3,5-tris(4-pyridyl)benzene and M indicates the metal ion that connects two L with an L–M–L angle of 90°. In the analysis, 1,3-di(4-pyridyl)benzene was used as L instead of 1,3,5-tris(4-pyridyl)benzene, and the ring strain was evaluated for M\ :sub:`n`\ L\ :sub:`n`\  rings (*n* = 2–4) with variable L–M–L angles. For more detailed information, please refer to the paper. 


What can you do with the RSU Project?
----------------------------------------
You can use the RSU Project to:

- Reproduce the results presented in the paper (see :doc:`Reproducing the Results <reprod>` section)
- Conduct your own analysis with the RSU Analyzer package (see :doc:`Using the RSU Analyzer <rsuanalyzer>` section)


Installation
----------------------------------------
To install the RSU Project, please follow the instructions in the :doc:`Installation <installation>` section.



Indices and tables
-------------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
