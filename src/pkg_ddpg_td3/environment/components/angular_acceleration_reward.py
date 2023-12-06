from . import Component


class AngularAccelerationReward(Component):
    """
    Gives negative reward proportional to (acceleration)^2
    """
    def __init__(self, factor: float):
        self.factor = factor
    
    def step(self) -> float:
        return -self.factor*self.env.agent.angular_acceleration**2