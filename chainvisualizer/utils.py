def transpose_to_xyz(points: list[list[float]]) -> list[list[float]]:
    """
    Example:
    >>> transpose_to_xyz([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    """
    return [list(coord) for coord in zip(*points)]


def limit_axis(ax, min_width):
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    z_min, z_max = ax.get_zlim()
    current_width = max(x_max - x_min, y_max - y_min, z_max - z_min)
    if current_width < min_width:
        x_center = (x_min + x_max) / 2
        y_center = (y_min + y_max) / 2
        z_center = (z_min + z_max) / 2
        ax.set_xlim(x_center - min_width / 2, x_center + min_width / 2)
        ax.set_ylim(y_center - min_width / 2, y_center + min_width / 2)
        ax.set_zlim(z_center - min_width / 2, z_center + min_width / 2)