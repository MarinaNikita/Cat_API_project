import requests
import os

# URL of the website
url = 'http://127.0.0.1:5000/upload'

# Path to the image for testing
file_path = r"C:\Users\marin\PycharmProjects\Cat_API_project\static\cat.jpg"

def test_upload_image():
    # Open the file to upload
    with open(file_path, 'rb') as file:   # using with-statement for file to be properly closed even if exceptions
        files = {'file': file}   # read-binary mode for reading file

        # Send the request to upload the image
        response = requests.post(url, files=files)

        # Check that the status code is 200 (success)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        # Check that the image URL is present in the response (image uploaded successfully)
        assert b'<img src="/static/cat.jpg"' in response.content, "Image not found in the response content"

def test_image_display():
    # Check that the image is displayed on the home page
    response = requests.get('http://127.0.0.1:5000/')
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    # Use 'b' to specify a byte string, as the response content is in byte format.
    assert b'<img src="/static/cat.jpg"' in response.content, "Image not found in the response content"

def test_no_file_uploaded():
    # Send the request without uploading any file
    response = requests.post(url, files={})

    # Check that the status code is 400 (Bad Request)
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert b'No file part' in response.content, "Error message not found"

def test_invalid_file_type():
    # Create a test text file
    file_path_invalid = 'invalid_file.txt'

    # Create an invalid text file for the test
    with open(file_path_invalid, 'w') as f:
        f.write("This is an invalid file for testing purposes")

    # Open the file to upload (in binary mode)
    with open(file_path_invalid, 'rb') as f:
        files = {'file': (file_path_invalid, f, 'text/plain')}
        response = requests.post(url, files=files)

    # Check that the status code is 400 (Bad Request) for invalid file type
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    # Check that the response contains the 'Invalid file type' message
    assert b'Invalid file type' in response.content, "Error message not found"

    # Clean up (delete the file after the test)
    os.remove(file_path_invalid)

# Run the tests
if __name__ == "__main__":
    test_upload_image()
    test_image_display()
    test_no_file_uploaded()
    test_invalid_file_type()
    print("All tests passed!")



