import numpy.typing as npt
from . import Component
from .. import ATR
from .utils import normalize


class SpeedObservation(Component):
    """
    Observes ATR speed
    """
    internal_obs_min: npt.ArrayLike = [-1]
    internal_obs_max: npt.ArrayLike = [1]

    def internal_obs(self) -> npt.ArrayLike:
        return [normalize(self.env.atr.speed, ATR.SPEED_MIN, ATR.SPEED_MAX)]