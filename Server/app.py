import cv2 as cv
from flask import Flask, Response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/picture', methods=['GET'])

def picture():
    cam = cv.VideoCapture(0)

    if not cam.isOpened():
        return jsonify({'error': 'Could not open webcam'}), 500

    ret, frame = cam.read()
    cam.release()

    if not ret:
        return jsonify({'error': 'Failed to capture image'}), 500

    ret, buffer = cv.imencode('.jpg', frame)

    if not ret:
        return jsonify({'error': 'Failed to encode image'}), 500

    return Response(buffer.tobytes(), mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)