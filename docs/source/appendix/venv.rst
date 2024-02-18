About Virtual Environment
=========================


Virtual Environment is a tool to create isolated Python environments. 
It creates a folder which contains all the necessary executables to use the packages that a Python project would need.
For more information, please refer to the documentation: https://docs.python.org/3/library/venv.html

In this project, we will create the virtual environment named ``myenv`` in the root of the project ``rsu-project``.

.. code-block:: none
   :emphasize-lines: 2

   rsu-project
   ├── .venv
   ├── LICENSE
   ├── README.md
   ├── docs
   ├── images
   ├── poetry.lock
   ├── pyproject.toml
   ├── reprod
   │   ├── rsuanalyzer
   │   ├── script1.py
   │   ├── script2.py
   │   ├── script3.py
   │   ├── script4.py
   │   └── script5.py
   ├── results
   └── tests


.. note::

   The following instructions are for macOS. If you are using other OS such as Windows or Linux, please refer to the official documentation: https://docs.python.org/3/library/venv.html


Create Virtual Environment
--------------------------

You probably already have a virtual environment created through the :doc:`installation of the project dependencies <../installation>`. If you already have a virtual environment, you don't need to create it again. You can skip this section and go to the next section.

Make sure your current working directory is the root of the project ``rsu-project``, then run the following command:

.. code-block:: bash

   python -m venv .venv

This will create a folder named ``.venv`` in the root of the project.

Once the virtual environment is created, you don't need to create it again. You can activate and deactivate it whenever you want.


Activate Virtual Environment
------------------------------

To activate the virtual environment, run the following command from the root of the project ``rsu-project``:

.. code-block:: bash

   source .venv/bin/activate

Or, if your current working directory is ``rsu-project/reprod``, you can run the following command:

.. code-block:: bash

   source ../.venv/bin/activate


When the virtual environment is activated, the shell prompt will change. It will include the name of the active virtual environment to help you keep track of it. For example:

.. code-block:: bash

   (.venv) user@hostname path/to/rsu-project %

Now you can install packages without affecting other projects or your global Python installation. Every time you install a package or execute a Python script, make sure the virtual environment is activated.


Deactivate Virtual Environment
--------------------------------

After you are done working with the virtual environment, you can deactivate it by running the following command:

.. code-block:: bash

   deactivate

The shell prompt will change back to the original state. You can see that the name of the active virtual environment is no longer displayed.

.. code-block:: bash

   user@hostname path/to/rsu-project %
