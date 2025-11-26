import asyncio
import time
import cvzone
import edge_tts
import pygame
# from playsound import playsound
from ultralytics import YOLO
from picamera2 import Picamera2, Preview
import cv2

model = YOLO('weights/custom/best9.pt')
classNames = ['BAYAS3', 'Battery', 'Camera', 'Capteur-Gaz', 'DRV8825 driver', 'Esp', 'Flex Sensor', 'GPS', 'L293D',
              'LCD-Display', 'LED', 'STM',
              'TB6600 Driver', 'Ultrasonico_sensor', 'A4988 driver', 'Arduino', 'Board', 'DC motor',
              'Display', 'Multimeter', 'Perforated PCB', 'Rasberry', 'Resistor', 'Servo Motor', 'Stepper motor']

# cap = cv2.VideoCapture("/dev/media3")
picam2 = Picamera2()
picam2.start_preview(Preview.NULL)  # optional
picam2.start()
cap = picam2
pygame.mixer.init()

detected_components = set()


async def generate_speech(components):
    # Read language choice
    try:
        with open("language.txt", "r") as f:
            lang = f.read().strip()
    except:
        lang = "en"  # Default

    # Read correct description file
    with open(f"./description/{lang}/{components}-{lang}.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # Choose voice based on language
    if lang == "fr":
        voice = "fr-FR-DeniseNeural"
    else:
        voice = "en-CA-ClaraNeural"
    output_file = "./speaker/output.mp3"

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)


# Desired output size
OUTPUT_WIDTH = 640
OUTPUT_HEIGHT = 460

freeze_start = None
frozen_frame = None
freeze_duration = 2  # seconds

# ---------------- ADDED VARIABLES FOR CONSISTENCY CHECK ----------------
last_detected = None
same_count = 0
required_consistency = 5  # number of consecutive frames to confirm detection
# ----------------------------------------------------------------------

while True:
    if freeze_start is not None:
        # If we are in freeze mode
        if time.time() - freeze_start < freeze_duration:
            cv2.imshow("Video Detection", frozen_frame)  # Show frozen frame
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            continue
        else:
            # End freeze
            freeze_start = None

    # success, img = cap.read()
    success = True
    if not success:
        break

    img = picam2.capture_array()  # capture frame
    # success, img = cap.read()
    success = True
    if not success:
        break
        # ---------------- DIGITAL ZOOM ----------------
    zoom_factor = 1.5
    height, width = img.shape[:2]
    new_width = int(width / zoom_factor)
    new_height = int(height / zoom_factor)
    x1 = (width - new_width) // 2
    y1 = (height - new_height) // 2
    img = img[y1:y1 + new_height, x1:x1 + new_width]
    # ------------------------------------------------
    img = cv2.resize(img, (OUTPUT_WIDTH, OUTPUT_HEIGHT))
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
    results = model(img, imgsz=640)

    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            bbox = (x1, y1, x2 - x1, y2 - y1)

            conf = box.conf[0].item()
            if conf > 0.5:
                cls = int(box.cls[0])
                cvzone.cornerRect(img, bbox, colorC=(0, 121, 255))
                cvzone.putTextRect(img, f"{classNames[cls]} {conf:.2f}",
                                   (max(0, x1), max(35, y1 - 10)),
                                   scale=1.5, thickness=2, colorR=(0, 100, 255))
                res = classNames[cls]

                # ---------------- CONSISTENCY CHECK EMBEDDED ----------------
                if last_detected == res:
                    same_count += 1
                else:
                    last_detected = res
                    same_count = 1

                if same_count >= required_consistency:  # Confirm detection
                    if res not in detected_components:
                        detected_components.add(res)
                        frozen_frame = img.copy()

                        asyncio.run(generate_speech(res))

                        mp3_file_path = f"./speaker/output.mp3"
                        pygame.mixer.music.load(mp3_file_path)
                        pygame.mixer.music.play()
                        while pygame.mixer.music.get_busy():
                            pygame.time.Clock().tick(10)

                        # Save current frame
                        freeze_start = time.time()  # Start freeze timer
                        same_count = 0  # reset after freezing
                # -----------------------------------------------------------

    cv2.imshow("Video Detection", img)
    cv2.moveWindow("Video Detection", 0, 0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cap.release()
picam2.stop()
cv2.destroyAllWindows()
