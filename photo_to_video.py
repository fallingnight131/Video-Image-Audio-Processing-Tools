import cv2
import os

def images_to_video(image_folder, output_file, fps=30):
    # 获取所有 PNG 文件并排序
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort()

    if not images:
        print("没有找到 PNG 文件！")
        return

    # 获取第一张图片的尺寸
    first_image = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, _ = first_image.shape

    # 定义视频编码器和输出
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # MP4 编码器
    video = cv2.VideoWriter(output_file + ".mp4", fourcc, fps, (width, height))

    # 将每张图片写入视频
    for image_name in images:
        image_path = os.path.join(image_folder, image_name)
        frame = cv2.imread(image_path)
        video.write(frame)

    video.release()
    print(f"视频已保存到 {output_file}.mp4")

    # 询问用户是否删除所有图片
    delete_images = input("是否删除所有图片？(y/n): ").strip().lower()
    if delete_images == 'y':
        for image_name in images:
            os.remove(os.path.join(image_folder, image_name))
        print("所有图片已删除。")
    else:
        print("图片保留。")

# 使用示例
image_folder = "D:\\DownLoads\\videos\\convert\\zgr--dlw"  # 替换为你的 PNG 文件夹路径
output_file = "D:\\DownLoads\\videos\\convert\\zgr--dlw\\1"          # 替换为输出 MP4 文件名
images_to_video(image_folder, output_file)
