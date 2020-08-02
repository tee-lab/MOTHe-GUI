# MOTHe-GUI

Mothe is a pipeline developed to detect and track multiple animals in a heterogeneous environment. MOTHe is a python based repository and it uses Convolutional Neural Network (CNN) architecture for the object detection task. It takes a digital image as an input and reads its features to assign a category. These algorithms are learning algorithms which means that they extract features from the images by using huge amounts of labeled training data. Once the CNN models are trained, these models can be used to classify novel data (images). MOTHe is designed to be generic which empowers the user to track objects of interest even in a natural setting.

**This repository provides a GUI application to run MOTHe on Linux/Windows/Mac OS.** User needs to install anaconda and then GUI can be run from anaconda environment.
Follow the pre-requisites and installation steps before processding to MOTHe-GUI demonstration.


## INSTALLATIONS AND PREREQUISITES

Visit this wiki page to learn about installing Anaconda for your respective OS. Follow the link below.

*__https://github.com/tee-lab/MOTHe-GUI/wiki__*

Finish these installations and pre-requisites before proceedinf further.

# Running MOTHe app

1. Download/clone this repository to your computer, if not done already. If you will be running MOTHe on our sample videos, download and copy untracked videos from [here](https://figshare.com/s/82661a4fd39008fae445){:target="_blank"} to the MOTHe folder which you just downloaded. For testing purpose, you can download any one video from the untracked videos folder.


2. Enter the anaconda environment

Windows: start Anaconda shell from the start menu

**screenshot required**

Linux: Open the terminal and type- `$ conda activate mothe`

**screenshot required**

3. Change directory to MOTHe folder

Windows: `cd <path to MOTHe-GUI directory>`

Linux: `$ cd MOTHE-GUI`

4. Run the MOTHe GUI app

`$ python mothe_gui.py`


<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/1_gui_start.png">
<br>

5. Follow below steps to run different functions of the app

**Step1** Configuration

This step is used to set parameters of MOTHe. All the parameters are saved in config.yml. Parameters to be set in this step - home directory, cropping size of animals in the videos, path to video files etc.

Select the configure option from drop down menu and press "run" button. It will prompt you to enter the path of the MOTHe directory, select the directory and confirm. Next it will ask you to select an example video. You can select any video from your video database.

The next prompt is to enter the threshold values and step size for detection and tracking. The min and max threshold values depends on the specific case study (contrast between animal and background) and may take a few trial and error attempts to get it right (Read section Choosing color threshold for more details). For the blackbuck videos, we have chosen 0 and 150 as the min and max threshold values and 150 and 250 for the wasp videos. 

You will also specify a step size (no. of frames to skip for detection and tracking task). If for any reason, you want to run the detection for every n frames instead of all the frames (it can speed up the detection task significantly). To track the video without skipping any frames, enter the step size as 1.


<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/2_press_run_configure.png">
<br>

<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/3_press_ok_selecting_path.png">
<br>

<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/4_select_video_set_config.png.png">
<br>

<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/5_video_select_confirmation.png">
<br>

<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/5_video_select_confirmation.png">
<br>

<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/6_fill_in_details.png">
<br>

<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/8_post_config_confirmation.png">
<br>

A window appears during the configuration process which is a frame of the test video you have chosen. This step is to determine the size of the animal to be detected and tracked. This value also helps in the dataset generation phase. Make sure to choose the most accomodating animal on the screen to avoid occlusions and missed detections later.

Click and drag across the animal to set the animal size for the configuration. Press the **c** key once to view the cropped animal. If satisfied with the click and drag process, proceed to press the **c** key **again** to confirm and end the configuration process.

**screenshot required**
**screenshot required**

You can view and change the *config.yml* file created in the mothe folder.

You can now select the next option from drop-down menu of MOTHe-GUI to run data generation step.


__Step 2: Data Generation__


This program will pick frames from the videos, user can click on animals or background in these images to create samples for both categories (animal and background). Examples of animal of ineterst will be saved in the folder **yes** and background in the folder **no**.

User needs to generate at least 8k-10k samples for each category (see section **How much training data do I need?** for detailed guidelines). One must ensure to take a wide representation of forms in which animals appears in the videos and same for the background variation.

Mothe supports only binary classification. Therefore name the classes 'yes' for positive examples and 'no' for background examples. The data generation method takes a **step size** argument as well which helps the user to keep the number of examples per video in check. (Ex: a higher step size limits the number of frames per video. if a video is very long, one can set a higher step size to skip through unwated and consecutive frames). Please note that this step size is different from the one you entered in configure step, this step size allows you to generated data from widely spaced frames of the videos.

<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/9_generate_dataset.png">
<br>

<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/10_select_video.png">
<br>


<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/12_fill_details.png.png">
<br>

A window appears which is a frame of the video you have chosen. Start generating data at this point.

Click at the center of the animal once. The algorithm calculates the size of the bounding box based on the config file entry. 

-Press the **s** key once to crop and store the animals once we have selected all the animals in the frame. Then it will take us to the next frame automatically. 

-Press the **n** key to proceed to the next frame if the current frame is not worth collecting data from. Any selected animals are not cropped and stored if **n** key is pressed. It just takes us to the next frame. 

-Press the **u** key if you want to undo a perticular selection that you have made. 

-Once you are done collectiong samples from a video, press **esc** key to complete the process for this video. 

**You shall repeat this process for multiple videos to sample training examples as widely as possible.**

**screenshot showing selection process**

<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/13_post_generation_update.png">
<br>


**Repeat this process for the 'no' class too.**

Select all background examples in this case. At this point you will have two class folder with many examples to train the neural network.


**For testing:**
If you wish to test (learn how to run) this module, download our video clips from [here](https://figshare.com/s/82661a4fd39008fae445). You can then generate samples by choosing any of these videos. If you directly want to proceed to next steps, download our training data from the same drive.


**Step 3: Training the CNN**

 To train the neural network, select the "train" option from the drop down menu-
 
<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/14_run_train.png">
<br>

After successfully training the model, two graphs appear on the screen. The loss graph starts at a higher point and if the correct learning rate is applied, it takes a drastic decline and starts to plateau out as it reaches near zero. If a very high learning rate is applied, the graph starts travelling upwards instead of downwards. If a slightly higher learning rate is applied, it will not reack a closer point towards the zero line. The accuracy curve should travel upwards sharply and plateau out. It is important to avoid over fitting of data. This can be done by using adequate variance in the examples we generate during data generation. It is also important not to have too much variance since the accuracy may go down even though the network can generalize fairly well. For this stage, please use the link provided below to use the already generated data to train the network. 

<br>
<img height="350" src="https://github.com/tee-lab/mothe/blob/master/mothe_screenshots/20_post_training_graphs.png">
<br>

<br>
<img height="350" src="https://github.com/tee-lab/mothe/blob/master/mothe_screenshots/21_stores_model.png">
<br>

After training, the model gets stored in the mothe directory as *mothe_model.h5py*. This model will be used to detect and track animals in the test videos.


**Step 4: Object detection**

This step will detect the animals (object of interest) in the video frames. As mentioned earlier, this process is done in two steps - first the code predicts the areas in which animal may be potentially present (localisation) and then these areas are passes to the network for classification task. For localisation, we need thrsholding approach which gives us regions which have animals as well as background noise.

Initiate the detection process by selecting 'detection' option and pressing the run button. It will prompt to enter the name of a test video and the model which you want to use. You can use the already trained model availab;le in MOTHe Github repository to run detection on blackbuck or wasp videos. 


<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/15_run_detection.png">
<br>

<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/16_select_video.png">
<br>

<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/18_model_selection.png">
<br>

<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/20_post_detection_update.png">
<br>

After the successful detection, a video with detections and *.csv* are generated in the mothe folder.


**STep 5: Object tracking**

This step is used to ascribe unique IDs to the detected animals and it gives us thetrajectoris of the animals. 
It will use the detections from previous step. Hence, the input for this step would be original video clip and *.csv* generated in the previous step.

Initiate the tracking process by selecting "track" option.

<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/21_run_tracking.png">
<br>

<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/22_select_video.png">
<br>
<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/23_select_video_confirm.png">
<br>
<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/24_select_model.png">
<br>
<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/25_model_selection_update.png">
<br>
<br>
<img height="350" src="https://github.com/tee-lab/MOTHe-GUI/blob/master/gui_screenshots/26_tracking_complete_update.png">
<br>


After the successful tracking, a tracked video and *.csv* are generated in the mothe folder.


This completes all the steps associated with animal detection and tracking in the videos. Once you have tested it on sample videos, you can use MOTHe for your particular dataset. below are some guidelines which will help you select parameters for your videos.



## HOW MUCH TRAINING DATA DO I NEED?

MOTHe uses a CNN which uses a set of labelled examples to learn the features of the objects. Neural Networks generally work well with huge number of training samples. We recommend using at least 8-10k image examples for the animal category. This number may need to be increased if the animal of interest shows a lot of variation in morphology. For example, if males and females are of different colors, it is important to include sufficient examples for both of them. Similarly, if the background is too heterogeneous then you may need more training data (around 1500-2000 samples for different types of variations in the background).
For example to train the MOTHe on our blackbuck videos, we used 9800 cropped samples for blackbuck (including males and females) and 19000 samples for the background because background included grass, soil, rocks, bushes, water etc.


## CHOOSING COLOR THRESHOLDS

The object detection steps requires user to enter threshold values in the config files. Object detection in MOTHe works in two steps, it first uses a color filter to identify the regions in the image on which to run the classification. We use color threshold to select these regions. You can see the values of thresholds for blackbuck and wasp videos in the *config.yml* file.
If you are running MOTHe on a new dataset, there are two ways to select appropriate threshold values:

1. You may open some frames from different videos in an interactive viewer (for example MATLAB image display), you can then click on the pixels on animal and check the RGB values (take the avergae of all 3 channels). Looking at these values in multiple instances will give you an idea to choose a starting minimum and maximum threshold. 
Run the detection with these thresholds and you can improve the detection by hit and trial method to tweak the threshold.

2. You can compare your videos to wasp and blackbuck videos and start with threshold values to which your data is more similar. For example, if your animal looks more similar to blackbuck in color and lighting conditions, you may start with default thresholds and improve the detection by changing lower and upper threshold by little amount at a time.








