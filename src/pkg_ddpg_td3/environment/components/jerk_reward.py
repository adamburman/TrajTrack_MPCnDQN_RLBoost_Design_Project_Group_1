from . import Component


class JerkReward(Component):
    """
    Rewards making progress along the reference path, penalizes the opposite
    """
    def __init__(self, factor: float):
        self.factor = factor

    def reset(self) -> None:
        self.last_acceleration = 0
    
    def step(self) -> float:
        reward = -self.factor*(self.env.agent.acceleration - self.last_acceleration)**2
        self.last_path_progress = self.env.agent.acceleration
        return reward