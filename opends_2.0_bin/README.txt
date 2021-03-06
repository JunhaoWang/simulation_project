OpenDS (Open-source Driving Simulator)
======================================

Version 2.0 - January 17th, 2014 (Built version)


OpenDS is an open source driving simulator for research. The software is 
programmed entirely in Java and is based on the jMonkeyEngine framework, 
a scene graph based game engine which is mainly used for rendering and 
physics computation. OpenDS is distributed under the terms of GNU General 
Public License (GPL).



1. What is contained in this archive
------------------------------------
The archive you downloaded contains an already built version of OpenDS including
the Analyzer to replay a drive and all library files needed to run both. As it 
does NOT contain any scenes, models or tasks (assets), you will have to obtain 
them from http://www.opends.eu separately. OpenDS will not work without a valid
assets-folder. More details about the already available tasks can be found in 
paragraph 7.



2. Getting started
------------------
Binaries for Windows, Mac OS and Linux are contained in this archive. 

1. Make sure you have installed the Java Runtime Environment (JRE) version 7 
   or higher. If not, download it from http://www.java.com
2. Add a new folder 'assets' to the simulator folder (where this README is 
   located) and copy the contents of assets.zip from http://www.opend.eu to that 
   folder (required).
3. Run 'OpenDS.jar' either by double clicking or using console (type: 
   'java -jar OpenDS.jar')
4. Select resolution and proceed with clicking 'OK'.
5. Specify driver’s name (optional).
6. Select which task to load and click 'Start'.

To stop the application, hit the ESC key or close the window.
Press F1 during simulation for default key assignment.



3. Building OpenDS
------------------
In order to build OpenDS from source go to http://www.opend.eu and download the
source code version.



4. Where to find documentation
------------------------------
More information (still growing) and JavaDoc can be found on the project website.



5. Contributors
---------------
a) Concept: Christian Müller
b) Architecture and development: Rafael Math
c) Other contributions:
	Saied Tehrani
	Michael Feld
	Otávio Biasutti
	Daniel Braun
	Gleb Banas
	Till Maurer
d) How to contribute? 
   Please write us using the contact form on the project website.
   Get access to the project's repository.



6. Credits
----------
Digital media assets have been taken from jMonkeyEngine (http://www.jmonkeyengine.org)
if no other reference can be found in the corresponding folder.



7. Available tasks
------------------

ConTReTask/conTReTask.xml (professional version only!)

The Continuous Tracking and Reaction Task (ConTRe Task) is a highly controlled 
driving task that allows fine-grained measurement of steering and event detection 
performance through very few dependent variables. Also, it is a rather artificial 
task that only resembles to realistic driving.
NOTE: This driving task is only available in the professional version of OpenDS


Idealtest2/idealtest2.xml

In this model the traffic light control will be demonstrated by the help of a few
simple intersections. At the beginning, trigger mode is active, i.e. approaching 
vehicles will be detected and the related traffic light will turn green. By 
pressing the "A"-key, you can toggle all traffic light modes: 
TRIGGER -> PROGRAM -> EXTERNAL INPUT -> BLINKING -> OFF. In program mode, all 
traffic lights will obey to a pre-defined list of traffic light rules and in 
external mode traffic lights can be interactively controlled by the experiment 
leader. When you reached modes blinking and off you can go back to trigger mode 
by pressing the "A"-key once more. The trip will be recorded for later analysis 
and in the "data analyzer" folder. Furthermore, a traffic vehicle obeying to traffic
lights will be available.


Paris/paris.xml

This CityEngine model includes photo-realistic textures of Paris and was equipped 
with a bus stop and a roundabout. This model shows how to use the Object Locator tool
to place further objects (cf. ParisTraffic as potential result).


ParisTraffic/parisTraffic.xml

This is the extended model (road signs, traffic, sky texture, triggers, etc.) of the 
aforementioned Paris model.


ReactionTest/reactionTest.xml

This task contains a reaction experiment with instruction screen. The driver has to 
react to suddenly appearing signs. After the drive, a PDF file with a bar chart will 
show up.


Stadtmitte22/stadtmitte22.xml

In order to demonstrate the triggering of events, which are able to perform state 
changes, this model contains three colored boxes (triggers). Usually triggers are 
invisible and vehicles cannot collide with them. Hitting the boxes causes actions 
like moving objects, making them (dis)appear, play sound files, set up reaction 
time measurements, set the driving car to a certain position, etc.


Terrain/terrain.xml

Test track for simple terrain generation from hight map and alpha map.


ThreeVehiclePlatooningTask/ThreeVehiclePlatooningTask.xml (professional version only!)

The Three Vehicle Platooning Task (3VPT) is a more realistic driving task and allows 
measuring many different dependent variables, but is still controlled. It demands 
the driver to control his lateral as well as longitudinal position and additionally 
to detect and respond to several events. 
NOTE: This driving task is only available in the professional version of OpenDS


Video5/video5.xml

This model has been created with CityEngine and shows the ability to model roads in 
hilly terrain. Furthermore, two vehicles (bus and car) will be driving.


Video16/video16.xml

Another CityEngine model showing snow and fog effects.