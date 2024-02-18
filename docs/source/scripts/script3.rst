Script 3
==============

Result
--------

CSV file with the following data:

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

The result will be saved in the same directory in a file called ``script3.csv``.

Source code
------------

.. literalinclude:: ../../../reprod/script3.py
   :language: python

.. seealso::

   For further details about the functions used in this script, please refer to the documentation:

   - :func:`rsuanalyzer.calc_rsu <rsuanalyzer.core.calc_rsu.calc_rsu>`
