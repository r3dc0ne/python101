from wanderer import TheWorld

world_instance = TheWorld()
world_instance.set_targets([(1, 1), (3, 4), (-1, 0)])
world_instance.walk()

world_instance.set_targets([(3, 2), (-2, 2)])
world_instance.walk()

