from flask  import  Flask, Response
from flask  import  render_template
from flask  import  request
from camera import Video

app  = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login_validation", methods=['POST'])
def login_validation():
     num= request.form.get('email')
     pas= request.form.get('password')

     if num == "xyz@gmail.com" and pas == "0000":

        return render_template('home.html')

     else:
        return render_template('index.html')

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')

@app.route('/video')

def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)