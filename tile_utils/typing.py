import sys
from typing import *
from torch import Tensor

from gradio.components import Component

from k_diffusion.external import CompVisDenoiser
from ldm.models.diffusion.ddpm import LatentDiffusion

from modules.processing import StableDiffusionProcessing
from modules.prompt_parser import MulticondLearnedConditioning, ScheduledPromptConditioning
from modules.extra_networks import ExtraNetworkParams
from modules.sd_samplers_kdiffusion import KDiffusionSampler, CFGDenoiser
from modules.sd_samplers_compvis import VanillaStableDiffusionSampler

ModuleType = type(sys)

BBoxControls = Union[List[Component], List[Any]]    # widgets or values

Sampler = Union[KDiffusionSampler, VanillaStableDiffusionSampler]
Cond = MulticondLearnedConditioning
Uncond = List[List[ScheduledPromptConditioning]]
ExtraNetworkData = DefaultDict[str, List[ExtraNetworkParams]]

# 'c_crossattn': Tensor    # prompt cond
# 'c_concat':    Tensor    # latent mask
CondDict = Dict[str, Tensor]