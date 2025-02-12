from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

detections = []  # Store detections

@app.route('/')
def index():
    return render_template('index.html', detections=detections)

@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    if data and "color_detected" in data:
        detections.append(data["color_detected"])
        return jsonify({"status": "success", "message": "Detection received!"})
    return jsonify({"status": "error", "message": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
