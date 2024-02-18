General instruction
==================================================

There are mainly two ways to use the RSU Analyzer package:

1. Use the Python interactive mode
2. Make a Python script and run it


Prerequisites
-------------

In both cases, you need to have the following prerequisites:

- If you haven't installed the package yet, install it by following the instructions in the :doc:`installation guide <../installation>`.

- If the virtual environment is not activated, activate it. (For more information see :doc:`../appendix/venv`)


1. Use the Python interactive mode
-----------------------------------

Introduction to Python interactive mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you are already familiar with Python, you can skip this section.

In this mode, you can directly type the Python commands in the terminal and see the results immediately.

Open a terminal and execute the command :code:`python3` to start the Python interactive mode.

.. code-block:: bash

    % python3
    ... some messages from Python ...
    >>> 

The prompt :code:`>>>` indicates that Python is ready to accept your commands. You can type the Python commands and see the results immediately.

.. code-block:: bash

    >>> 1 + 1
    2
    >>> sum([1, 2, 3, 4, 5])
    15

To exit the Python interactive mode, type :code:`exit()` or press :code:`Ctrl-D`.

.. code-block:: bash

    >>> exit()
    %


Use the RSU Analyzer package in the Python interactive mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Navigate to the ``rsu-project/reprod`` directory, where the ``rsuanalyzer`` package is located.

.. code-block:: bash

    % cd path/to/rsu-project/reprod

Please replace :code:`path/to/rsu-project` with the actual path to the ``rsu-project`` directory.

Start the Python interactive mode.

.. code-block:: bash

    % python3
    ... some messages from Python ...
    >>>

Import the ``rsuanalyzer`` package.

.. code-block:: python

    >>> import rsuanalyzer as ra

This will import the package and make it available as the variable :code:`ra`.

Now you can use the package by typing the commands, for example:

.. code-block:: python

    >>> ra.calc_rsu("RLFFRLFFRLFF", 34)
    0.2200836694739778

or

.. code-block:: python

    >>> ra.visualize_chain("RLFFRLFFRLFF", 34)

This second command will open a window and show the visualization of the RSU chain.

When you are done, you can exit the Python interactive mode by typing :code:`exit()` or pressing :code:`Ctrl-D`.

Variables you define in the interactive mode will be lost when you exit the Python interactive mode. If you want to keep the results, you should save them in a file or use the second method.


2. Make a Python script and run it
-----------------------------------

Create a Python script file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, create a new Python script file, for example, :code:`my_script.py`.
The file can be located anywhere on your computer.

Open the file with a text editor or an integrated development environment (IDE) and write the Python commands in the file.

.. code-block:: python
    :caption: my_script.py

    import sys
    import os

    # Add the path to the rsuanalyzer package to the sys.path
    sys.path.append("path/to/rsu-project/reprod")

    import rsuanalyzer as ra

    print(ra.calc_rsu("RLFFRLFFRLFF", 34))


Please replace :code:`path/to/rsu-project` with the actual path to the ``rsu-project`` directory.

The first three lines are used to add the path to the ``rsuanalyzer`` package to the :code:`sys.path` so that Python can find the package.


Run the Python script
^^^^^^^^^^^^^^^^^^^^^

Open a terminal and navigate to the directory where the Python script file is located.

.. code-block:: bash

    cd path/to/directory/where/my_script.py/is/located

Please replace :code:`path/to/directory/where/my_script.py/is/located` with the actual path to the directory where the Python script file is located.

Start the Python interpreter and run the script.

.. code-block:: bash

    python3 my_script.py

This will execute the commands in the script file and show the results in the terminal.
It looks like this:

.. code-block:: none

    % python3 my_script.py
    0.2200836694739778


Next steps
------------

- Some examples of how to use the RSU Analyzer package are provided in the :doc:`examples <examples>` section.
- For more information about the functions in the package, see the :doc:`API reference <api>` section.
