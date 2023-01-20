"""
Downloader
"""

import os
import json
import cv2


def download(video_path, ytb_id, proxy=None):
    """
    ytb_id: youtube_id
    save_folder: save video folder
    proxy: proxy url, default None
    """
    if proxy is not None:
        proxy_cmd = "--proxy {}".format(proxy)
    else:
        proxy_cmd = ""
    if not os.path.exists(video_path):
        down_video = " ".join([
            "yt-dlp",
            proxy_cmd,
            '-f', "'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio'",
            '--skip-unavailable-fragments',
            '--merge-output-format', 'mp4',
            "https://www.youtube.com/watch?v=" + ytb_id, "--output",
            video_path, "--external-downloader", "aria2c",
            "--external-downloader-args", '"-x 16 -k 1M"'
        ])
        print(down_video)
        status = os.system(down_video)
        if status != 0:
            print(f"video not found: {ytb_id}")


def expand(bbox, ratio, vid_w, vid_h):
    top, bottom, left, right = bbox
    exp_h = vid_h * ratio
    exp_w = vid_w * ratio
    top = max(top - exp_h, 0)
    bottom = min(bottom + exp_h, vid_h)
    left = max(left - exp_w, 0)
    right = min(right + exp_w, vid_w)
    return top, bottom, left, right


def to_square(bbox):
    top, bottom, left, right = bbox
    h = bottom - top
    w = right - left
    c = min(h, w) // 2
    c_h = (top + bottom) / 2
    c_w = (left + right) / 2

    top, bottom = c_h - c, c_h + c
    left, right = c_w - c, c_w + c
    return top, bottom, left, right


def process_ffmpeg(raw_vid_path, save_folder, save_vid_name, bbox, time):
    """
    raw_vid_path:
    save_folder:
    save_vid_name:
    bbox: format: top, bottom, left, right. the values are normalized to 0~1
    time: begin_sec, end_sec
    """

    def secs_to_timestr(secs):
        hrs = secs // (60 * 60)
        min = (secs - hrs * 3600) // 60
        sec = secs % 60
        end = (secs - int(secs)) * 100
        return "{:02d}:{:02d}:{:02d}.{:02d}".format(int(hrs), int(min), int(sec), int(end))

    out_path = os.path.join(save_folder, save_vid_name)
    cap = cv2.VideoCapture(raw_vid_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    top, bottom, left, right = to_square(expand(bbox, 0.02, width, height))
    start_sec, end_sec = time

    cmd = f"ffmpeg -i {raw_vid_path} -vf crop={right - left}:{bottom - top}:{left}:{top} -ss {secs_to_timestr(start_sec)} -to {secs_to_timestr(end_sec)} -loglevel error {out_path}"
    os.system(cmd)
    return out_path


def load_data(file_path):
    with open(file_path) as f:
        data_dict = json.load(f)

    for key, val in data_dict['clips'].items():
        save_name = key + ".mp4"
        ytb_id = val['ytb_id']
        time = val['duration']['start_sec'], val['duration']['end_sec']
        bbox = [val['bbox']['top'], val['bbox']['bottom'], val['bbox']['left'], val['bbox']['right']]
        yield ytb_id, save_name, time, bbox


if __name__ == '__main__':
    json_path = 'test.json'  # json file path
    raw_vid_root = './downloaded_celebvtext/raw/'  # download raw video path
    processed_vid_root = './downloaded_celebvtext/processed/'  # processed video path
    proxy = None  # proxy url example, set to None if not use

    os.makedirs(raw_vid_root, exist_ok=True)
    os.makedirs(processed_vid_root, exist_ok=True)

    for vid_id, save_vid_name, time, bbox in load_data(json_path):
        raw_vid_path = os.path.join(raw_vid_root, vid_id + ".mp4")
        # Downloading is io bounded and processing is cpu bounded.
        # It is better to download all videos firstly and then process them via multiple cpu cores.
        download(raw_vid_path, vid_id, proxy)
        # process_ffmpeg(raw_vid_path, processed_vid_root, save_vid_name, bbox, time)

    # with open('./ytb_id_errored.log', 'r') as f:
    #     lines = f.readlines()
    # for line in lines:
    #     raw_vid_path = os.path.join(raw_vid_root, line + ".mp4")
    #     download(raw_vid_path, line)
