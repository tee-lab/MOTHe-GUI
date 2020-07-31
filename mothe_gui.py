from tkinter import *
from mothe.pipe import mothe
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
import yaml
from tkinter import ttk

class mothe_gui:
    
    def __init__(self):
        pass

    def click_help():
        window1 = Tk()
        window1.title("Help")
        window1.geometry('550x300')
        txt = scrolledtext.ScrolledText(window1,width=500,height=250)
        txt.insert(INSERT,'MOTHe:\nMothe is a pipeline developed to detect and track multiple animals in a heterogeneous environment. \nMOTHe is a python based repository and it uses Convolutional Neural Network (CNN) architecture for the object detection task. \nIt takes a digital image as an input and reads its features to assign a category. \nThese algorithms are learning algorithms which means that they extract features from the images by using huge amounts \nof labeled training data. Once the CNN models are trained, these \nmodels can be used to classify novel data (images). \nMOTHe is designed to be generic which empowers the user to track objects of interest even in a natural setting.')
        txt.grid(column=0,row=0)

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
                    messagebox.showinfo('Update','Configuration file has been saved')
                btn3 = Button(window2, text="GENERATE CONFIGURATION FILE", command = get_txt)
                btn3.grid(column=1, row=3)
            elif combo_val == "generate data":
                window3 = Tk()
                window3.title("Set variables")
                window3.geometry("550x300")
                path = filedialog.askopenfilename()
                path = path.split("/")
                path = path[-1]
                messagebox.showinfo('Status','Using [{}] for data generation'.format(path))
                lbl = Label(window3, text="Name of the class (Ex: yes or no)")
                lbl.grid(column=0, row=0)
                lbl = Label(window3, text="Step size between frames")
                lbl.grid(column=0, row=1)
                txt = Entry(window3,width=20)
                txt.grid(column=1, row=0)
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
                    class_name = txt.get()
                    inst = mothe(rt_path, thresh_min, thresh_max, step)
                    inst.generate_dataset(path, class_name, step_dg)
                    messagebox.showinfo('Update','Data generation completed')
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
                messagebox.showinfo('Update','Model generation completed')
            elif combo_val == "detection":
                path = filedialog.askopenfilename()
                path = path.split("/")
                path = path[-1]
                messagebox.showinfo('Status','Using [{}] video for detection'.format(path))
                path1 = filedialog.askopenfilename()
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
                messagebox.showinfo('Update','Object detection completed')
            elif combo_val == "track":
                path = filedialog.askopenfilename()
                path = path.split("/")
                path = path[-1]
                messagebox.showinfo('Status','Using [{}] video for tracking'.format(path))
                path1 = filedialog.askopenfilename()
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
        btn1.grid(column=3, row=4)
        window.mainloop()

mothe_gui.main() 
