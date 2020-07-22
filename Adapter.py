class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):

        light_rezult = []
        obstacles_rezult = []

        dim = (len(grid[0]), len(grid))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    lights = (j, i)
                    light_rezult.append(lights)
                elif grid[i][j] == -1:
                    obstacles = (j, i)
                    obstacles_rezult.append(obstacles)
                else:
                    continue

        self.adaptee.set_dim(dim)
        self.adaptee.set_lights(light_rezult)
        self.adaptee.set_obstacles(obstacles_rezult)
        return self.adaptee.generate_lights()
