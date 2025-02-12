from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Status storage
detection_status = "Product Undetected!"

# Route to update status
@app.route('/update_status', methods=['POST'])
def update_status():
    global detection_status
    data = request.json
    detection_status = data.get("status", "Product Undetected!")
    return jsonify({"message": "Status updated successfully"})

# Homepage displaying status
@app.route('/')
def index():
    return render_template("index.html", status=detection_status)

if __name__ == '__main__':
    app.run(debug=True)