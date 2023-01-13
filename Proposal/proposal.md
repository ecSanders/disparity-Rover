# Project Proposal - Visual SLAM Rover

| Name | Email | Phone |
|------|-------|-------|
| Erik Sanders | san17015@byui.edu | 602-686-5613 |
| Jared Perlic | jrperlic@gmail.com | 970-657-6957 |
| Tyson Nipges-Mergel | nip20001@byui.edu | 360-223-8504 |

## Abstract

The goal of this project is to create a rover that can be used for exploration or surveillance. To that end, the rover, outfitted with a stereo camera and a Raspberry Pi, will generate a point cloud using the Visual SLAM (Visual Simultaneous Localization and Mapping, aka vSLAM) algorithm.

## Background

We all have different backgrounds and areas of expertise. Some of us have worked with computer vision algorithms before, while others are familiar with robotics.

Each team member has had experiences that will help the group succeed. Erik came up with the idea of implementing vSLAM in the fall of 2022. He is well-versed in computer vision and artificial intelligence, and he was recently hired as a computer vision engineer for Space Dynamic Labs. Jared has been involved in robotics since grade school. As a result, he possesses a skill set that is ideal for programming robots. Tyson understands Python at a high level and can answer questions that others would find difficult to answer.

SLAM algorithms have been around for decades; research has been going on since the 1990s. We will not be venturing into uncharted territory with vSLAM. Instead, we will try to replicate what has already been discovered and learned for our own benefit.

![Topic Web of Visual SLAM Rover](topic-web.jpg)

## Description

For this project, we will construct a small rover about the size of an RC car. It will travel using two motors connected to tank treads. However, it will not be capable of traversing rough terrain. A Raspberry Pi and a stereo camera will be installed. Near-ground level feed will be captured by the stereo camera. The Raspberry Pi will serve as the transmitter, receiving commands from the controller and sending data from the stereo camera. The controller will serve as the "brain," running the SLAM algorithm (more on that later) and generating a point cloud. This point cloud functions as a map that provides information about the nearby area to the operator.

This project would be beneficial to military or space agencies. For instance, the Visual SLAM rover could help with space exploration. Particularly on Mars or other planetary surfaces, rovers outperform manned missions. Bearing this in mind, our target audience would be the military or a space agency. Assuming that the user or operator will be a member of our target audience, then the procedure for using the robot would be as follows:

1. The operator will control the movements of the rover using a controller. (Specifically, the Raspberry Pi will receive the movement instructions from the controller and move accordingly.)
2. The depth camera will be taking images at a rate of 25 frames per second and feeding those images to the controller's computer.
3. The controller's computer, using OpenCV and the vSLAM algorithm, will process the images and generate a point cloud.

The vSLAM algorithm will be developed in Python using the OpenCV library, but the majority of the physical work will be done in the robot lab (STC 239) on Mondays, Wednesdays, and Fridays from 2–3 p.m.

The first stage of the project will be to build the rover and connect it to the controller. The second stage will be to get camera feed. The final stage will be to perfect the vSLAM algorithm in order to generate the point cloud. The project is complete when the controller's point cloud is accurate and precise within a small room.

## Significance

This project will be significant because it will demonstrate our algorithmic abilities as well as our computer vision skills and experience. It will be something we can put on our resumes, and it will certainly impress prospective employers.

## New Computer Science Concepts

To complete this project, we will need to learn three new things: 1) how the vSLAM algorithm works; 2) how to implement Visual SLAM; and 3) how to use a Raspberry Pi. We have no prior experience with Visual SLAM, and we have never used a Raspberry Pi.

In addition, we will use programming languages and libraries that we are already familiar with in novel ways. To complete this project, we expect to use the Python OpenCV library.

## Interestingness

This project interests and excites us because it combines our interests in robotics and programming. The Visual SLAM algorithm, in particular, is at the forefront of robotic mapping, making this our opportunity to demonstrate just how far we've come since we were a part of NXT Robotics in middle school.

The problem domain of computer vision is both deep and far-reaching. We anticipate that computer vision will remain relevant in the tech industry for many years, and we should be familiar with it for our future careers.

## Tasks and Schedule

| Week | Tasks |
| ---- | ----- |
| 1 | Project Approval, Generate Ideas |
| 2 | Project Proposal, Acquire Robot Parts |
| 3 | Stage One, Build Rover |
| 4 | Stage One, Connect Rover to Controller |
| 5 | Stage Two, Learn OpenCV |
| 6 | Stage Two, Obtain Live Camera Feed |
| 7 | Stage Three, vSLAM Step One |
| 8 | Stage Three, vSLAM Step Two |
| 9 | Stage Three, vSLAM Step Three |
| 10 | Stage Three, vSLAM Step Four |
| 11 | Stage Three, vSLAM Step Five |
| 12 | Stage Three, Refine vSLAM Algorithm |
| 13 | Project Completion |
| 14 | Project Presentation |

Admittedly, this schedule is quite aggressive in the beginning. We want to be focused on the Visual SLAM algorithm by week 7, and we think that is reasonable. In order for that to happen, we need to complete the first two stages quickly.

We are prepared to spend roughly 130 hours on this project per person. That amounts to approximately 9.5 hours per week, which is in line with class expectations. It is difficult to prove that the project will not take over 200 hours per person; we cannot know the future. That being said, we can assume that the project will not take that long because of the existence of Visual SLAM libraries in OpenCV. If we cannot figure out Visual SLAM within 200 hours, we can default to a pre-built library.

The completion of the three stages will determine our success and progress. Each stage is a checkpoint that brings us closer to completion.

## Resources

For this project, we are willing to spend up to $250 on equipment. The majority of that will go toward a mid-level stereo camera, since that is critical for our project. The remainder of the equipment can be borrowed from the school. We intend to use free software. Finally, we do not anticipate any dependency issues—we have previously used Python's OpenCV library and are confident it will meet our needs.

### Hardware

- Raspberry Pi
- Stereo camera
- Xbox controller

### Software

- Git (Version Control)
- Python's OpenCV library
- Visual Studio Code (IDE)