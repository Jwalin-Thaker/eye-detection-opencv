## Eye Detection with OpenCV + Python

### Overview:
- This project is an implementation of opencv + python in an attempt to learn how face and eye detection work
- I have used pre-trained classifiers (previously run on thousands of images) in the form of [xml](https://github.com/opencv/opencv/tree/master/data/haarcascades) files (which come bundled with [cv2](https://pypi.org/project/opencv-python) package) to capture facial features and then track them
- Applied geomterical analysis to detect closing of eye with area calculation and distance from facial ends
- Check out the functional demo at https://www.youtube.com/watch?v=EpnMyfZQEjE

**Version config:**
1. Python - `3.7.9`
2. OpenCV - `4.5.4`

*Note: Make sure you have a stable/supported version of Python 3+*

## Steps to run:
1. Clone this repository into your local machine
2. Commands to run:
   1. `pip install -r requirements.txt` (only if single python environment, else change pip to pip3)
   2. `python main.py` (only if single python environment, else change python to python3) 

## Applications:
- This program has applications in the following:
  1. Road accident prevention - detect driver's eyes shutting off
  2. Social media engagement - control mini-games using eye gestures
  3. Medical aid - help bed ridden patients (eg. paralyzed) to naviagte useful functional menus 
  4. Education - detect attentiveness of a learner in online classes


## Future scopes
- I have tried to implement a gui using tkinter under the file `gui.py` which shows a basic menu implementation which can be linked with the data insights coming from the opencv program to navigate and create an application for medical aid
- To better the detecttion and tracking we can tweak the parameters (to smoothen and sharpen at places) in the code as well as perform more training models to create our custom classifiers
- Use other alternatives and approaches like dlib to calculate contours and hulls around the face and use the EAR algorithm to enhance the results
- Have a neural network with layers which enhance the image to generalise for different lighting conditions before applying any opencv in-built functions

*For any further queries or collaborations, email at jthaker1@stevens.edu*

Made with ❤️
