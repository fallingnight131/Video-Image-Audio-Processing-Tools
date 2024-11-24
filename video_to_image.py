import cv2
import os

def extract_frames(video_path, output_dir):
    """
    将 MP4 文件分解为一帧帧 JPG 图像。

    参数:
    - video_path: 视频文件的路径。
    - output_dir: 保存帧的目录路径。
    """
    # 检查输出目录是否存在，如果不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 打开视频文件
    video_capture = cv2.VideoCapture(video_path)

    if not video_capture.isOpened():
        print("无法打开视频文件:", video_path)
        return

    frame_count = 0
    while True:
        # 读取帧
        success, frame = video_capture.read()
        if not success:
            break  # 如果无法读取，则结束

        # 保存帧为 JPG 图像
        frame_filename = os.path.join(output_dir, f"frame3_{frame_count:05d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    video_capture.release()
    print(f"视频分解完成，共提取 {frame_count} 帧。保存于: {output_dir}")

# 示例用法
if __name__ == "__main__":
    video_path = "datas/input/2.mp4"  # 输入视频文件路径
    output_dir = "datas/output"      # 输出帧保存目录
    extract_frames(video_path, output_dir)
