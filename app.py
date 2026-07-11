from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_complaint():
    name = request.form.get('name')
    phone = request.form.get('phone')
    area = request.form.get('area')
    issue = request.form.get('issue')
    details = request.form.get('details')

    with open("complaints.txt", "a", encoding="utf-8") as f:
        f.write(f"नाम: {name} | फोन: {phone} | इलाका: {area} | समस्या: {issue} | विवरण: {details}\n")
        f.write("-" * 50 + "\n")

    msg = "आपकी शिकायत सफलतापूर्वक दर्ज कर ली गई है! जल्द ही कार्रवाई की जाएगी।"
    return render_template('index.html', success_msg=msg)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
