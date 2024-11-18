from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# List of allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Function to check if the file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home page
@app.route('/')
def index():
    # Check if there is an uploaded image
    image_url = None
    if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], 'cat.jpg')):
        image_url = url_for('static', filename='cat.jpg')
    return render_template('index.html', image_url=image_url)

# File upload handler
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400  # Return 400 error if no file is provided

    file = request.files['file']

    if file and allowed_file(file.filename):
        # Save the file if it has an allowed extension
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'cat.jpg'))
        return render_template('index.html', image_url=url_for('static', filename='cat.jpg'))  # Display the image
    else:
        return 'Invalid file type', 400  # Return 400 error if the file type is invalid

if __name__ == '__main__':
    app.run(debug=True)



