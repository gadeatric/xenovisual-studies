import requests
import random
import json
import time
import webbrowser
import os
from pychan import FourChan as chan4, PychanLogger, LogLevel

#### instance made by code copy-pasted from github as recomended by the github repository of the library 
# (https://github.com/cooperwalbrun/pychan?tab=readme-ov-file#usage) ####

fourchan = chan4(raise_http_exceptions=False)

# Tell pychan to gracefully ignore parsing exceptions, if any, within its internal logic
fourchan = chan4(raise_parsing_exceptions=False)

# Configure logging explicitly:
logger = PychanLogger(LogLevel.INFO)

# Use all of the above settings at once
four_chan_instance = chan4(
    logger=logger,
    raise_http_exceptions=True,
    raise_parsing_exceptions=True
)

# get the boads
boards = four_chan_instance.get_boards()
print(boards)

# store in a dict the boards we are interested in
dict_boards = {"pw": "professional_wrestling", 
               "m": "mecha", "vg": "videogames",
               "vrpg": "videogames_rpg",
               "out": "outdoors",
               "jp": "otaku_culture",
               "po": "paperwork_and_origami"}

# create the folders:
for k in dict_boards.keys(): 
    board_directory = f"download_image/{k}"
    if not os.path.exists(board_directory):
        os.makedirs(board_directory)
    
    # counter for the limit:
    limit = 0
    
    # iterate through the threads 
    for thread in fourchan.get_threads(k): # name the folders after the threads
        for post in fourchan.get_posts(thread): # iterate through the posts in the thread
            # select only the posts that are files
            if hasattr(post, 'file') and post.file and limit < 30: #set the limit to 30 downloads per board
                image_url = post.file.url # get the url
                response = requests.get(image_url) # request the url
                image_filename = image_url.split('/')[-1] # get the image name
                if response.status_code == 200 and image_filename[-3:] in ("jpg", "png"): # get only jpg and png format images
                    save_path = os.path.join(board_directory, image_filename)
                    with open(save_path, 'wb') as file:
                        file.write(response.content) # save the images
                    print(f"image {save_path} saved! ☆⌒ヽ(*'､^*)chu♡")
                    limit+=1
                else:
                    if response.status_code == 200:
                        print("the image was not in the desired format!")
                    else:
                        print(f" there was an error (｡•́︿•̀｡)...:{response.status_code}") 

                if limit == 30:
                    break
        if limit == 30:
            break
        


