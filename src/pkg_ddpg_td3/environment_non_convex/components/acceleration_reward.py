from . import Component


class AccelerationReward(Component):
    """
    Gives negative reward proportional to (acceleration)^2
    """
    def __init__(self, factor: float):
        self.factor = factor
    
    def step(self) -> float:
        return -self.factor*self.env.atr.acceleration**2