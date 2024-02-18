Script 5
==============

Result
--------

RSU vs. theta plot for the following rings:

- syn-S-2
- syn-S-1
- syn-T-1
- minimum RSU of dimeric rings

.. image:: ../_static/images/script5.png
   :align: center


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
   
   python3 script5.py

Another window will pop up, showing a plot like the one in the figure above. The plot will be interactive, so you can zoom in, pan, etc.

Source code
------------

.. literalinclude:: ../../../reprod/script5.py
   :language: python

.. seealso::

   For further details about the functions used in this script, please refer to the documentation:

   - :func:`rsuanalyzer.create_rsu_vs_theta_df <rsuanalyzer.analyze_rsu.calc_rsu_vs_theta.create_rsu_vs_theta_df>`
   - :func:`rsuanalyzer.enum_ring_ids <rsuanalyzer.enum_ring_ids.enum_ring_ids>`
   - :func:`rsuanalyzer.create_min_rsu_vs_theta_df <rsuanalyzer.analyze_rsu.calc_min_rsu_vs_theta.create_min_rsu_vs_theta_df>`
   - :func:`rsuanalyzer.plot_rsu_vs_theta <rsuanalyzer.analyze_rsu.plot_rsu_vs_theta.plot_rsu_vs_theta>`
