# MiRo-Project12a

This is the repository for SOFAR Project 12a.

Project by Jacopo Favaro, Fabrizio Zavanone, Muhammad Talha Siddiqui, Muhammad Tahir, Muhammad Sayum Ahmed, Syed Hani Kazmi Hussain.


## Intro

The project is aimed to build a software architecture to control, using audio commands, the social robot MiRo. MiRo has to perform simple actions like moving near a specified target, given its shape and colour.

## Prerequisites

### ROS
The project has been developed and tested with [ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu).

### MIROapp v1.0

To establish a connection with MiRo it is necessary to download and install [MiRo app](http://labs.consequentialrobotics.com/download.php?file=miroapp-200107.apk) on a working Android device.
MiRo and the device communicate via bluetooth. After having established the connection, simply put MiRo in normal mode and check for the correct behaviour (bridge running, files present, battery percentage displayed).
In presence of any kind of problem, put back MiRo in demo mode (being sure that silent and immobile options are checked) and then back to normal.

### MiRo Workstation Setup

Download the [Miro Developer kit](http://labs.consequentialrobotics.com/miro/mdk/).

Follow the instructions from Consequential Robotics [Miro: Prepare Workstation](https://consequential.bitbucket.io/Developer_Preparation_Prepare_workstation.html) to set up your workstation to work with the robot. 
Strictly follow the instructions in the Install **mdk** section as the following steps will rely on this.
Not necessary to make static IP for your workstation (laptop) while setting up connection with MiRo.
For a clear tutorial step-by-step you should visit [Emarolab Miro Repository](https://github.com/EmaroLab/MIRO.git).

### ROS Based Speech Interface

The communication and speech to text part of the project has been hadled by this [repository](https://github.com/EmaroLab/ros_verbal_interaction_node.git), which contains a web interface based on Google Speech Demo.

Clone the repository in your catkin workpace's src folder:

```
$ git clone https://github.com/EmaroLab/ros_verbal_interaction_node.git

```
Once runned, text converted from an audio input will be published on /speech_to_text alongside with its confidence and detected language.
The interface also handles text to speech, but for our project we simply decided to discard this part by publishing on an unusubscribed topic. To do so, modify [speech_web_interface.html](https://github.com/EmaroLab/ros_verbal_interaction_node/blob/master/java-script/speech_web_interface.html), changing the topic name from `/text_to_speech` to something else.

### OpenCV apps 

TO BE DONE

## MiRo-Project12a installation

Inside your catkin workspace's src folder do:

```
$ git clone https://github.com/Thsuva/MiRo-Project12a
$ catkin_make
$ source devel/setup.bash
```

## The modules

* **src/state_machine_main.py**: main file that builds the state machine, which is the back bone of the project, as shown in this UML:

![](https://github.com/Thsuva/MiRo-Project12a/blob/state_machine/docs/StateMachine.jpg)

* **src/states/**: directory which contains all the needed states to make the state machine work (for more specific information, see the readme file inside the folder).
* **src/parser/parser.py**: file that contains the logic to clean up the input from `/speech_to_text` in order to get the required information (action, colour, target). To wake up MiRo, only the chosen "wake up word" (that can be modified inside this file) is needed.

## Acknowledgments

* [ros_verbal_interaction_node](https://github.com/EmaroLab/ros_verbal_interaction_node.git) repository by Luca Buoncompagni
* [MiRo-training](https://github.com/EmaroLab/MiRo-training) repository by Roberta Delrio, Valentina Pericu