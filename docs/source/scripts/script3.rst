Script 3
==============

Result
--------

Table of the calculated RSU values for the different ring conformations of the Pd6L4, Pd9L6 and Pd12L8 complexes.

- syn-T-1  (:math:`\theta` = 0°)
- 1,3-alt-S  (:math:`\theta` = 0°)
- syn-T-1  (:math:`\theta` = 34°)
- syn-S-2  (:math:`\theta` = 30°)
- syn-S-1  (:math:`\theta` = 38°)

.. csv-table:: 
   :file: ../_static/csv/script3.csv
   :header-rows: 1


How to run the script?
-----------------------

Prerequisites
^^^^^^^^^^^^^^

- If you haven't installed the package yet, install it by following the instructions in the :doc:`installation guide <../installation>`.

- If the virtual environment is not activated, activate it. (For more information see :doc:`../appendix/venv`)


Running the script
^^^^^^^^^^^^^^^^^^

Go to the directory where the script is located (``rsu-project/reprod``) and run the following command:

.. code-block:: bash
   
   python3 script3.py

This will show the following output:

.. code-block:: none

            name           ring_id  theta    rsu                         description
   0    syn-T-1      RLFFRLFFRLFF      0  0.243  three membered ring in Pd6L4 (L=1)
   1  1,3-alt-S  RRFFRRBBRRFFRRBB      0  0.284   four membered ring in Pd6L4 (L=1)
   2    syn-T-1      RLFFRLFFRLFF     34  0.220  three membered ring in Pd9L6 (L=2)
   3    syn-S-2  RRFBRLBBRRFBRLBB     30  0.470   four membered ring in Pd9L6 (L=2)
   4    syn-S-1  RRFFLLBBRRFFLLBB     38  0.010  four membered ring in Pd12L8 (L=2)


Source code
------------

.. literalinclude:: ../../../reprod/script3.py
   :language: python

.. seealso::

   For further details about the functions used in this script, please refer to the documentation:

   - :func:`rsuanalyzer.calc_rsu <rsuanalyzer.core.calc_rsu.calc_rsu>`
