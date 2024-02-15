.. toctree::
   :maxdepth: 1
   :hidden:

   Calculate RSU <src.calc_rsu>
   Analyze RSU <src.analyze_rsu>
   Enumerate rings <src.enum_ids>
   Visualize chain <src.visualize_chain>


.. image:: _static/images/header.png
   :align: center


RSU Analyzer
========================================

RSU Analyzer is a Python project developed by Hiraoka Laboratory at The University of Tokyo for the scientific paper titled: **Rational design of metal-organic cages to increase the number of components via dihedral angle control** by T. Abe, K. Takeuchi, and S. Hiraoka. (DOI: `10.26434/chemrxiv-2024-m8m60 <https://doi.org/10.26434/chemrxiv-2024-m8m60>`_)

This project focuses on analyzing ring strain per unit (RSU), which acts as an indicator for estimating purely geometric strains in M\ :sub:`n`\ L\ :sub:`n`\  subcomponent rings in M\ :sub:`6`\ L\ :sub:`4`\ , M\ :sub:`9`\ L\ :sub:`6`\ , and M\ :sub:`12`\ L\ :sub:`8`\  assemblies, where L is 1,3,5-tris(4-pyridyl)benzene and M indicates the metal ion that connects two L with an L–M–L angle of 90°. In the analysis, 1,3-di(4-pyridyl)benzene was used as L instead of 1,3,5-tris(4-pyridyl)benzene, and the ring strain was evaluated for M\ :sub:`n`\ L\ :sub:`n`\  rings (*n* = 2–4) with variable L–M–L angles. 

For more detailed information, please refer to the associated research paper. (DOI: `10.26434/chemrxiv-2024-m8m60 <https://doi.org/10.26434/chemrxiv-2024-m8m60>`_)


What RSU Analyzer can do
========================================

- :doc:`Calculate RSU <src.calc_rsu>`

- :doc:`Analyze RSU <src.analyze_rsu>`

- :doc:`Enumerate all possible rings <src.enum_ids>`

- :doc:`Visualize chain using matplotlib 3D plot <src.visualize_chain>`



Indices and tables
====================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
