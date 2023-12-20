from . import Component


class JerkReward(Component):
    """
    Gives negative reward proportional to (linear jerk)^2
    """
    def __init__(self, factor: float):
        self.factor = factor

    def reset(self) -> None:
        self.last_acceleration = 0
    
    def step(self) -> float:
        reward = -self.factor*(self.env.atr.acceleration - self.last_acceleration)**2
        self.last_acceleration = self.env.atr.acceleration
        return reward