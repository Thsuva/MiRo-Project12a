# MiRo-Project12a

This is the repository for SOFAR Project 12a.

Project by Jacopo Favaro, Fabrizio Zavanone, Muhammad Talha Siddiqui, Muhammad Tahir, Muhammad Sayum Ahmed, Syed Hani Kazmi Hussain.


## Objective of the Project

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

This module handles speech to text conversion. To install it, run in your catkin workpace's src folder:

```
$ git clone https://github.com/EmaroLab/ros_verbal_interaction_node.git

```

### OpenCV apps 

TO BE DONE

## Architecture of the System

The majority of the project has been thought as a state machine that handles the complex behaviour of MiRo robot. The structure of the state machine is shown in the following UML.

![](https://github.com/Thsuva/MiRo-Project12a/blob/state_machine/docs/StateMachine.jpg)



## Description of the System’s Architecture

### Module < state machine >

This module has been developed by Fabrizio Zavanone and Jacopo Favaro. It uses smach library with python 2.7. The files relative to this module are:

* **src/state_machine_main.py**: main file that builds the state machine, which is the back bone of the project
* **src/states/**: directory which contains all the needed states to make the state machine work (for more specific information, see the readme file inside the folder).
* **src/parser/parser.py**: file that contains the logic to clean up the input from `/speech_to_text` in order to get the required information (action, colour, target). To wake up MiRo, only the chosen "wake up word" (that can be modified inside this file) is needed.

### Module < speech to text >

This module, that handles speech to text conversion, is taken from [this repository](https://github.com/EmaroLab/ros_verbal_interaction_node.git), which contains a web interface based on Google Speech Demo.
Once runned, text converted from an audio input will be published on /speech_to_text alongside with its confidence and detected language.
The interface also handles text to speech, but for our project we simply decided to discard this part by publishing on an unusubscribed topic. To do so, modify [speech_web_interface.html](https://github.com/EmaroLab/ros_verbal_interaction_node/blob/master/java-script/speech_web_interface.html), changing the topic name from `/text_to_speech` to something else.

### Module < name >

TO BE DONE

## Installation and System Testing

To install the system, in your catkin workspace's src folder do:

```
$ git clone https://github.com/Thsuva/MiRo-Project12a
$ cd ..
$ catkin_make
```
To run it, simply type and run:

```
$ roslaunch MiRo-Project12a state_machine.launch
```

**Be sure to launch the app to connect to MiRo only in this moment, otherwise there will be a failure of connection (MiRo topics won't be present in your rostopic list).**
### RQT graph

TO BE DONE

### Demonstration

TO BE DONE

## Report

This is the link to the report: <[Report_MiRo-12a](https://github.com/Thsuva/MiRo-Project12a/blob/state_machine/docs/Report_MiRo-12a.docx)>

## Acknowledgments

* [ros_verbal_interaction_node](https://github.com/EmaroLab/ros_verbal_interaction_node.git) repository by Luca Buoncompagni
* [MiRo-training](https://github.com/EmaroLab/MiRo-training) repository by Roberta Delrio, Valentina Pericu

## Authors
* Jacopo Favaro S3947407@studenti.unige.it
* Fabrizio Zavanone S3945845@studenti.unige.it
* FirstName LastName: email@email.com
