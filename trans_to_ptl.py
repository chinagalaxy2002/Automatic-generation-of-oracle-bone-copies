import torch
from torch.utils.mobile_optimizer import optimize_for mobile

model = torch.load("netG_A.torscript")
model.eval()

scripted_model = torch.jit.script(model)
optimized_scripted_model = optimize_for_mobile(scripted_model)
optimized_scripted_model._save_for_lite_interpreter(netG_A.torscript.ptl)