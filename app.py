from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from Bio import SeqIO  # Import Biopython to parse FASTA files
import random

app = Flask(__name__)

# Path to your allergen database
allergen_db_path = "C:/Users/priya/OneDrive/Desktop/Database_Allergenonline.fasta"

# Folder to store uploaded files
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'fasta', 'fa'}

# Check if the file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Upload route
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        # Process the FASTA file here
        results = process_fasta(file_path)
        return render_template('results.html', results=results)
    return jsonify({'error': 'Invalid file type'}), 400

def process_fasta(file_path):
    results = []
    with open(file_path, 'r') as file:
        # Parse all sequences in the uploaded FASTA file
        for record in SeqIO.parse(file, "fasta"):
            # Extract necessary information from each sequence (example values below)
            name = record.id
            sequence = str(record.seq)
            
            # For demonstration, we are using mock values, replace with actual analysis
            molecular_weight = len(sequence) * 110  # Example, calculate based on sequence length
            hydrophobicity = random.uniform(-1.0, 1.0)  # Random value for demonstration
            tanimoto_coefficient = random.uniform(0.5, 1.0)  # Random value for demonstration
            antigenicity_score = random.uniform(0.5, 1.0)  # Random value for demonstration
            ige_binding_score = random.uniform(0.5, 1.0)  # Random value for demonstration
            
            # Append the result for each sequence
            results.append({
                'name': name,
                'molecular_weight': molecular_weight,
                'hydrophobicity': hydrophobicity,
                'tanimoto_coefficient': tanimoto_coefficient,
                'antigenicity_score': antigenicity_score,
                'ige_binding_score': ige_binding_score
            })
    
    return results

if __name__ == '__main__':
    app.run(debug=True)
