from flask import Flask, render_template, request, redirect
from os.path import join, isfile
from os import listdir

app = Flask(__name__, static_folder='./resources/', static_url_path='/')

sharedFolder = join('.', 'resources', 'uploads')
sharedURL = '/uploads'

@app.route('/', methods=['GET'])
def get_index():
    filelist = []
    for file in listdir(sharedFolder):
        if isfile(join(sharedFolder, file)):
            filelist.append(f"{sharedURL}/{file}")
    print(filelist)
    return render_template("index.html", filelist=filelist)

@app.route('/upload', methods=['POST'])
def post_upload():
    file = request.files.get('upfile', None)
    try:
        if file == None:
            return "파일이 선택되지 않았습니다."
        file.save(join(sharedFolder, file.filename))
    except Exception as e:
        pass
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)