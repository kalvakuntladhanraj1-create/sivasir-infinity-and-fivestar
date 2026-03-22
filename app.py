from flask import Flask, request, send_file, render_template
from docxtpl import DocxTemplate
import os

app = Flask(__name__)

# Absolute base path (more reliable)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# ================= HEALTH CHECK =================
@app.route("/ping")
def ping():
    return "OK", 200


# ================= HOME =================
@app.route("/")
def home():
    return render_template("home.html")


# ================= SALE FORM =================
@app.route("/sale")
def sale_form():
    return render_template("sale.html")


# ================= GIFT FORM =================
@app.route("/gift")
def gift_form():
    return render_template("gift.html")


# ================= GENERATE SALE =================
@app.route("/generate_sale", methods=["POST"])
def generate_sale():
    try:
        data = request.form.to_dict()

        template_path = os.path.join(BASE_DIR, "templates_docx", "sale.docx")
        output_path = os.path.join("/tmp", "sale_report.docx")

        # DEBUG CHECK
        if not os.path.exists(template_path):
            return f"Template NOT FOUND: {template_path}", 500

        doc = DocxTemplate(template_path)
        doc.render(data)
        doc.save(output_path)

        return send_file(output_path, as_attachment=True)

    except Exception as e:
        return f"ERROR (SALE): {str(e)}", 500


# ================= GENERATE GIFT =================
@app.route("/generate_gift", methods=["POST"])
def generate_gift():
    try:
        data = request.form.to_dict()

        template_path = os.path.join(BASE_DIR, "templates_docx", "gift.docx")
        output_path = os.path.join("/tmp", "gift_report.docx")

        # DEBUG CHECK
        if not os.path.exists(template_path):
            return f"Template NOT FOUND: {template_path}", 500

        doc = DocxTemplate(template_path)
        doc.render(data)
        doc.save(output_path)

        return send_file(output_path, as_attachment=True)

    except Exception as e:
        return f"ERROR (GIFT): {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)
