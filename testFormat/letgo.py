from flask import Flask, request


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
  <body>
    <form action = "https://duckduckgo.com" method = "get">
      <label for = "first-name">First Name:</label>
      <input id = "first-name" type = "text" name = "first_name" />
      <input type = "submit" />
    </form>
  </body>
</html>
"""

@app.route("/")
def index():
    return form