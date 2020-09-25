#CreateVideoGrids::
#Runs though a given directory and all subdirectories to find all video files with given ext.
#Creates a n*m gid of frames (equispaced) for each video file
#Names the grid using subdir names and file name


#Directory to look into for files (here and any subdirectories) ::
pointed_directory = 'C:\\Camera_Temp_Folder\\Dump2_22409\\20200923'
##This should not have any '\\' at the end to save the file name corectly

#Directory to save the grid images ::
grid_directory = 'C:\\Camera_Temp_Folder\\grids3\\20200923\\'
## This should have a '\\' at the end or the last folder name will be prefixed to file name

#filetype extension to look for e.g.: "*.mp4" ::
pattern = "*.mp4"
#Size of the grid to make ::
grid_columns = 2
grid_rows = 2


def creategrid(filename,columns,rows):
    #import libraries
    import cv2
    import numpy as np
    from PIL import Image

    #open video file
    vid = cv2.VideoCapture(filename)

    #Generate data about video file:
    no_frames=int(vid.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    frame_width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    #Generate list of frames to capture:
    N = no_frames//(columns*rows)
    frame_list = []
    for i in range(1,columns*rows+1):
        frame_list.append(N*i)

    #Generatre white array for holding the frames
    border_around_frames = 0.05 #5% white border around each frame
    top_border = int(np.floor(frame_height*border_around_frames))
    side_border = int(np.floor(frame_width*border_around_frames))
    matrix_width = int(np.floor(frame_width*columns + side_border*(columns+1)))
    matrix_height = int(np.floor(frame_height*rows + top_border*(rows+1)))
    frames_matrix = np.full((matrix_height,matrix_width,3),255, dtype=np.uint8)

    #Generate figure with frames
    for ind,frame in enumerate(frame_list):
        vid.set(1,frame)
        ret,frame_image = vid.read()
        frame_image = cv2.cvtColor(frame_image, cv2.COLOR_BGR2RGB)
        
        rowN = ind//columns
        colN = (ind%columns)
        frames_matrix[((rowN+1)*top_border+(rowN)*frame_height):((rowN+1)*top_border+(rowN+1)*frame_height),((colN+1)*side_border+(colN)*frame_width):((colN+1)*side_border+(colN+1)*frame_width),:]=frame_image
        
    vid.release()
    img = Image.fromarray(frames_matrix)
    
    return img


#Function to go through directory/subdir. and run creategrd for every .mp4 file
def main():
    import os
    from glob import glob

    files_list = []
    for dir,_,_ in os.walk(pointed_directory):
        files_list.extend(glob(os.path.join(dir,pattern)))

    #grid_image = creategrid('14.mp4',2,2)
    number_of_files = len(files_list)
    print('Total files found:'+str(number_of_files))
    for i,directory in enumerate(files_list):
        #for i in range(3):
        try:
            grid_image = creategrid(directory,grid_columns,grid_rows)
            grid_image.save(grid_directory+directory.replace(pointed_directory+'\\','').replace('\\','_').replace('.mp4','')+'.jpg',"JPEG")
        except:
            print('Could not process file: '+directory)
        #print the number of the file currently finished
        print(str(i)+',',end='')
        #Print the file number out of how many files in total every 100 files
        if i%100 == 0:
            print('\n'+str(i) + '/' + str(number_of_files))
    pass


if __name__=='__main__':
    main()
