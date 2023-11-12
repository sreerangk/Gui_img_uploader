# Gui_img_uploader

Screenshot Uploader Application Documentation
Requirements
Before setting up the application, ensure you have the following installed on your system:

Python (3.x recommended)
pip (Python package installer)
Installation
Clone the Repository:

git clone https://github.com/your-username/screenshot-uploader.git
cd screenshot-uploader

Install Dependencies:

pip install -r requirements.txt

Open the screenshot_uploader.py file.
Update the api_endpoint variable with the actual URL of your API.
Update the phone_number variable with a unique identifier, e.g., a phone number.
Run the Application:

python screenshot_uploader.py

Usage
Capture Screenshot:

Click the "Capture Screenshot" button to capture the current screen.
Upload Screenshot:

Click the "Upload Screenshot" button to send the captured screenshot to the specified API endpoint.
Handling API Responses
If the upload is successful, a success message will be displayed with details such as file path, remarks, phone, and timestamp.
If there's an API error or an issue with the request, an error message will be displayed.

Conclusion
The Screenshot Uploader application is now set up and ready to use.
