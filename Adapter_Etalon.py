class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lights_or_obstacles(self, descriptor, grid):
        result = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == descriptor:
                    result.append((j, i))
        return result

    def lighten(self, grid):
        dim = (len(grid[0]), len(grid))
        self.adaptee.set_dim(dim)
        lights = self.lights_or_obstacles(1, grid)
        obstacles = self.lights_or_obstacles(-1, grid)
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)
        return self.adaptee.generate_lights()