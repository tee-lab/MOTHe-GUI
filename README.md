## MOTHe-GUI

#INSTALLING ANACONDA FOR LINUX (DEBIAN DISTIBUTIONS)

1. Execute the following command in the terminal
$ apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

2. Download the Anaconda distribution from the following website
*__https://www.anaconda.com/products/individual#linux__*

3. Execute the following command in the terminal to install the python3 anaconda distribution
$ bash ~/Downloads/Anaconda3-2020.02-Linux-x86_64.sh

4. Press positive responses for all options(Ex: yes/OK)

5. exit the terminal. Open a new terminal and execute the following command
$ source .bashrc

# SETTING UP ENVIRONMENT

1. Install python3.6 if it does not exist in the anaconda environment. OPen the terminal and execute the following command
$ conda install python=3.6

2. Create a virtual environment in anaconda with python3.6. Execute the following command in the terminal
$ conda create -n py36 python=3.6 anaconda

3. Activate the virtual environment. If the name of the virtual environment is 'mothe', Execute the following command in the terminal. Replace mothe with the name of your environment if it is not mothe
$ conda activate mothe

4. Install the tkinter graphical module by executing the following command
$  conda install -c anaconda tk 

5. Install the pip package manager from the conda repository by executing the following command
$  conda install -c anaconda pip 

6. Clone/download the mothe gui repository from the following link
*__https://github.com/tee-lab/MOTHe-GUI__*

7. change the working directory into the downloaded directory
$ cd MOTHE-GUI

8. Use the requirement.txt file to install all teh modules required by mothe
$ pip install -r requirement.txt

9. Run the python file to start using the mthe application
$ python mothe_gui.py


