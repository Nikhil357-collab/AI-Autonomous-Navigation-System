# AI-Autonomous-Navigation-System
Built an AI-Based Autonomous Navigation System Simulation using Python, OpenCV, and YOLOv8. The project performs real-time lane detection, object detection, collision risk analysis, steering decisions, and autonomous driving simulation using computer vision and AI.
# AI-Based Autonomous Navigation System

## Project Overview

This project simulates an AI-powered autonomous navigation system using Computer Vision and Artificial Intelligence techniques. The system performs real-time object detection, lane detection, collision risk estimation, and autonomous navigation decision-making using YOLOv8 and OpenCV.

The project demonstrates the perception and behavioral planning pipeline used in modern self-driving vehicle systems.

---

# Features

- Real-Time Object Detection using YOLOv8
- Lane Detection using OpenCV
- Collision Risk Analysis
- Autonomous Steering Decisions
- Speed Control Simulation
- Horn Warning System
- AI Navigation Dashboard
- Real-Time FPS Monitoring

---

# Tech Stack

- Python
- OpenCV
- YOLOv8
- NumPy
- Computer Vision
- Artificial Intelligence

---

# System Workflow

Video Feed
↓
Object Detection
↓
Lane Detection
↓
Collision Analysis
↓
Navigation Decision Engine
↓
Autonomous Driving Simulation

---

# Project Structure

AI_Based_Navigation_System/
│
├── main.py
├── yolov8n.pt
├── road_video.mp4
│
├── detection/
│   ├── object_detection.py
│   ├── lane_detection.py
│   └── collision_warning.py
│
├── navigation/
│   └── steering_logic.py
│
└── utils/
    └── dashboard.py

---

# Installation

```bash
pip install ultralytics opencv-python numpy
