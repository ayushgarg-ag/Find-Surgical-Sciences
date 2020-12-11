from flask import Flask, render_template, request

app = Flask(__name__)

# import glob
# # print(glob.glob("/home/adam/*.txt"))
# print(glob.glob("/Users/ayushgarg/COMPUTER SCIENCE/Find Surgical Sciences Work/FSS-ConfigWebForm/*.html"))

# import os

# # Getting the current work directory (cwd)
# thisdir = os.getcwd() + "/static"

# # r=root, d=directories, f = files
# for r, d, f in os.walk(thisdir):
#     for file in f:
#         print(os.path.join(r, file))


# @app.route('/')
# def index():
#     return render_template('home.html')


@app.route('/')
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        info = request.data.decode()
        f = open("./static/css/config.ini", "a")
        f.write(info)
        f.close()

        f = open("config.ini", "r")
        print(f.read())
        return
    else:
        return render_template('form.html')

    
# @app.route('/hello', methods=['POST'])
# def hello():
#     print("WHAT")
#     print(request)
#     print(request.method)

#     req = request.get_json()

#     print(req)

#     res = make_response(jsonify({"message": "OK"}), 200)

#     return res

    # if request.method == 'POST':
    #     print("ahfaushfaiuha")
    # return 'Hello, World'

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)
if __name__ == "__main__":
    app.run(debug=True, port=4250)


# import os
# from werkzeug.utils import secure_filename

# UPLOAD_FOLDER = '/Users/ayushgarg/COMPUTER SCIENCE/Find Surgical Sciences Work/FSS-ConfigWebForm/static/javascript'
# ALLOWED_EXTENSIONS = {'ini'}

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit an empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file',
#                                     filename=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)
