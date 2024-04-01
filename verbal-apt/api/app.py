from flask import Flask, render_template, request, jsonify
from assistant import run
app = Flask(__name__)

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    #audio_blob = request.files['audio'].read()
    uploaded_file = request.files['audio']

    # Process the uploaded file (e.g., save it to disk, perform analysis, etc.)
    # Example: Save the file to disk
    uploaded_file.save('uploaded_audio.wav')
    # Process the audio data using your Python script
    # e.g., perform speech recognition, audio analysis, etc.

    return 'Audio uploaded successfully', 200

@app.route('/')
def index():
    return render_template('index.html')
 

@app.route('/', methods=['POST'])
def process():
    user_request = request.json
    bot_response = run(user_request)
    return bot_response #jsonify({'response': bot_response})

# @app.route('/')
# def hello_world():
#     conversation = True
#     while conversation == True:
#         inp = input("say something")
#         if inp == 'kill':
#             conversation = False
#             return "killed"
#         print("response", inp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
