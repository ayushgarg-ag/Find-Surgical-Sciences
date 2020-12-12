from flask import Flask, render_template, request
from api import get_patients_list, readPrevIniFile, saveFileToPatient

app = Flask(__name__)
patient = ''

@app.route('/')
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        info = request.data.decode()
        saveFileToPatient(info, patient)
        return ""
    else:
        return render_template('form.html', patients=get_patients_list())

@app.route('/readFile', methods=['GET', 'POST'])
def readFile():
    global patient
    if request.method == 'POST':
        patient = request.data.decode()
        print(patient)
        return readPrevIniFile(patient)

if __name__ == "__main__":
    app.run(debug=True, port=4250)
