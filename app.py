from flask import Flask, request, send_file
from docxtpl import DocxTemplate
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ================= HEALTH CHECK (CRITICAL FOR RENDER) =================
# UptimeRobot should monitor THIS route
@app.route("/ping")
def ping():
    return "OK", 200


# ================= HOME =================
@app.route("/")
def home():
    with open(os.path.join(BASE_DIR, "html", "home.html"), encoding="utf-8") as f:
        return f.read()


# ================= SALE FORM =================
@app.route("/sale")
def sale_form():
    with open(os.path.join(BASE_DIR, "html", "sale.html"), encoding="utf-8") as f:
        return f.read()


# ================= GIFT FORM =================
@app.route("/gift")
def gift_form():
    with open(os.path.join(BASE_DIR, "html", "gift.html"), encoding="utf-8") as f:
        return f.read()


# ================= GENERATE SALE =================
@app.route("/generate_sale", methods=["POST"])
def generate_sale():
    data = request.form.to_dict()

    template = os.path.join(BASE_DIR, "templates_docx", "sale.docx")
    output = "/tmp/sale_report.docx"

    doc = DocxTemplate(template)
    doc.render(data)
    doc.save(output)

    return send_file(output, as_attachment=True)


# ================= GENERATE GIFT =================
@app.route("/generate_gift", methods=["POST"])
def generate_gift():
    data = request.form.to_dict()

    template = os.path.join(BASE_DIR, "templates_docx", "gift.docx")
    output = "/tmp/gift_report.docx"

    doc = DocxTemplate(template)
    doc.render(data)
    doc.save(output)

    return send_file(output, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
