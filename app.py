from flask import Flask, render_template, request
from encryption import encrypt
from decryption import decrypt

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def dashboard():
    result = ""
    message = ""
    key1 = ""
    key2 = ""
    operation = ""

    if request.method == "POST":
        message = request.form["message"]
        key1 = int(request.form["key1"])
        key2 = int(request.form["key2"])
        operation = request.form["operation"]

        if operation == "encrypt":
            result = encrypt(message, key1, key2)

        elif operation == "decrypt":
            result = decrypt(message, key1, key2)

    return render_template(
        "dashboard.html",
        result=result,
        message=message,
        key1=key1,
        key2=key2,
        operation=operation
    )

if __name__ == "__main__":
    app.run(debug=True)