RSU Analyzer
===================
This package provides tools for calculating and analyzing RSU, and visualizing chains.

.. toctree::
   :maxdepth: 2
   :hidden:

   rsuanalyzer/instruction
   rsuanalyzer/modules

.. role:: python(code)
   :language: python


Examples
-------------
Here are some examples of how to use the package.


1. Calculate RSU
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To calculate the RSU, you can use the following code:

.. code-block:: python

   import rsuanalyzer as ra

   ans = ra.calc_rsu("RLFFRLFFRLFF", 34)

   print(ans)
   
The result is below.

.. code-block:: python

   0.2200836694739778

In this example, the RSU of the trimeric ring "RLFFRLFFRLFF" with theta of 34 degrees is calculated. Delta is set to 87 degrees by default, but you can change it by specifying the delta argument, e.g., :python:`ra.calc_rsu("RLFFRLFFRLFF", 34, 90)`.

.. note::
   For more information, please refer to the documentation of the function. :func:`rsuanalyzer.core.calc_rsu.calc_rsu` 


2. Make a Ranking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
First example is to make an RSU rank table.

.. code-block:: python

   import rsuanalyzer as ra

   # Enumerate all trimeric ring IDs
   trimeric_rings = ra.enum_ring_ids(3)

   # Create ranking. (theta=40, delta=87, num_top=5)
   df = ra.create_small_rsu_ranking(trimeric_rings, 40, 87, 5)

   # Save the ranking to a csv file
   df.to_csv("top5_trimeric_theta40.csv")

The result is shown below.

.. csv-table:: 
   :file: _static/csv/top5_trimeric_theta40.csv
   :header-rows: 1

.. note::
   See the documentation of the functions for more information. 
      - :func:`rsuanalyzer.create_small_rsu_ranking <rsuanalyzer.analyze_rsu.small_rsu_ranking.create_small_rsu_ranking>`
      - :func:`rsuanalyzer.enum_ring_ids <rsuanalyzer.enum_ring_ids.enum_ring_ids.enum_ring_ids>`


3. Make a Plot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Second example is to make a plot of RSU vs. theta.

.. code-block:: python

   import rsuanalyzer as ra

   # Create a pandas.DataFrame of RSU vs. theta
   df1 = ra.create_rsu_vs_theta_df("RLFFRLFFRLFF")

   # Plot RSU vs. theta
   ra.plot_rsu_vs_theta(df1, labels=["syn-T-1"])

The result is shown below.

.. image:: _static/images/rsu_vs_theta_of_syn-T-1.png
   :align: center



4. Visualize Chains
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can visualize chains using the following code:

.. code-block:: python

   import rsuanalyzer as ra

   # Create a chain
   ra.visualize_chain("RRFFLLBBRRFFLLBB", 34, 87)

The result is shown below.

.. image:: _static/images/visualized_syn-S-1.png
   :align: center
