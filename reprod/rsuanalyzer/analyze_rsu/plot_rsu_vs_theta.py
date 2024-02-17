from typing import Iterable

import pandas as pd
from matplotlib import pyplot as plt


def plot_rsu_vs_theta(
        *dfs: pd.DataFrame,
        labels: Iterable[str] = None,
        title: str = r"RSU vs tilt angle $\theta$",
        xlabel: str = r"Tilt angle $\theta$ /deg.", ylabel: str = "RSU"
        ) -> None:
    """Plot the RSU vs theta.

    Args:
        dfs (pd.DataFrame): 
            The pandas DataFrames containing the RSU for each theta.

            Important:
                Columns of the DataFrames should have the names "theta"
                and "RSU". Other columns will be ignored.

            Note:
                DataFrames do not nessarily have the same thetas.

        labels (Iterable[str]): 
            The names of the DataFrames. Default is None.

            Important:
                labels is keyword-only argument.

            Note:
                If labels is None, the names of the DataFrames will be 
                "df1", "df2", ... in the order of the input.

        title (str): 
            The title of the plot. Default is 
            r"RSU vs tilt angle $\theta$".
        xlabel (str): 
            The label of the x-axis. Default is 
            r"Tilt angle $\theta$ /deg.".
        ylabel (str): 
            The label of the y-axis. Default is "RSU".


    Returns:
        None

    Example:
        Case 1: Plot a single DataFrame
            >>> import rsuanalyzer as ra
            >>> ra.create_rsu_vs_theta_df("RLFFRLFFRLFF")
            >>> ra.plot_rsu_vs_theta(df1)

        Case 2: Plot multiple DataFrames
            >>> import rsuanalyzer as ra
            >>> df1 = ra.create_rsu_vs_theta_df("RRFFLLBBRRFFLLBB", delta_=87)
            >>> df2 = ra.create_rsu_vs_theta_df("RRFFLLBBRRFFLLBB", delta_=90)
            >>> ra.plot_rsu_vs_theta(df1, df2, labels=["delta=87", "delta=90"])
    """
    fig, ax = plt.subplots()

    if labels is None:
        labels = [f"df{i + 1}" for i in range(len(dfs))]
    if len(dfs) != len(labels):
        raise ValueError(
            "The number of DataFrames and the number of names should be the same.")

    for df, df_name in zip(dfs, labels):
        ax.plot(df["theta"], df["RSU"], label=df_name)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    plt.show()
