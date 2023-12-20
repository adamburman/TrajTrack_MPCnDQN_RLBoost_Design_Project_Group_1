from . import Component


class AngularJerkReward(Component):
    """
    Gives negative reward proportional to (angular jerk)^2
    """
    def __init__(self, factor: float):
        self.factor = factor

    def reset(self) -> None:
        self.last_angular_acceleration = 0
    
    def step(self) -> float:
        reward = -self.factor*(self.env.atr.angular_acceleration - self.last_angular_acceleration)**2
        self.last_angular_acceleration = self.env.atr.angular_acceleration
        return reward