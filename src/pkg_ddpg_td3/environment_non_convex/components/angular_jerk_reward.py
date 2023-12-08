from . import Component


class AngularJerkReward(Component):
    """
    Rewards making progress along the reference path, penalizes the opposite
    """
    def __init__(self, factor: float):
        self.factor = factor

    def reset(self) -> None:
        self.last_angular_acceleration = 0
    
    def step(self,action) -> float:
        reward = -self.factor*(self.env.agent.angular_acceleration - self.last_angular_acceleration)**2
        self.last_path_progress = self.env.agent.angular_acceleration
        return reward