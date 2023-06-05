from flask import Flask, render_template, request
import face_recognition

app = Flask(__name__)

known_faces = {
    "Ehtisham Sadiq": "known_images/ehtisham.jpeg",
    "Zeeshan Sadiq": "known_images/Zeeshan.jpeg",
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No image uploaded"
    
    image = request.files['image']
    image_path = 'static/uploaded_image.jpg'
    image.save(image_path)
    
    uploaded_image = face_recognition.load_image_file(image_path)
    uploaded_face_encodings = face_recognition.face_encodings(uploaded_image)
    
    if len(uploaded_face_encodings) > 0:
        detected_faces = []
        for face_encoding in uploaded_face_encodings:
            face_found = False
            for known_name, known_image in known_faces.items():
                known_face_image = face_recognition.load_image_file(known_image)
                known_face_encodings = face_recognition.face_encodings(known_face_image)
                
                if len(known_face_encodings) > 0:
                    match_results = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    if any(match_results):
                        detected_faces.append(known_name)
                        face_found = True
                        break
            
            if not face_found:
                detected_faces.append("Unknown Person")
        
        if detected_faces:
            name = ', '.join(detected_faces)
        else:
            name = "Unknown Person"
    else:
        name = None
    
    return render_template('result.html', name=name, image=image_path)

if __name__ == '__main__':
    app.run(debug=True)
