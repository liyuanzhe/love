from flask import Flask, render_template, request

app = Flask(__name__)
PROJ_NAME = u"AI图片裁剪示例"
PROJ_DESCRIPTION = u"AI多尺寸图片裁剪V1.0"

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route("/")
def index():
  return render_template("index.html", PROJ_NAME=PROJ_NAME, PROJ_DESCRIPTION=PROJ_DESCRIPTION)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
