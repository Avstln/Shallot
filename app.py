#!/usr/bin/env python
import subprocess
from flask import Flask, request, render_template, send_from_directory, redirect, flash, jsonify
import os
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ZEEK_CONTAINER_NAME = 'zeek01'  # Name of your Zeek container

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('upload.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files' not in request.files:
        flash('No file part')
        return redirect(request.url)

    files = request.files.getlist('files')
    uploaded_files = []

    for file in files:
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if not file.filename.endswith('.pcap'):
            flash('Only .pcap files are allowed!')
            return redirect(request.url)

        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        unique_filename = f"{timestamp}_{file.filename}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
        uploaded_files.append(unique_filename)

    flash('File(s) successfully uploaded')
    return redirect('/')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify(success=True), 200
    return jsonify(success=False, error="File not found"), 404

@app.route('/analyze/<filename>', methods=['POST'])
def analyze_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        try:
            # Execute the Zeek analysis on the other container
            result = subprocess.run([
                'docker', 'exec', ZEEK_CONTAINER_NAME, 'zeek', '-Cr', 'LogAscii::use_json=T', f"/pcap/{filename}"
            ], capture_output=True, text=True)

            if result.returncode == 0:
                return jsonify(success=True, message=f"Analysis completed for {filename}"), 200
            else:
                return jsonify(success=False, error=f"Zeek analysis failed: {result.stderr}"), 500
        except Exception as e:
            return jsonify(success=False, error=str(e)), 500

    return jsonify(success=False, error="File not found"), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

