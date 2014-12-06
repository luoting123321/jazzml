
# The Flask app to run the music project.
from flask import Flask, render_template
app = Flask('musicapp')

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run()