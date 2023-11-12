import tkinter as tk
from tkinter import messagebox
import requests
from PIL import ImageGrab, ImageTk
import io
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class ScreenshotUploader:
    def __init__(self, root):
        self.root = root
        self.root.title("Screenshot Uploader")

        # GUI Elements
        self.label = tk.Label(root, text="Screenshot Uploader")
        self.label.pack(pady=10)

        self.button_capture = tk.Button(root, text="Capture Screenshot", command=self.capture_screenshot)
        self.button_capture.pack(pady=10)

        self.button_upload = tk.Button(root, text="Upload Screenshot", command=self.upload_screenshot)
        self.button_upload.pack(pady=10)

    def capture_screenshot(self):
        # Capture screenshot using Pillow (cross-platform)
        screenshot = ImageGrab.grab()

        # Display the screenshot in a new window
        screenshot_window = tk.Toplevel(self.root)
        screenshot_window.title("Captured Screenshot")

        # Convert the screenshot to Tkinter PhotoImage format
        screenshot_tk = ImageTk.PhotoImage(screenshot)

        # Create a label to display the screenshot
        label_screenshot = tk.Label(screenshot_window, image=screenshot_tk)
        label_screenshot.image = screenshot_tk  # Keep a reference to prevent garbage collection
        label_screenshot.pack()

        # Close the screenshot window on click
        label_screenshot.bind("<Button-1>", lambda event: screenshot_window.destroy())

    def upload_screenshot(self):
        screenshot = ImageGrab.grab()
        screenshot_bytes = io.BytesIO()
        screenshot.save(screenshot_bytes, format='PNG')

        api_endpoint = os.getenv("API_ENDPOINT")
        phone_number = os.getenv("PHONE_NUMBER")

        data = {
            'remarks': 'Active Application Name',
            'phone': phone_number,
        }
        files = {'image': screenshot_bytes.getvalue()}

        try:
            response = requests.post(api_endpoint, data=data, files=files)
            response_data = response.json()

            if response_data['status'] == 'success':
                success_message = f"File uploaded successfully!\nFile Path: {response_data['data']['file_path']}\n" \
                                  f"Remarks: {response_data['data']['remarks']}\n" \
                                  f"Phone: {response_data['data']['phone']}\n" \
                                  f"Timestamp: {response_data['data']['timestamp']}"
                messagebox.showinfo("Success", success_message)
            else:
                messagebox.showerror("Error", f"API Error: {response_data['message']}")

        except requests.RequestException as e:
            messagebox.showerror("Error", f"Request Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotUploader(root)
    root.mainloop()
