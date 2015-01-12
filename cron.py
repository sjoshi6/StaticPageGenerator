__author__ = 'saurabh'
import os, time, shutil, sys
import FileReader
work_path = './input_folder/'
count=0
while(True):

    if len(os.listdir(work_path))>1:
        count=count+1
        print("File Found: Parsing...")
        FileReader.input_reader('./input_folder/input.txt',count)

    print("No input")
    time.sleep(3)