from flask import Flask, request
from db.functions import randomcode, create_note, read_note_by_code, update_note_by_code
from markdown import markdown
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/<code>', methods=['GET', 'POST', 'PUT'])
def page(code):
    if request.method == 'GET':
        code = code
        content = {
            "code": code,
            "note": read_note_by_code(code)   
        }
        return content
    
    if request.method == 'POST':
        code = code
        note = request.args.get('note')
        create_note(code, note)
        content = {
            "code": code,
            "note": note
        }
        return content
    
    if request.method == 'PUT':
        code = code
        note = request.args.get('note')
        update_note_by_code(code, note)
        content = {
            "code": code,
            "note": note
        }
        return content
    
@app.route('/randomcode', methods=['GET'])
def random_code():
    code = randomcode()
    content = {
        "code": code
    }
    return content

@app.route('/markdowntohtml', methods=['POST'])
def markdown_to_html():
    content = request.headers.get('message')
    html = markdown(content)
    content = {
        "message": html
    }
    return content

@app.route('/', methods=['GET'])
def index():
    return {'connect': "Success connection!"}