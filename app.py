from flask import Flask

app = Flask(__name__)
app.route("/")
def hello_world():
  return "hell!!"

print(__name__)
if __name__ == "__main__":
  app.run (host='172.31.196.36',debug=True)
  print('__name__')