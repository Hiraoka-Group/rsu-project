Installation
================

.. note::

    The following instructions are for installing the project on a Unix-based system (e.g., Linux, macOS). If you are using a Windows system, please refer to documentation on how to install the project on Windows.

To install the project, follow these steps:

Before You Begin
-------------------

Before you install the project, make sure you have the following software installed on your system:

- Python 3.11 or later
- Git
- Poetry

If you don't have any of the above software installed, please refer to the documentation for each software to install it on your system.


Installation Steps
---------------------

1. Clone the repository
^^^^^^^^^^^^^^^^^^^^^^^^^

Navigate to the directory where you want to store the project using the ``cd`` command, like this:

.. code-block:: bash

    cd path/to/your/directory

Please replace ``path/to/your/directory`` with the path to the directory where you want to store the project.

Then, run the following command to clone the repository:

.. code-block:: bash

    git clone https://github.com/Hiraoka-Group/rsu-project.git


The above command will create a new directory named ``rsu-project`` in the directory you specified. This directory will contain the project files.


2. Create a virtual environment, and activate it. 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a virtual environment to install the project dependencies. You can use the built-in ``venv`` module to create a virtual environment. 

In this example, we will create a virtual environment named ``myenv`` in the project root directory (i.e., the ``rsu-project`` directory).

Navigate to the project root directory using the ``cd`` command, like this:

.. code-block:: bash

    cd rsu-project

Then, run the following command to create a virtual environment:

.. code-block:: bash

    python3 -m venv myenv

In this example, the virtual environment is named ``myenv``. You can replace ``myenv`` with the name you want to use for the virtual environment.

The above command will create a new directory named ``myenv`` in the project directory. This directory will contain the virtual environment files.

Activate the virtual environment by running the following command:

.. code-block:: bash

    source myenv/bin/activate

After running the above command, you should see ``(myenv)`` at the beginning of the command prompt. This indicates that the virtual environment is activated. For example:

.. code-block:: bash

    (myenv) user@hostname rsu-project %

.. note::

    If you want to deactivate the virtual environment, run the following command:

    .. code-block:: bash

        deactivate

    After running the above command, you should see the virtual environment name at the beginning of the command prompt disappear. For example:

    .. code-block:: bash

        user@hostname rsu-project %
    
    This indicates that the virtual environment is deactivated.


3. Install the project dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make sure the virtual environment is activated, and then run the following command:

.. code-block:: bash

    poetry install

The above command will install the project dependencies in the virtual environment.



Next Steps
--------------

- If you want to reproduce the results of the paper, please refer to the :doc:`Reproducing the Results <reprod>` section.

- If you want to use the RSU Analyzer package for your own research, please refer to the :doc:`Using the RSU Analyzer <rsuanalyzer>` section.
