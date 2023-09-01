import cv2
import imutils
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

password = "admin123"
cap = cv2.VideoCapture(0)
enabled = False

def enable_security():
    global enabled
    entered_password = password_entry.get()
    if entered_password == password:
        enable_button.config(state=DISABLED)
        disable_button.config(state=NORMAL)
        status_label.config(text="Camera security enabled", fg="green")
        error_label.config(text="")
        enabled = True
        video_frame.pack()  # Show the video frame
    else:
        error_label.config(text="Incorrect password", fg="red")

def disable_security():
    global enabled
    enable_button.config(state=NORMAL)
    disable_button.config(state=DISABLED)
    status_label.config(text="Camera security disabled", fg="red")
    error_label.config(text="")
    enabled = False
    video_frame.pack_forget()  # Hide the video frame

    if enabled:  # Release the camera only if security was previously enabled
        # Release the camera
        cap.release()

def capture_frame():
    if enabled:
        ret, frame = cap.read()
        frame = imutils.resize(frame, width=400)

        # Convert the frame from BGR to RGB format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create a PIL ImageTk object to display the frame in Tkinter
        image = Image.fromarray(frame_rgb)
        image_tk = ImageTk.PhotoImage(image)

        # Update the image on the label
        video_label.configure(image=image_tk)
        video_label.image = image_tk

    window.after(10, capture_frame)

window = Tk()
window.title("Camera Security For Spyware")

# Apply themed style to the window
style = ttk.Style()
style.theme_use("default")

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window geometry for full screen display
window.geometry(f"{screen_width}x{screen_height}+0+0")

# Background Image
bg_image = Image.open(r"C:\Users\Syed Aziz Ahmed\Downloads\malware_attack.png")  # Replace with your own image file path
bg_image = bg_image.resize((screen_width, screen_height), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame for the video display
video_frame = Frame(window)

# Create a label for the video display
video_label = Label(video_frame)
video_label.pack()

# Password Entry
password_frame = Frame(window)
password_frame.pack(pady=20)  # Add vertical padding
password_label = Label(password_frame, text="Password:")
password_label.pack(side=LEFT)
password_entry = Entry(password_frame, show="*", width=20)
password_entry.pack(side=LEFT)

# Enable Button
enable_button = ttk.Button(window, text="Enable", command=enable_security)
enable_button.pack(pady=5)

# Disable Button
disable_button = ttk.Button(window, text="Disable", command=disable_security, state=DISABLED)
disable_button.pack(pady=5)

# Error Label
error_label = Label(window, text="", fg="red")
error_label.pack()

# Status Label
status_label = Label(window, text="Camera security disabled", fg="red")
status_label.pack(pady=10)

# Start capturing frames
capture_frame()

window.mainloop()
