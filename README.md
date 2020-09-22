# CreateVideoGrid
Creates a singe image grid of n*m frames, read form a video file, from all video files in a given dirctory (directory and subdirectories)
Grid images are named after subdirectory and file name


Input variables:

#Directory to look into for files (here and any subdirectories) ::
pointed_directory = 'G:\\Folder1\\Folder2\\'

#Directory to save the grid images ::
grid_directory = 'C:\\Folder1\\grids\\'

#filetype extension to look for e.g.: "*.mp4" ::
pattern = "*.mp4"

#Size of the grid to make ::
grid_columns = 2
grid_rows = 2


For example if you give a directory 'G:\\Folder1\\Folder2\\', and inside you have 3 folders: F20, F21, F22, with 2 video files each (1.mp4 and 2.mp4), the program will return 6 grid images named:

'F20_1.jpg';'F20_2.jpg';'F21_1.jpg';'F21_2.jpg';'F22_1.jpg';'F22_2.jpg'

this is to prvent nameclash if you have the same video file name in multiple directories


Thigs that can be improved:
-allow the program to be run from comand line with given arguments
-time how long it takes to generate each grid file (for 2x2 3x3 4x4 etc.)
-check if video file length affects runtime
-allow text to be written on the grid image (frame number, file name etc)

