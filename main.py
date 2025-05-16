from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import send_from_directory
from color_extractor import get_dominant_colors
from werkzeug.utils import secure_filename
import os



app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Configuration
app.config['SECRET_KEY'] = 'secret_key'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Create the upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part', 'danger')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file', 'danger')
        return redirect(request.url)

    # Save file
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    return redirect(url_for('process_image', filename=filename))

@app.route('/process/<filename>')
def process_image(filename):
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    
    top_colors = get_dominant_colors(image_path, k=10)  
    
    return render_template('process.html', filename=filename, top_colors=top_colors)



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



if __name__ == '__main__':
    app.run(debug=True)