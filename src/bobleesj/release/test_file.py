class Gridded_circle:
    def __init__(self, radius=1, n_points_on_diameter=N_POINTS_ON_DIAMETER, mu=None):
        self.radius = radius
        self.npoints = n_points_on_diameter
        self.mu = mu
        self.distances = []
        self.muls = []
        self._get_grid_points()

    def _get_grid_points(self):
        """
        given a radius and a grid size, return a grid of points to uniformly sample that circle
        """
        xs = np.linspace(-self.radius, self.radius, self.npoints)
        ys = np.linspace(-self.radius, self.radius, self.npoints)
        self.grid = {(x, y) for x in xs for y in ys if x**2 + y**2 <= self.radius**2}
        self.total_points_in_grid = len(self.grid)

    def set_distances_at_angle(self, angle):
        """
        given an angle, set the distances from the grid points to the entry and exit coordinates

        Parameters
        ----------
        angle float
          the angle in degrees

        Returns
        -------
        the list of distances containing total distance, primary distance and secondary distance

        """
        self.primary_distances, self.secondary_distances, self.distances = [], [], []
        for coord in self.grid:
            distance, primary, secondary = self.get_path_length(coord, angle)
            self.distances.append(distance)
            self.primary_distances.append(primary)
            self.secondary_distances.append(secondary)
