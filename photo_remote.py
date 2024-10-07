# How is this different from the local version, photo.py?
# Answer: 
#   - Added import: url_for
#   
# Notes:
#   - No changes to folder setup*
#   - No changes to app.route
#   - No changes to if __name__ == '__main__':
#

from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)

# Folder to save the uploaded photos
UPLOAD_FOLDER = 'uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return '''
    <html>
        <body>
            <h2>Submit a Photo</h2>
            <form action="/upload" method="POST" enctype="multipart/form-data">
                <label for="file">Choose a photo:</label>
                <input type="file" id="file" name="file" accept="image/*">
                <input type="submit" value="Upload Photo">
            </form>
        </body>
    </html>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return f"Photo uploaded successfully: {file.filename}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
    #app.run(debug=True)
