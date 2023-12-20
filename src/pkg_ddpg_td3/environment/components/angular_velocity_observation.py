import numpy.typing as npt
from . import Component
from .. import ATR
from .utils import normalize


class AngularVelocityObservation(Component):
    """
    Observes ATR angular velocity
    """
    internal_obs_min: npt.ArrayLike = [-1]
    internal_obs_max: npt.ArrayLike = [1]

    def internal_obs(self) -> npt.ArrayLike:
        return [
            normalize(
                self.env.atr.angular_velocity,
                ATR.ANGULAR_ACCELERATION_MIN,
                ATR.ANGULAR_ACCELERATION_MAX
            )
        ]