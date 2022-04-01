from flask import Flask, jsonify, request
from flask import Flask

app = Flask(__name__)

@app.route('/endpoint/bmi', methods=['POST'])
def bmi():
    berat = float(request.form.get('berat'))
    tinggi = float(request.form.get('tinggi'))
    BMI = berat/(tinggi/100)**2
    if BMI < 18.5:
        ket = "Kurus"
    elif BMI > 18.5 and BMI < 25:
        ket = "Normal"
    elif BMI > 25 and BMI < 40:
        ket = "Berlebih"
    else:
        ket = "Bahaya"
    data = {'ket': ket}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=False, port=8888)