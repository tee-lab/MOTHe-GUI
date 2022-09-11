from tkinter import *
from mothe.pipe import mothe
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
import yaml
from tkinter import ttk
import numpy as np
from matplotlib import pyplot as plt
import cv2

class mothe_gui:
    
    def __init__(self):
        pass

    def click_help():
        window1 = Tk()
        window1.title("Help")
        window1.geometry('550x300')
        txt = scrolledtext.ScrolledText(window1,width=500,height=250)
        txt.insert(INSERT,'MOTHe:\n0. Mothe tutorial: https://github.com/tee-lab/MOTHe-GUI/#mothe-gui\n1. Anaconda installation for linux: https://github.com/tee-lab/MOTHe-GUI/wiki#installations-and-prerequisites\n2. Anaconda installation for Windows/Mac: https://github.com/tee-lab/MOTHe-GUI/wiki#installing-anaconda-for-windowsmac\n3. Linux environment setup: https://github.com/tee-lab/MOTHe-GUI/wiki#setting-up-the-environment-linux\n4. Windows/Mac environment setup: https://github.com/tee-lab/MOTHe-GUI/wiki#setting-up-the-environment-windowsmac\n5. FAQs and troubleshooting: https://github.com/tee-lab/MOTHe-GUI/wiki#faqstroubleshooting')
        txt.grid(column=0,row=0)

    def click_determine_thresh():
        max_value = 255
        max_type = 1
        max_binary_value = 255
        trackbar_type = 'Type: \n 0: Binary'
        trackbar_value = 'Value'
        window_name = 'Check threshold'
        def Threshold_Demo(val):
            # threshold_type = cv2.getTrackbarPos(trackbar_type, window_name)
            threshold_value = cv2.getTrackbarPos(trackbar_value, window_name)
            _, dst = cv2.threshold(src_gray, threshold_value, max_binary_value, 0)
            cv2.imshow(window_name, dst)
        messagebox.showinfo('Status','Select a video file to check threshold values')
        video = filedialog.askopenfilename()
        cap = cv2.VideoCapture(video)
        nframes =cap.get(cv2.CAP_PROP_FRAME_COUNT)          
        i = 0
        steps = 10
        while cap.isOpened() and i<(nframes-steps):
            i=i+steps
            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            ret, frame = cap.read()
            if ret == False:
                continue
            src = frame.copy()
            src = cv2.resize(src, (800, 600))
            src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            cv2.namedWindow(window_name)
            cv2.resizeWindow(window_name, 800, 600)
            # cv2.createTrackbar(trackbar_type, window_name , 0, max_type, Threshold_Demo)
            # Create Trackbar to choose Threshold value
            cv2.createTrackbar(trackbar_value, window_name , 0, max_value, Threshold_Demo)
            # Call the function to initialize
            Threshold_Demo(0)
            # Wait until user finishes program
            key = cv2.waitKey() & 0xFF
            if key == 27:
                i = nframes-steps
                cv2.destroyAllWindows()
            elif key == ord('n'):
                continue

    def main():
        window = Tk()
        window.title("MOTHe")
        window.geometry('550x300')
        lbl = Label(window, text="WELCOME TO MOTHe", font=("Arial Bold", 10))
        lbl.grid(column=0, row=0)
        combo = Combobox(window)
        combo['values']= ("configure", "generate data", "train", "detection", "track")
        combo.current(0) #set the selected item
        combo.grid(column=0, row=3)
        def click_run():
            combo_val = combo.get()
            if combo_val == "configure":
                window2 = Tk()
                window2.title("Set variables")
                window2.geometry("550x300")
                path = filedialog.askdirectory()
                messagebox.showinfo('Status','succesfully set path as [{}]'.format(path))
                lbl = Label(window2, text="Minimum Threshold value (0 to 254)")
                lbl.grid(column=0, row=0)
                lbl = Label(window2, text="Maximum Threshold value (1 to 255)")
                lbl.grid(column=0, row=1)
                lbl = Label(window2, text="Step size for detection and tracking(1 to 15)")
                lbl.grid(column=0, row=2)
                txt = Entry(window2,width=20)
                txt.grid(column=1, row=0) 
                txt1 = Entry(window2,width=20)
                txt1.grid(column=1, row=1) 
                txt2 = Entry(window2,width=20)
                txt2.grid(column=1, row=2) 
                messagebox.showinfo('Status','Select the video file you would like to use to set box size')
                file = filedialog.askopenfilename()
                file = file.split("/")
                file = file[-1]
                messagebox.showinfo('Status','Using [{}] to determine the size of the bounding box'.format(file))
                def get_txt():
                    thresh_min = int(txt.get())
                    thresh_max = int(txt1.get())
                    step_dg = int(txt2.get())
                    inst = mothe(path, thresh_min, thresh_max, step_dg)
                    inst.set_config(file)
                    window2.destroy()
                    messagebox.showinfo('Update','Configuration file has been saved. Proceed to data generation!')
                btn3 = Button(window2, text="GENERATE CONFIGURATION FILE", command = get_txt)
                btn3.grid(column=1, row=3)
            elif combo_val == "generate data":
                window3 = Tk()
                window3.title("Set variables")
                window3.geometry("550x300")
                messagebox.showinfo('status','Select video to generate your dataset')
                path = filedialog.askopenfilename()
                path = path.split("/")
                path = path[-1]
                messagebox.showinfo('Status','Using [{}] for data generation'.format(path))
                lbl = Label(window3, text="Name of the class")
                lbl.grid(column=0, row=0)
                lbl = Label(window3, text="Step size between frames")
                lbl.grid(column=0, row=1)
                selected = StringVar(window3, "1")
                rad1 = Radiobutton(window3,text='yes', variable=selected, value="1")
                rad2 = Radiobutton(window3,text='no', variable=selected, value="2")
                rad1.grid(column=1, row=0)
                rad2.grid(column=2, row=0)
                txt1 = Entry(window3,width=20)
                txt1.grid(column=1, row=1)
                with open("config.yml", "r") as stream:
                    config_data= yaml.safe_load(stream)
                rt_path = config_data["root_dir"]
                thresh_min = (int(config_data["threshold_value1"]))
                thresh_max = (int(config_data["threshold_value2"]))
                step = (int(config_data["step_for_dt"]))
                def get_txt():
                    step_dg = int(txt1.get())
                    if selected.get()=="1":
                        class_name = "yes"
                    elif selected.get()=="2":
                        class_name = "no"
                    inst = mothe(rt_path, thresh_min, thresh_max, step)
                    inst.generate_dataset(path, class_name, step_dg)
                    messagebox.showinfo('Update','Data generation completed for {} video and {} class'.format(path, class_name))
                btn4 = Button(window3, text="GENERATE DATA", command = get_txt)
                btn4.grid(column=1, row=2)  
            elif combo_val == "train":
                with open("config.yml", "r") as stream:
                    config_data= yaml.safe_load(stream)
                rt_path = config_data["root_dir"]
                thresh_min = (int(config_data["threshold_value1"]))
                thresh_max = (int(config_data["threshold_value2"]))
                step = (int(config_data["step_for_dt"]))
                inst = mothe(rt_path, thresh_min, thresh_max, step)
                inst.train_model()
                messagebox.showinfo('Update','Model generation completed. Proceed to perform detection and tracking!')
            elif combo_val == "detection":
                messagebox.showinfo('Status','Select video file to start detection')
                path = filedialog.askopenfilename()
                path = path.split("/")
                path = path[-1]
                messagebox.showinfo('Status','Using [{}] video for detection'.format(path))
                messagebox.showinfo('Status','Select model file to start detection')
                #path1 = filedialog.askopenfilename()
                path1 = filedialog.askdirectory()
                path1 = path1.split("/")
                path1 = path1[-1]
                messagebox.showinfo('Status','Using [{}] model for detection'.format(path1))
                with open("config.yml", "r") as stream:
                    config_data= yaml.safe_load(stream)
                rt_path = config_data["root_dir"]
                thresh_min = (int(config_data["threshold_value1"]))
                thresh_max = (int(config_data["threshold_value2"]))
                step = (int(config_data["step_for_dt"]))
                inst = mothe(rt_path, thresh_min, thresh_max, step)
                inst.detection(path, path1)
                messagebox.showinfo('Update','Object detection completed. Proceed to perform tracking!')
            elif combo_val == "track":
                messagebox.showinfo('Status','Select video file to start detection')
                path = filedialog.askopenfilename()
                path = path.split("/")
                path = path[-1]
                messagebox.showinfo('Status','Using [{}] video for tracking'.format(path))
                messagebox.showinfo('Status','Select model file to start detection')
                #path1 = filedialog.askopenfilename()
                path1 = filedialog.askdirectory()
                path1 = path1.split("/")
                path1 = path1[-1]
                messagebox.showinfo('Status','Using [{}] model for tracking'.format(path1))
                with open("config.yml", "r") as stream:
                    config_data= yaml.safe_load(stream)
                rt_path = config_data["root_dir"]
                thresh_min = (int(config_data["threshold_value1"]))
                thresh_max = (int(config_data["threshold_value2"]))
                step = (int(config_data["step_for_dt"]))
                inst = mothe(rt_path, thresh_min, thresh_max, step)
                inst.tracking(path, path1)
                messagebox.showinfo('Update','Object tracking completed')

        btn2 = Button(window, text="Run", command = click_run)
        btn2.grid(column=3, row=3)   
        btn1 = Button(window, text="Help", command = mothe_gui.click_help)
        btn1.grid(column=3, row=5)
        btn3 = Button(window, text="Determine threshold", command = mothe_gui.click_determine_thresh)
        btn3.grid(column=3, row=4)
        
        window.mainloop()

mothe_gui.main() 
