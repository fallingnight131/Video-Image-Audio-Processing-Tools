import cv2
import os
from moviepy.editor import VideoFileClip

def extract_frames_and_audio(input_dir, output_frames_dir, output_audio_dir):
    """
    将目录下所有 MP4 文件的帧和音频分别保存到不同的目录。

    参数:
    - input_dir: 输入视频文件所在的目录。
    - output_frames_dir: 保存帧的目录。
    - output_audio_dir: 保存音频的目录。
    """
    # 创建输出目录（如果不存在）
    if not os.path.exists(output_frames_dir):
        os.makedirs(output_frames_dir)
    if not os.path.exists(output_audio_dir):
        os.makedirs(output_audio_dir)

    # 遍历输入目录下的所有文件
    for video_filename in os.listdir(input_dir):
        if video_filename.endswith(".mp4"):  # 检查是否为 MP4 文件
            video_path = os.path.join(input_dir, video_filename)
            
            # 构造每个视频的帧保存目录
            frames_output_dir = os.path.join(output_frames_dir, os.path.splitext(video_filename)[0])
            if not os.path.exists(frames_output_dir):
                os.makedirs(frames_output_dir)

            # 提取视频帧
            video_capture = cv2.VideoCapture(video_path)
            if not video_capture.isOpened():
                print("无法打开视频文件:", video_path)
                continue

            frame_count = 0
            while True:
                # 读取帧
                success, frame = video_capture.read()
                if not success:
                    break  # 如果无法读取，则结束

                # 保存帧为 JPG 图像
                frame_filename = os.path.join(frames_output_dir, f"frame_{frame_count:05d}.jpg")
                cv2.imwrite(frame_filename, frame)
                frame_count += 1

            video_capture.release()
            print(f"视频 {video_filename} 的帧分解完成，共提取 {frame_count} 帧，保存于: {frames_output_dir}")

            # 提取音频
            try:
                audio_output_path = os.path.join(output_audio_dir, f"{os.path.splitext(video_filename)[0]}.mp3")
                video_clip = VideoFileClip(video_path)
                video_clip.audio.write_audiofile(audio_output_path, codec="libmp3lame")
                print(f"视频 {video_filename} 的音频提取完成，保存于: {audio_output_path}")
            except Exception as e:
                print(f"提取音频时出错: {e}")

# 示例用法
if __name__ == "__main__":
    input_dir = "D:/DownLoads/videos/bilibili/bigpowerking"  # 输入视频文件目录路径
    output_frames_dir = "D:/datas/faces/frames"  # 输出帧保存目录
    output_audio_dir = "D:/datas/faces/audio"  # 输出音频保存目录
    extract_frames_and_audio(input_dir, output_frames_dir, output_audio_dir)
