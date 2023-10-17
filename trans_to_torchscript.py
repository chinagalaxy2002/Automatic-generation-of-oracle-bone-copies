import time
from options.train_options import TrainOptions
from data import create_dataset
from models import create_model
from util.visualizer import Visualizer
import torch.jit

if __name__ == '__main__':
    opt = TrainOptions().parse()  # get training options
    model = create_model(opt)  # create a model given opt.model and other options
    model.setup(opt)
    # 加载预训练权重
    model.load_networks(30)

    for name in model.model_names:
        if isinstance(name, str):
            net_name = 'net' + name
            net = getattr(model, net_name)
            if isinstance(net, torch.nn.DataParallel):
                net = net.module
            print(net)
            net_script = torch.jit.script(net)
            net_script.save(f"{net_name}.torscript")
    # # 将模型转换为torchscript
    # model_script = torch.jit.trace(model, torch.rand(1, 3, 256, 256))  # 这里的输入大小应与模型期望的输入大小匹配
    # # 保存torchscript模型到文件
    # model_script.save('moben.torchscript')