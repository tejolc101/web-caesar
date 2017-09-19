from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
        <!DOCTYPE html>
        <html>
             <head>
                <style>
                    form {
                        background-color: #eee;
                        padding: 20px;
                        margin: 0 auto;
                        width: 540px;
                        font: 16px sans-serif;
                        border-radius: 10px;
                    }
                    textarea {
                        margin: 10px 0;
                        width: 540px;
                        height: 120px;
                    }
                </style>
            </head>
            <body>
                <form action = "/encrypt" method = "post">
                    <label for="rotation">Rotate by:
                    <input type="text" id="rotation" value = 0 name="rot"/>
                    </label><br/>
                    <textarea name="text"></textarea><br/>
                    <input type="submit" value="Submit Query"/>
                </form>
            </body>
        </html>
    """

@app.route("/") 
def index():
    return form
@app.route("/encrypt", methods = ['POST'])
def encrypt():
    rotations = request.form['rot']
    rotations = int(rotations)
    text_area = request.form['text']
    result = rotate_string(text_area, rotations)
    
    return "<h1>" + result + "</h1>"

app.run()