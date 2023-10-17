from PIL import Image
import os

# 指定输入和输出文件夹
input_folder = "datasets/moben/trainBBB"  # 将 "input_folder" 替换为包含要裁剪的图片的文件夹的路径
output_folder = "datasets/moben/trainBB"  # 将 "output_folder" 替换为保存裁剪后图片的文件夹的路径

# 定义裁剪的边距（单位为像素）
left_margin = 100  # 左边距（根据需要进行调整）
right_margin = 100  # 右边距（根据需要进行调整）
top_margin = 100  # 上边距（根据需要进行调整）
bottom_margin = 100  # 下边距（根据需要进行调整）

# 创建输出文件夹（如果不存在）
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有图片文件
for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".jpeg", ".png", ".bmp")):
        # 打开图片
        image = Image.open(os.path.join(input_folder, filename))

        # 获取图片的宽度和高度
        width, height = image.size

        # 计算裁剪的边界框
        left = left_margin
        top = top_margin
        right = width - right_margin
        bottom = height - bottom_margin

        # 裁剪图片
        cropped_image = image.crop((left, top, right, bottom))

        # 保存裁剪后的图片到输出文件夹
        cropped_image.save(os.path.join(output_folder, filename))

print("图片裁剪完成")
