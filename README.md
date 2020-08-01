# INSTALLATIONS AND PREREQUISITES

## INSTALLING ANACONDA FOR LINUX (DEBIAN DISTIBUTIONS)

1. Execute the following command in the terminal

`$ apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6 libcanberra-gtk-module libcanberra-gtk3-module`

2. Download the Anaconda distribution from the following website

*__https://www.anaconda.com/products/individual#linux__*

3. Execute the following command in the terminal to install the python3 anaconda distribution

`$ bash ~/Downloads/Anaconda3-2020.02-Linux-x86_64.sh`

4. Press positive responses for all options(Ex: yes/OK)

5. exit the terminal. Open a new terminal and execute the following command

`$ source .bashrc`

# Setting up the environment (Linux/Windows/Mac)

1. Open the terminal/anaconda shell in windows. Install python3.6 if it does not exist in the anaconda environment. 
 You can check the python version by running- 
 
   `$ python --version`
   
 We need python 3.6 to run the MOTHe app, so if your current version is any other version (eg. >3.6 or < 3.6), execute the following command to install python 3.6

`$ conda install python=3.6`

2. Create a virtual environment in anaconda with python3.6. Execute the following command in the terminal

`$ conda create -n mothe python=3.6 anaconda`

3. Activate the virtual environment. If the name of the virtual environment is 'mothe', Execute the following command in the terminal. Replace mothe with the name of your environment if it is not mothe

`$ conda activate mothe`

4. Install the tkinter graphical module by executing the following command

`$  conda install -c anaconda tk `

5. Install the pip package manager from the conda repository by executing the following command

`$  conda install -c anaconda pip `

6. Use the requirement.txt file to install all teh modules required by mothe

`$ pip install -r requirement.txt`


# Running MOTHe app

