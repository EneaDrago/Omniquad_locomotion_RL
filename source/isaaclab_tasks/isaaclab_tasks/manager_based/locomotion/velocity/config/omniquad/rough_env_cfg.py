from isaaclab.utils import configclass
import isaaclab_tasks.manager_based.locomotion.velocity.mdp as mdp
from isaaclab_tasks.manager_based.locomotion.velocity.velocity_env_omni_cfg_v0 import LocomotionVelocityRoughEnvCfg
from isaaclab_tasks.manager_based.locomotion.velocity.vel_omni_cfg_play import PlayLocomotionVelocityRoughEnvCfg


##
# Pre-defined configs
##
from isaaclab_assets.robots.omniquad import OMNIQUAD_CFG  # isort: skip


@configclass
class OmniQuadRoughEnvCfg(LocomotionVelocityRoughEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()
        # switch robot to omniquad
        self.scene.robot = OMNIQUAD_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")


@configclass
class PlayOmniQuadRoughEnvCfg(PlayLocomotionVelocityRoughEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()
        # switch robot to omniquad
        self.scene.robot = OMNIQUAD_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")        
