from typing import Iterable

import pandas as pd

from ..core.calc_rsu import calc_rsu


def create_rsu_vs_theta_df(
        ring_id: str,
        thetas: Iterable[float] = range(0, 91, 1),
        delta_: float = 87) -> pd.DataFrame:
    """Calculate the RSU of the given ring for each theta.

    Args:
        ring_id (str): 
            The conformation ID of the ring, e.g. "RLFFRLFFRLFF".
        thetas (Iterable[float], optional): 
            The list of tilt angles of C-C bonds. (unit: degree) 
            0 <= theta <= 90. Default is range(0, 91, 1).
        delta_ (float, optional): 
            N-Pd-N angle. (unit: degree) 0 < delta\_ <= 180. 
            Default is 87.
    
    Example:
        >>> import rsuanalyzer as ra
        >>> ra.create_rsu_vs_theta_df("RLFFRLFFRLFF", range(0, 91, 10))
        >>> # The result will be:
        >>> # theta       RSU
        >>> # 0      0  0.243351
        >>> # 1     10  0.079101
        >>> # 2     20  0.062665
        >>> # 3     30  0.180018
        >>> # 4     40  0.273040
        >>> # 5     50  0.343376
        >>> # 6     60  0.393650
        >>> # 7     70  0.426807
        >>> # 8     80  0.445484
        >>> # 9     90  0.451495

    See Also:
        You can plot the result using the function
        :func:`plot_rsu_vs_theta \
        <rsuanalyzer.analyze_rsu.plot_rsu_vs_theta.plot_rsu_vs_theta>`
    """
    rsu_list = [
        calc_rsu(ring_id, theta, delta_) for theta in thetas]
    
    rsu_table = pd.DataFrame({
        "theta": thetas,
        "RSU": rsu_list
    })

    return rsu_table
