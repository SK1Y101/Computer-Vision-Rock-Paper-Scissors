# Computer-Vision-Rock-Paper-Scissors
In this lab, you will create an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

# Model
A keras model created using [Teachable-Machine](https://teachablemachine.withgoogle.com/) is located within this repository at `source/keras_model`. This has been trained to recognise the three hand gestures associated wth rock paper scissors, as well as a fourth null gesture.

A testing script was provided to ensure this model works, located at `source/RPS-Template.py` to execute it, an appropriate conda environment with opencv-python, keras, and tensorflow is required.

# Standard Game
located at `source/rock_paper_scissors.py` is a simple game that will play Rock-Paper-Scissors. This can be ran without any dependancies.

# Computer Vission Game
located at `source/CV_RPS.py` is the rock-paper-scissor game combined with the keras neural network. This requires the same environment as the keras model above does.