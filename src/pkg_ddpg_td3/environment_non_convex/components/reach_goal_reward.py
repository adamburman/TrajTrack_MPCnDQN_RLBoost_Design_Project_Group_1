from . import Component


class ReachGoalReward(Component):
    """
    Gives a constant negative reward when the ATR reaches the goal
    """
    def __init__(self, factor: float):
        self.factor = factor
    
    def step(self) -> float:
        reward = self.factor if self.env.reached_goal else 0
        return reward