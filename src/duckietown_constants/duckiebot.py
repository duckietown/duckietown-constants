import numpy as np

from .geometry import Pose
from .sensors import CameraInfo
from .sensors import LedsInfo
from .sensors import EncoderInfo
from .components import Wheel


@dataclass
class NominalDuckiebot(object):

  camera_pose: Pose
  encoder: Optional[EncoderInfo]
  left_wheel_pose: Pose
  right_wheel_pose: Pose
  wheels_baseline: float
  wheels_radius: float
  leds: LedsInfo



nominal_duckiebot = {
  "DB18": NominalDuckiebot(
    camera_pose=np.array([0, 0, 0, 0, 0, 0])
  ),
  "DB19": NominalDuckiebot(
    camera_pose=np.array([0, 0, 0, 0, 0, 0])
  )
}


duckiebot_models = list(nominal_duckiebot.keys())


__all__ = [
  "nominal_duckiebot",
  "duckiebot_models"
]
