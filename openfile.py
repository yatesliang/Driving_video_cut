import csv
import os
import time
import threading
from moviepy.editor import VideoFileClip
import multiprocessing

def open_csv():
    with open("C:\\Users\\admin\PycharmProjects\Driving_video_cut\\video_info.csv", 'r') as csv_file:
        dict_reader = csv.DictReader(csv_file)
        path = "C:\\Users\\admin\\workspace\\3batchLaneChangeEvents\\3batchVideoFront(69\\"
        # process_pool = multiprocessing.pool.Pool(10)
        for item in dict_reader:

            str = path+item['fileName']
           
            str = str.replace(".csv", "_Front.mp4")
            
            if os.path.exists(str):
                print(item['eventId'])
                # process_pool.apply_async(cut, args=(str, int(item['videoStart']), int(item['changeVideoPoint']), (item['eventId']),))
                cut(str, int(item['videoStart']), int(item['changeVideoPoint']), (item['eventId']))

        # process_pool.close()
        # process_pool.join()



def cut(filename, video_start,event_point, event_id):
    #specify a path to save the video

    
    path_save = "C:\\Users\\admin\PycharmProjects\Driving_video_cut\\eventVideo\\"
 
    start = (event_point - 10000 - video_start)/1000
    if start < 0:
        start = 0
    end = (event_point + 10000 - video_start)/1000
    clip = VideoFileClip(filename).subclip(start, end)
    clip.write_videofile(path_save + "event_%s.mp4" % event_id)
    clip.reader.close()





if __name__ == "__main__":
    open_csv()


