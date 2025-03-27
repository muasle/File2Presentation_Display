import os
import time
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
IMAGE_FOLDER = 'C:\Users\sellis12\OneDrive - University Of Oregon\Pictures\Screenshots'

@app.route('/')
def index():
    images = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith('.png')]
    return render_template('index.html', images=images)

@app.route('/ ')