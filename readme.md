# Vision Detection (Electrical Embedded Object Detection System)

## Overview
This project is a **Vision Detection system** developed for **Raspberry Pi**, capable of detecting **20+ electronic components**. When a component is detected, the system plays an audio description in **English or French**.

## Features
- Detects components such as Arduino, Resistors, Servo Motors, Stepper Motors, DC Motors, and more.
- Dual-language audio output (English & French) for each component.
- Freeze-frame feature for confirmed detection.
- Modular structure: main code, descriptions, audio outputs, and trained model weights.

## File Structure
- `start-menu.py`: Program to select language and start detection.
- `main_pi.py`: Main detection program (runs automatically after Start Detection in the menu).
- `weights/`: Contains trained YOLO model weights.
- `description/`: Text descriptions for each component in EN/FR.
- `speaker/`: Audio outputs generated for each component.
- `.idea/`: IDE configuration files (optional, can be ignored).
- `.venv/`: Local virtual environment (not included in repo).
- `requirements.txt`: Python packages required to run the project.
- `README.md`: Project description.

## Usage
1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Run the start menu program:
```bash
python start-menu.py
```
3. Choose the language and press Start Detection. The system will then automatically run the main detection program using the Raspberry Pi camera.?