1. Download/clone this repository to your computer. If you will be running MOTHe on our sample videos, download and copy untracked videos from [here](https://figshare.com/s/82661a4fd39008fae445) to the MOTHe folder which you just downloaded.

2. Enter the anaconda environment

Windows: start Anaconda sheel from the start menu

Linux: `$ conda activate mothe`

3. Change directory to MOTHe folder

Windows:

Linux: cd MOTHE-GUI

4. Run the MOTHe GUI app

`$ python mothe_gui.py`

5. Follow below steps to run different functions of the app

**Step1** Configuration

This step is used to set parameters of MOTHe. All the parameters are saved in config.yml. Parameters to be set in this step - home directory, cropping size of animals in the videos, path to video files etc.

Select the configure option from drop down menu and press "run" button. It will prompt you to enter the path of the MOTHe directory, select the directory and confirm. Next it will ask you to select an example video. You can select any video from your video database.


next prompt is to enter the threshold values and step size for detection and tracking. The min and max threshold values depends on the specific case study (contrast between animal and background) and may take a few trial and error attempts to get it right (Read section Choosing color threshold for more details). For the blackbuck videos, we have chosen 0 and 150 as the min and max threshold values and 150 and 250 for the wasp videos. You will also specify a step size (no. of frames to skip for detection and tracking task). If for any reason, you want to run the detection for every n frames instead of all the frames (it can speed up the detection task significantly). To track the video without skipping any frames, enter the step size as 1.

A window appears during the configuration process which is a frame of the test video you have chosen. This step is to determine the size of the animal to be detected and tracked. This value also helps in the dataset generation phase. Make sure to choose the most accomodating animal on the screen to avoid occlusions and missed detections later.

<br>
<img height="350" src="https://github.com/tee-lab/mothe/blob/master/mothe_screenshots/10_drag_across_animal.png">
<br>

Click and drag across the animal to set the animal size for the configuration.


<br>
<img height="350" src="https://github.com/tee-lab/mothe/blob/master/mothe_screenshots/11_press_c_twice.png">
<br>

Press the **c** key once to view the cropped animal. If satisfied with the click and drag process, proceed to press the **c** key **again** to confirm and end the configuration process.


<br>
<img height="350" src="https://github.com/tee-lab/mothe/blob/master/mothe_screenshots/12_creates_config_file.png">
<br>

You can view and change the *config.yml* file created in the mothe folder.

__Step 2: Data Generation__


This program will pick frames from the videos, user can click on animals or background in these images to create samples for both categories (animal and background). Examples of animal of ineterst will be saved in the folder **yes** and background in the folder **no**.
User needs to generate at least 8k-10k samples for each category (see section **How much training data do I need?** for detailed guidelines). One must ensure to take a wide representation of forms in which animals appears in the videos and same for the background variation.

Mothe supports only binary classification. Therefore name the classes 'yes' for positive examples and 'no' for background examples. The data generation method takes a **step size** argument as well which helps the user to keep the number of examples per video in check. (Ex: a higher step size limits the number of frames per video. if a video is very long, one can set a higher step size to skip through unwated and consecutive frames.) 

`$ mothe.generate_dataset("path/to/video", "class_name")`

<br>
<img height="350" src="https://github.com/tee-lab/mothe/blob/master/mothe_screenshots/14_window_appears.png">
<br>

A window appears which is a frame of the video you have chosen. Start generating data at this point.

<br>
<img height="350" src="https://github.com/tee-lab/mothe/blob/master/mothe_screenshots/15_click_and_press_a.png">
<br>

Click at the center of the animal once. The algorithm calculates the size of the bounding box based on the config file entry. Press the **s** key once to crop and store the animals once we have selected all the animals in the frame. Then it will take us to the next frame automatically. Press the **n** key to proceed to the next frame if the current frame is not worth collecting data from. Any selected animals are not cropped and stored if **n** key is pressed. It just takes us to the next frame. Press the **u** key if you want to undo a perticular selection that you have made. Once you are done collectiong samples from a video, press **esc** key to complete the process for this video. You shall repeat this process for multiple videos to sample training examples as widely as possible.

<br>
<img height="350" src="https://github.com/tee-lab/mothe/blob/master/mothe_screenshots/16_creates_class_folder.png">
<br>

At this point, a class folder is created in the mothe folder which stores all animal examples.

<br>
<img height="350" src="https://github.com/tee-lab/mothe/blob/master/mothe_screenshots/17_starts_storing_data.png">
<br>

Data starts to get stored in the class folder.


<br>
<img height="350" src="https://github.com/tee-lab/mothe/blob/master/mothe_screenshots/18_select_all_individuals.png">
<br>

Repeat this process for the 'no' class too. Select all background examples in this case. At this point you will have two class folder with many examples to train the neural network.


<br>
<img height="350" src="https://github.com/tee-lab/mothe/blob/master/mothe_screenshots/19_train_model.png">
<br>

**For testing:**
If you wish to test (learn how to run) this module, download our video clips from [here](https://figshare.com/s/82661a4fd39008fae445). You can then generate samples by choosing any of these videos. If you directly want to proceed to next steps, download our training data from the same drive.


**Step 3: Training the CNN**

 To train the neural network, select the "train" option from the drop down menu-
 
<br>
<img height="350" src="https://github.com/tee-lab/mothe/blob/master/mothe_screenshots/20_post_training_graphs.png">
<br>

After successfully training the model, two graphs appear on the screen. The loss graph starts at a higher point and if the correct learning rate is applied, it takes a drastic decline and starts to plateau out as it reaches near zero. If a very high learning rate is applied, the graph starts travelling upwards instead of downwards. If a slightly higher learning rate is applied, it will not reack a closer point towards the zero line. The accuracy curve should travel upwards sharply and plateau out. It is important to avoid over fitting of data. This can be done by using adequate variance in the examples we generate during data generation. It is also important not to have too much variance since the accuracy may go down even though the network can generalize fairly well. For this stage, please use the link provided below to use the already generated data to train the network. 

<br>
<img height="350" src="https://github.com/tee-lab/mothe/blob/master/mothe_screenshots/21_stores_model.png">
<br>

After training, the model gets stored in the mothe directory as *mothe_model.h5py*. This model will be used to detect and track animals in the test videos.


<br>
<img height="350" src="https://github.com/tee-lab/mothe/blob/master/mothe_screenshots/22_start_detection.png">
<br>

**Step 4: Object detection**

This step will detect the animals (object of interest) in the video frames. As mentioned earlier, this process is done in two steps - first the code predicts the areas in which animal may be potentially present (localisation) and then these areas are passes to the network for classification task. For localisation, we need thrsholding approach which gives us regions which have animals as well as background noise.

Initiate the detection process by selecting detection option and pressing the run button. It will prompt to enter the name of a test video and the model which you want to use. You can use the already trained model availab;le in MOTHe Github repository to run detection on blackbuck or wasp videos. 


<br>
<img height="350" src="https://github.com/tee-lab/mothe/blob/master/mothe_screenshots/23_stores_video_csv.png">
<br>

After the successful detection, a detection video and *.csv* are generated in the mothe folder.

<br>
<img height="350" src="https://github.com/tee-lab/mothe/blob/master/mothe_screenshots/24_start_tracking.png">
<br>

**STep 5: Object tracking**

This step is used to ascribe unique IDs to the detected animals and it gives us thetrajectoris of the animals. 
It will use the detections from previous step. Hence, the input for this step would be original video clip and *.csv* generated in the previous step.

Initiate the tracking process by selecting "track" option.

`$ mothe.tracking("path/to/the/video/file", "path/to/the/trained/model")`


<br>
<img height="350" src="https://github.com/tee-lab/mothe/blob/master/mothe_screenshots/25_stores_video_csv.png">
<br>

After the successful tracking, a tracking video and csv are generated in the mothe folder.



## HOW MUCH TRAINING DATA DO I NEED?

MOTHe uses a CNN which uses a set of labelled examples to learn the features of the objects. Neural Networks generally work well with huge number of training samples. We recommend using at least 8-10k image examples for the animal category. This number may need to be increased if the animal of interest shows a lot of variation in morphology. For example, if males and females are of different colors, it is important to include sufficient examples for both of them. Similarly, if the background is too heterogeneous then you may need more training data (around 1500-2000 samples for different types of variations in the background).
For example to train the MOTHe on our blackbuck videos, we used 9800 cropped samples for blackbuck (including males and females) and 19000 samples for the background because background included grass, soil, rocks, bushes, water etc.


## CHOOSING COLOR THRESHOLDS

The object detection steps requires user to enter threshold values in the config files. Object detection in MOTHe works in two steps, it first uses a color filter to identify the regions in the image on which to run the classification. We use color threshold to select these regions. You can see the values of thresholds for blackbuck and wasp videos in the *config.yml* file.
If you are running MOTHe on a new dataset, there are two ways to select appropriate threshold values:

1. You may open some frames from different videos in an interactive viewer (for example MATLAB image display), you can then click on the pixels on animal and check the RGB values (take the avergae of all 3 channels). Looking at these values in multiple instances will give you an idea to choose a starting minimum and maximum threshold. 
Run the detection with these thresholds and you can improve the detection by hit and trial method to tweak the threshold.

2. You can compare your videos to wasp and blackbuck videos and start with threshold values to which your data is more similar. For example, if your animal looks more similar to blackbuck in color and lighting conditions, you may start with default thresholds and improve the detection by changing lower and upper threshold by little amount at a time.








