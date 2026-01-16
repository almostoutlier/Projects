from flask import Flask, render_template, request
import requests

app = Flask(__name__)
MCP_URL = "http://mcp_server:9000/infer"  # MCP routes to FastAPI

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        payload = {
            "sepal length (cm)": float(request.form["sepal_length"]),
            "sepal width (cm)": float(request.form["sepal_width"]),
            "petal length (cm)": float(request.form["petal_length"]),
            "petal width (cm)": float(request.form["petal_width"]),
        }
        try:
            response = requests.post(MCP_URL, json=payload)
            prediction = response.json()
        except Exception as e:
            prediction = {"error": str(e)}

    return render_template("form.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

