import csv
import os
import threading
from moviepy.editor import VideoFileClip
import multiprocessing

def open_csv():
    with open("C:\\Users\\admin\PycharmProjects\Driving_video_cut\\video_info.csv", 'r') as csv_file:
        dict_reader = csv.DictReader(csv_file)
        path = "C:\\Users\\admin\\workspace\\3batchLaneChangeEvents\\3batchVideoFront(69\\"
        process_pool = multiprocessing.pool.Pool(10)
        for item in dict_reader:
            print(item["fileName"])
            str = path+item['fileName']
           
            str = str.replace(".csv", "_Front.mp4")
            
            if os.path.exists(str):
                print(str)
                process_pool.apply_async(cut, args=(str, int(item['videoStart']), int(item['changeVideoFrom']), int(item['changeVideoTo']), (item['eventId']),))
                # cut(item['fileName'], 2241, int(item['changeVideoFrom']), int(item['changeVideoTo']), str(item['eventId']))
        process_pool.close()
        process_pool.join()



def cut(filename, video_start,enevt_start, event_end, event_id):
    #specify a path to save the video
    print(video_start)
    
    path_save = "C:\\Users\\admin\PycharmProjects\Driving_video_cut\\eventVideo\\"
 
    start = (enevt_start - 1000 - video_start)/1000
    print(start)
    end = (event_end + 1000 - video_start)/1000
    print(end)
    clip = VideoFileClip(filename).subclip(start, end)
    clip.write_videofile(path_save + "event_%s.mp4"%event_id)




if __name__ == "__main__":
    open_csv()


