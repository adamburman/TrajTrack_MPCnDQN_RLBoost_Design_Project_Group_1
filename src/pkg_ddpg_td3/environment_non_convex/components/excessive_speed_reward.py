from numpy import sign
from . import Component


class ExcessiveSpeedReward(Component):
    """
    Gives a negative reward for exceeding a reference speed
    """
    def __init__(self, factor: float, reference_speed: float):
        self.factor = factor
        self.reference_speed = reference_speed
    
    def step(self) -> float:
        error = sign(self.reference_speed) * (self.env.atr.speed - self.reference_speed)
        return -self.env.time_step * self.factor * max(0, error)