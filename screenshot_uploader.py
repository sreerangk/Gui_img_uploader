import tkinter as tk
from tkinter import messagebox
import requests
from PIL import ImageGrab
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
        screenshot = ImageGrab.grab()
        screenshot.show()

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
