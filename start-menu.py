import tkinter as tk
import subprocess

main_process = None  # Global reference to the detection process

# ---------------- Functions ----------------
def start_detection():
    global main_process
    if main_process is None:
        try:
            main_process = subprocess.Popen(["python3", "main.py"])
            status_label.config(text="🟢 Detection Running...", fg="#00ff88")
            start_btn.config(state="disabled", bg="#1a5f3a")
        except Exception as e:
            status_label.config(text=f"❌ Error: {e}", fg="#ff4444")

def stop_detection():
    global main_process
    if main_process:
        main_process.terminate()
        main_process = None
        status_label.config(text="🟠 Detection Stopped", fg="#ffaa44")
        start_btn.config(state="normal", bg="#2ecc71")

def exit_program():
    stop_detection()
    root.destroy()

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Smart Component Detector")
root.attributes('-fullscreen', True)  # Fullscreen
root.config(bg="#0f1419")

# ---------------- Title with shadow effect ----------------
title_shadow = tk.Label(
    root, text="👁️ Smart Component Detector",
    font=("Arial", 24, "bold"), fg="#333333", bg="#0f1419"
)
title_shadow.place(x=52, y=52)

title_label = tk.Label(
    root, text="👁️ Smart Component Detector",
    font=("Arial", 24, "bold"), fg="#00d2ff", bg="#0f1419"
)
title_label.place(x=50, y=50)

# ---------------- Right Side Frame ----------------
right_frame = tk.Frame(root, bg="#1a1f2e", relief="ridge", bd=3)
right_frame.place(relx=0.55, rely=0.15, relwidth=0.4, relheight=0.7)

# ---------------- Language Buttons ----------------
language_frame = tk.Frame(root, bg="#0f1419")
language_frame.place(x=50, y=120)

tk.Label(language_frame, text="Language:", font=("Arial", 16), fg="white", bg="#0f1419").pack(side="left")

def set_language(lang):
    with open("language.txt", "w") as f:
        f.write(lang)
    if lang == "en":
        en_btn.config(bg="#00d2ff", fg="white")
        fr_btn.config(bg="#666666", fg="white")
    else:
        fr_btn.config(bg="#00d2ff", fg="white")
        en_btn.config(bg="#666666", fg="white")

en_btn = tk.Button(language_frame, text="English", command=lambda: set_language("en"),
                   font=("Arial", 12), bg="#00d2ff", fg="white", width=8)
en_btn.pack(side="left", padx=5)

fr_btn = tk.Button(language_frame, text="Français", command=lambda: set_language("fr"),
                   font=("Arial", 12), bg="#666666", fg="white", width=8)
fr_btn.pack(side="left", padx=5)

# ---------------- Buttons ----------------
button_font = ("Arial", 20, "bold")
button_width = 18
button_height = 2
pad_y = 20

start_btn = tk.Button(
    right_frame, text="▶️ Start Detection", font=button_font,
    bg="#2ecc71", fg="white", width=button_width, height=button_height,
    relief="raised", bd=4,
    activebackground="#27ae60",
    command=start_detection
)
start_btn.pack(pady=pad_y)

stop_btn = tk.Button(
    right_frame, text="⏹️ Stop Detection", font=button_font,
    bg="#e67e22", fg="white", width=button_width, height=button_height,
    relief="raised", bd=4,
    activebackground="#d35400",
    command=stop_detection
)
stop_btn.pack(pady=pad_y)

# ---------------- Status ----------------
status_frame = tk.Frame(right_frame, bg="#2c3e50", relief="sunken", bd=2)
status_frame.pack(pady=30, padx=20, fill="x")

status_label = tk.Label(
    status_frame, text="⚪ Waiting...", font=("Arial", 18, "bold"),
    fg="#ecf0f1", bg="#2c3e50", pady=15
)
status_label.pack()

# ---------------- Exit Button ----------------
exit_btn = tk.Button(
    root, text="❌ Exit", font=("Arial", 14, "bold"),
    bg="#c0392b", fg="white", width=8, height=1,
    relief="raised", bd=2,
    activebackground="#a93226",
    command=exit_program
)
exit_btn.place(relx=0.95, rely=0.95, anchor="se")

watermark = tk.Label(
    root,
    text="Made by @Ayoub Chahid",
    font=("Arial", 12, "italic"),
    fg="#aaaaaa",
    bg="#0f1419"
)
watermark.place(relx=0.01, rely=0.98, anchor="sw")
# ---------------- Run ----------------
root.mainloop()
