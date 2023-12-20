from . import Component


class SpeedReward(Component):
    """
    Gives reward proportional to -(speed - reference speed)²
    """
    def __init__(self, factor: float, reference_speed: float):
        self.factor = factor
        self.reference_speed = reference_speed
    
    def step(self) -> float:
        return -self.env.time_step * self.factor * (self.env.atr.speed - self.reference_speed)**2