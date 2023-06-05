# Face-Recognition-using-Deep-Learning-Approach

This is a simple web application that performs face recognition on user-uploaded images. It uses the face_recognition library to detect faces in the uploaded images and compare them with known faces to determine the person's name.

## Usage

1. Clone the repository and navigate to the project directory.

2. Install the required dependencies using pip:
- `pip3 install -r requirements.txt`

3. Start the Flask application:
- `python3 main.py`

4. Open a web browser and go to `http://localhost:5000`.

5. Upload an image using the provided form.

6. The application will detect the faces in the image and display the detected person's name.

## Customization

- Modify the `known_faces` dictionary in the `app.py` file to add or change the known faces. Each key-value pair represents a known person's name and the corresponding image file.

- Customize the HTML templates in the `templates` directory to change the appearance of the web pages.


