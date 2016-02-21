from flask import Flask
app = Flask(__name__)
from werkzeug import secure_filename
from flask import Flask, request, redirect, url_for
import os


UPLOAD_FOLDER = '/root/mhacks/web-stuff/uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return '''
    <!doctype html>
<html lang="en">
  <head>
    <style type="text/css">
    body {
    font-family: sans-serif;
    background-color: #eeeeee;
    }
    .logo {
    text-align: center;
    }
    .file-upload {
    background-color: #ffffff;
    width: 600px;
    margin: 0 auto;
    padding: 20px;
    }
    .file-upload-btn {
    width: 100%;
    margin: 0;
    color: #fff;
    background: #1FB264;
    border: none;
    padding: 10px;
    border-radius: 4px;
    border-bottom: 4px solid #15824B;
    transition: all .2s ease;
    outline: none;
    text-transform: uppercase;
    font-weight: 700;
    }
    .file-upload-btn:hover {
    background: #1AA059;
    color: #ffffff;
    transition: all .2s ease;
    cursor: pointer;
    }
    .file-upload-btn:active {
    border: 0;
    transition: all .2s ease;
    }
    .file-submit-btn {
    width: 100%;
    margin: 0;
    color: #fff;
    background: #1FB264;
    border: none;
    padding: 10px;
    border-radius: 4px;
    border-bottom: 4px solid #15824B;
    transition: all .2s ease;
    outline: none;
    text-transform: uppercase;
    font-weight: 700;
    }
    .submit-btn:hover {
    background: #1AA059;
    color: #ffffff;
    transition: all .2s ease;
    cursor: pointer;
    }
    .submit-btn:active {
    border: 0;
    transition: all .2s ease;
    }
    .file-upload-content {
    display: none;
    text-align: center;
    }
    .file-upload-input {
    position: absolute;
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    outline: none;
    opacity: 0;
    cursor: pointer;
    }
    .image-upload-wrap {
    margin-top: 20px;
    border: 4px dashed #1FB264;
    position: relative;
    }
    .image-dropping,
    .image-upload-wrap:hover {
    background-color: #1FB264;
    border: 4px dashed #ffffff;
    }
    .image-title-wrap {
    padding: 0 15px 15px 15px;
    color: #222;
    }
    .drag-text {
    text-align: center;

    }
    .drag-text h3 {
    font-weight: 100;
    text-transform: uppercase;
    color: #15824B;
    padding: 60px 0;
    }
    .file-upload-image {
    max-height: 200px;
    max-width: 200px;
    margin: auto;
    padding: 20px;
    }
    .remove-image {
    width: 200px;
    margin: 0;
    color: #fff;
    background: #cd4535;
    border: none;
    padding: 10px;
    border-radius: 4px;
    border-bottom: 4px solid #b02818;
    transition: all .2s ease;
    outline: none;
    text-transform: uppercase;
    font-weight: 700;
    }
    .remove-image:hover {
    background: #c13b2a;
    color: #ffffff;
    transition: all .2s ease;
    cursor: pointer;
    }
    .remove-image:active {
    border: 0;
    transition: all .2s ease;
    }
  </style>
  <link rel="stylesheet" type="text/css" href="/root/mhacks/web-stuff/mystyle.css">
  <script class="jsbin" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
  <script class = "upload">
  function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function(e) {
    $('.image-upload-wrap').hide();
    $('.file-upload-image').attr('src', e.target.result);
    $('.file-upload-content').show();
    $('.image-title').html(input.files[0].name);
    };
    reader.readAsDataURL(input.files[0]);
  } else {
      removeUpload();
  }
  }
  function removeUpload() {
    $('.file-upload-input').replaceWith($('.file-upload-input').clone());
    $('.file-upload-content').hide();
    $('.image-upload-wrap').show();
    }
    $('.image-upload-wrap').bind('dragover', function () {
      $('.image-upload-wrap').addClass('image-dropping');
    });
    $('.image-upload-wrap').bind('dragleave', function () {
    $('.image-upload-wrap').removeClass('image-dropping');
  });
  </script>
</head>
<body>
  <div class = "logo">
    <img src="https://raw.githubusercontent.com/clu-star/mhacks/master/logo/oncoBOT.png" style="width:600px;height:320px;">
  </div>
  <div class="file-upload">
    <form action="" method=post enctype=multipart/form-data>

  
      
    <button class="file-upload-btn" type="button" onclick="$('.file-upload-input').trigger( 'click' )">Add Image</button>
    <div class="image-upload-wrap">
      <input class="file-upload-input" type='file' onchange="readURL(this);" accept="image/*" />
      <div class="drag-text">
        <h3>Drag and drop a file or select add Image</h3>

      </div>
    </div>
    <div class="file-upload-content">
      <img class="file-upload-image" src="#" alt="your image" />
      <div class="image-title-wrap">
        <button type="button" onclick="removeUpload()" class="remove-image">Remove <span class="image-title">Uploaded Image</span></button>
          <input type = 'submit' value = Upload>
         </form>
      </div>
    </div>
  </div>
</body>
</html>
    '''

if __name__ == '__main__':
   app.run(host='0.0.0.0')
