# import utility
import datetime
import cv2
import os
import numpy as np

def main():

    # for each video vname in the input folder
    for vname in os.listdir("./input_videos"):
        if vname != ".DS_Store":
            # create output folder
            output_folder = "./output_images/" + vname[:vname.index('.')] + "_output"
            os.makedirs(output_folder)
            capture_interval = datetime.timedelta(minutes=1)

            # get file extension
            extension = vname[vname.index('.'):]
            snap_from_video("./input_videos/" + vname, capture_interval, output_folder, extension)


def snap_from_video(video_path, capture_interval, image_folder, extension, time_format="%Y%m%d_%H%M%S"):
    video_filename = os.path.basename(video_path)
    video_filename_format = "%Y%m%d-%H%M%S" + extension
    print video_filename 

    # snap images from the video file
    cap = cv2.VideoCapture(video_path)
    initial_time = datetime.datetime.strptime(video_filename, video_filename_format)

    video_pos_time = 0  # in ms
    curr_time = initial_time

    while cap.isOpened():
        cap.set(0, video_pos_time)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(image_folder + "/" + curr_time.strftime(time_format) + ".jpg", frame)
            video_pos_time += capture_interval.total_seconds() * 1000  # in ms
            curr_time += capture_interval
        else:
            break
    end_time = curr_time - capture_interval

    return initial_time, end_time


if __name__ == '__main__':
    main()
