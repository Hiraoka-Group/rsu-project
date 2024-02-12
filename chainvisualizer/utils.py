def transpose_to_xyz(points: list[list[float]]) -> list[list[float]]:
    """Transpose a list of points from the form of 
    [[x1, y1, z1], [x2, y2, z2], ...]
    to the form of [[x1, x2, ...], [y1, y2, ...], [z1, z2, ...]].

    It is useful when you want to plot the points with matplotlib.

    Args:
        points (list[list[float]]): A list of points.

    Returns:
        list[list[float]]: 
            A list of points in the form of 
            [[x1, x2, ...], [y1, y2, ...], [z1, z2, ...]].

    Example:
    >>> transpose_to_xyz([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    """
    return [list(coord) for coord in zip(*points)]


def limit_axis(ax, min_width):
    """Set the display limits of the axis to a cube with a minimum width.
    
    If the maximum width of the axis is smaller than the minimum width,
    the axis will be set to a cube with the minimum width. Otherwise,
    the axis will be set to a cube with the maximum width.

    Args:
        ax (mpl_toolkits.mplot3d.Axes3D): A 3D axis object.
        min_width (float): The minimum width of the axis.
    """
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    z_min, z_max = ax.get_zlim()
    current_width = max(x_max - x_min, y_max - y_min, z_max - z_min)
    min_width = max(min_width, current_width)
    x_center = (x_min + x_max) / 2
    y_center = (y_min + y_max) / 2
    z_center = (z_min + z_max) / 2
    ax.set_xlim(x_center - min_width / 2, x_center + min_width / 2)
    ax.set_ylim(y_center - min_width / 2, y_center + min_width / 2)
    ax.set_zlim(z_center - min_width / 2, z_center + min_width / 2)