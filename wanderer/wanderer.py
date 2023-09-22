class TheWorld:
    def __init__(self):
        self.walker_pos_x = 0
        self.walker_pos_y = 0
        self.targets = []
        self.steps = 0

    def set_targets(self, targets):
        self.targets = targets
        self.steps = 0
        self.walker_pos_x = targets[0][0]
        self.walker_pos_y = targets[0][1]

    def walk(self):
        for target in self.targets:
            target_pos_x = target[0]
            target_pos_y = target[1]

            while (target_pos_x, target_pos_y) != (self.walker_pos_x, self.walker_pos_y):

                if self.walker_pos_x < target_pos_x:
                    self.walker_pos_x += 1
                elif self.walker_pos_x > target_pos_x:
                    self.walker_pos_x -= 1

                if self.walker_pos_y < target_pos_y:
                    self.walker_pos_y += 1
                elif self.walker_pos_y > target_pos_y:
                    self.walker_pos_y -= 1

                self.steps += 1

            print(self.steps)
