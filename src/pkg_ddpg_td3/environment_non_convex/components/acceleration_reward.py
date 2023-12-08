from . import Component


class AccelerationReward(Component):
    """
    Gives negative reward proportional to |acceleration|
    """
    def __init__(self, factor: float):
        self.factor = factor
    
    def step(self,action) -> float:
        return -self.factor*self.env.agent.acceleration**2