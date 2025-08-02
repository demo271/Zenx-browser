from flask import Flask, render_template, request
app = Flask(__name__)

@app.after_request
def set_security_headers(response):
    response.headers["Content-Security-Policy"] = "default-src 'self'; frame-src *;"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response

@app.route("/", methods=["GET", "POST"])
def home():
    url = request.form.get("url", "https://duckduckgo.com")
    return render_template("browser.html", url=url)

if __name__ == "__main__":
    app.run(debug=True)
