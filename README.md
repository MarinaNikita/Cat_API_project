Cat API Project
Overview
This project is an API testing project built using Python, Flask, and the requests library. The main objective is to test file upload functionality for images, ensuring that the correct responses are returned based on different scenarios (valid/invalid file types, missing files, etc.).

Features
Upload image files via an API endpoint.
Validate that images are successfully uploaded and returned in the response.
Handle cases where no file or an invalid file type is uploaded.
Project Structure
app.py: Main Flask application to handle file uploads.
tests/: Contains test scripts to validate the file upload functionality.
Dependencies
Flask: Web framework for building the API.
requests: Used for sending HTTP requests in tests.
os: For handling file operations (such as removing test files).
Installation
To get started with this project, follow the steps below:

Clone the repository:

git clone https://github.com/yourusername/Cat_API_project.git
cd Cat_API_project

Install the necessary dependencies:
pip install -r requirements.txt

Running the Application
To run the Flask application locally:
Open a terminal and navigate to the project directory.

Run the Flask app:
python app.py
This will start the Flask server at http://127.0.0.1:5000.

Running the Tests
The tests for the file upload functionality are located in the tests/test_upload.py file.

To run the tests:
Open a terminal and ensure the Flask app is running.

In another terminal window, run the test script:
python tests/test_upload.py
The tests will check the following scenarios:

Uploading a valid image.
Displaying the uploaded image on the homepage.
Uploading no file.
Uploading a file with an invalid type.

If all tests pass, you will see the message All tests passed!.

Test Functions:

test_upload_image()
Description: Tests uploading a valid image file.
Expected Outcome: Status code 200 (OK), and the image URL should be present in the response.

test_image_display()
Description: Tests if the uploaded image is displayed correctly on the homepage.
Expected Outcome: Status code 200 (OK), and the image should be in the response content.

test_no_file_uploaded()
Description: Tests the case when no file is uploaded.
Expected Outcome: Status code 400 (Bad Request), with the message No file part.

test_invalid_file_type()
Description: Tests uploading a file with an invalid file type (e.g., .txt file).
Expected Outcome: Status code 400 (Bad Request), with the message Invalid file type.

MIME Types
MIME (Multipurpose Internet Mail Extensions) types are used to specify the type of content being sent over the network.
Here are some common MIME types:

text/plain: Plain text files (e.g., .txt).
image/jpeg: JPEG images (e.g., .jpg).
application/json: JSON files (e.g., .json).
multipart/form-data: Used for forms with file uploads.

License
This project is licensed under the MIT License - see the LICENSE file for details.