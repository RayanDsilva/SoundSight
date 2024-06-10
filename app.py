# from flask import Flask, render_template, request, send_from_directory
# import os
# from nltk.metrics import edit_distance

# app = Flask(__name__)

# def find_closest_match(user_input, sign_languages):
#     # Calculate the edit distance (Levenshtein distance) between user input and each sign language
#     distances = [(language, edit_distance(user_input, language)) for language in sign_languages]
#     # Sort the distances by the edit distance in ascending order
#     sorted_distances = sorted(distances, key=lambda x: x[1])
#     # Return the sign language with the smallest edit distance
#     return sorted_distances[0][0]

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         user_input = request.form['sentence'].lower()
#         words = user_input.split()
#         avatar_videos = []

#         # Dictionary mapping sign languages to file names
#         sign_language_files = {
#             "After": "After.mp4",
#             "Again": "Again.mp4",
#             "D":"D.mp4",
#             "J":"J.mp4",
#             # Add more sign languages and their corresponding file names as needed
#         }

#         for word in words:
#             if word in sign_language_files:
#                 avatar_videos.append(f'{word}.mp4')
#             else:
#                 closest_match = find_closest_match(word, sign_language_files.keys())
#                 avatar_videos.append(f'{closest_match}.mp4')

#         return render_template('index.html', avatar_videos=avatar_videos)
#     return render_template('index.html', avatar_videos=None)

# @app.route('/videos/<path:filename>')
# def download_file(filename):
#     return send_from_directory('C:\\Users\\91735\\OneDrive\\Desktop\\audio to sign\\firsttry\\static\\assets', filename, as_attachment=False)

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, send_from_directory
# import os
# import speech_recognition as sr
# from nltk.metrics import edit_distance

# app = Flask(__name__)

# def find_closest_match(user_input, sign_languages):
#     # Calculate the edit distance (Levenshtein distance) between user input and each sign language
#     distances = [(language, edit_distance(user_input, language)) for language in sign_languages]
#     # Sort the distances by the edit distance in ascending order
#     sorted_distances = sorted(distances, key=lambda x: x[1])
#     # Return the sign language with the smallest edit distance
#     return sorted_distances[0][0]

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         if 'audio' in request.files:
#             # Handle audio input
#             audio_file = request.files['audio']
#             recognizer = sr.Recognizer()
#             with sr.AudioFile(audio_file) as source:
#                 audio_data = recognizer.record(source)
#             try:
#                 user_input = recognizer.recognize_google(audio_data)
#             except sr.UnknownValueError:
#                 user_input = ""  # If speech cannot be recognized, set user_input to an empty string
#         else:
#             # Handle text input
#             user_input = request.form['sentence'].lower()

#         words = user_input.split()
#         avatar_videos = []

#         # Dictionary mapping sign languages to file names
#         sign_language_files = {
#             "0":"0.mp4",
#             "1":"1.mp4",
#             "2":"2.mp4",
#             "3":"3.mp4",
#             "4":"4.mp4",
#             "5":"5.mp4",
#             "6":"6.mp4",
#             "7":"7.mp4",
#             "8":"8.mp4",
#             "9":"9.mp4",
#             "A":"A.mp4",
#             "After":"After.mp4",
#             "Again":"Again.mp4",
#             "Against":"Against.mp4",
#             "Age":"Age.mp4",
#             "All":"All.mp4",
#             "Alone":"ALone.mp4",
#             "Also":"Also.mp4",
#             "And":"And.mp4",
#             "Ask":"Ask.mp4",
#             "At":"At.mp4",
#             "B":"B.mp4",
#             "Be":"Be.mp4",
#             "Beautiful":"Beautiful.mp4",
#             "Before":"Before.mp4",
#             "Best":"Best.mp4",
#             "Better":"Better.mp4",
#             "Busy":"Busy.mp4",
#             "But":"But.mp4",
#             "Bye":"bye.mp4",
#             "C":"C.mp4",
#             "Can":"Can.mp4",
#             "Cannot":"Cannot.mp4",
#             "Change":"Change.mp4",
#             "College":"College.mp4",
#             "Come":"Come.mp4",
#             "Computer":"Computer.mp4",
#             "D":"D.mp4",
#             "Day":"Day.mp4",
#             "deaf":"deaf.mp4",
#             "Distance":"Distance.mp4",
#             "Do":"Do.mp4",
#             "Do Not":"Do Not.mp4",
#             "Does Not":"Does Not.mp4",
#             "E":"E.mp4",
#             "Eat":"Eat.mp4",
#             "Engineer":"Engineer.mp4",
#             "F":"F.mp4",
#             "Fight":"Fight.mp3",
#             "Finish":"Finish.mp3",
#             "From":"From.mp4",
#             "G":"G.mp4",
#             "Glitter":"Glitter.mp4",
#             "Go":"Go.mp4",
#             "God":"God.mp4",
#             "Gold":"Gold.mp4",
#             "Good":"Good.mp4",
#             "Great":"Great.mp4",
#             "H":"H.mp4",
#             "Hand":"Hand.mp4",
#             "Hands":"Hands.mp4",
#             "Happy":"Happy.mp4",
#             "Hello":"Hello.mp4",
#             "Help":"Help.mp4",
#             "Her":"Her.mp4",
#             "Here":"Here.mp4",
#             "His":"His.mp4",
#             "Home":"Home.mp4",
#             "Homepage":"Homepage.mp4",
#             "How":"How.mp4",
#             "I":"I.mp4",
#             "Invent":"Invent.mp4",
#             "It":"It.mp4",
#             "J":"J.mp4",
#             "K":"K.mp4",
#             "Keep":"Keep.mp4",
#             "L":"L.mp4",
#             "Language":"Language.mp4",
#             "Laugh":"Laugh.mp4",
#             "Learn":"Learn.mp4",
#             "M":"M.mp4",
#             "Me":"ME.mp4",
#             "More":"More.mp4",
#             "My":"My.mp4",
#             "N":"N.mp4",
#             "Name":"Name.mp4",
#             "Next":"Next.mp4",
#             "Not":"Not.mp4",
#             "Now":"Now.mp4",
#             "O":"O.mp4",
#             "Of":"Of.mp4",
#             "On":"On.mp4",
#             "Our":"Our.mp4",
#             "Out":"Out.mp4",
#             "P":"P.mp4",
#             "Pretty":"Pretty.mp4",
#             "Q":"Q.mp4",
#             "R":"R.mp4",
#             "Right":"Right.mp4",
#             "S":"S.mp4",
#             "Sad":"Sad.mp4",
#             "Safe":"Safe.mp4",
#             "See":"See.mp4",
#             "Self":"Self.mp4",
#             "Sign":"Sign.mp4",
#             "Sing":"Sing.mp4",
#             "So":"So.mp4",
#             "Sound":"Sound.mp4",
#             "Stay":"Stay.mp4",
#             "Study":"Study.mp4",
#             "T":"T.mp4",
#             "Talk":"Talk.mp4",
#             "Television":"Television.mp4",
#             "Thank":"Thank.mp4",
#             "Thank You":"Thank You.mp4",
#             "That":"That.mp4",
#             "They":"They.mp4",
#             "This":"This.mp4",
#             "Those":"Those.mp4",
#             "Time":"Time.mp4",
#             "To":"to.mp4",
#             "Type":"Type.mp4",
#             "U":"U.mp4",
#             "Us":"Us.mp4",
#             "V":"V.mp4",
#             "W":"W.mp4",
#             "Walk":"Walk.mp4",
#             "Wash":"wash.mp4",
#             "Way":"Way.mp4",
#             "We":"We.mp4",
#             "Welcome":"Welcome.mp4",
#             "What":"What.mp4",
#             "When":"when.mp4",
#             "Where":"Where.mp4",
#             "Which":"Which.mp4",
#             "Who":"Who.mp4",
#             "Whole":"Whole.mp4",
#             "Whose":"Whose.mp4",
#             "Why":"Why.mp4",
#             "Will":"Will.mp4",
#             "With":"With.mp4",
#             "Without":"Without.mp4",
#             "Words":"Words.mp4",
#             "Work":"Work.mp4",
#             "World":"World.mp4",
#             "Wrong":"Wrong.mp4",
#             "X":"X.mp4",
#             "Y":"Y.mp4",
#             "You":"You.mp4",
#             "Your":"Your.mp4",
#             "Yourself":"Yourself.mp4",
#             "Z":"Z.mp4"
#         }

#         for word in words:
#             if word in sign_language_files:
#                 avatar_videos.append(f'{word}.mp4')
#             else:
#                 closest_match = find_closest_match(word, sign_language_files.keys())
#                 print(closest_match)
#                 avatar_videos.append(f'{closest_match}.mp4')

#         return render_template('index.html', avatar_videos=avatar_videos)
#     return render_template('index.html', avatar_videos=None)

# @app.route('/videos/<path:filename>')
# def download_file(filename):
#     return send_from_directory('C:\\Users\\91735\\OneDrive\\Desktop\\audio to sign\\firsttry\\static\\assets', filename, as_attachment=False)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, send_from_directory,Response,jsonify
import os
import speech_recognition as sr
from nltk.metrics import edit_distance
import cv2
from ultralytics import YOLO
import pyttsx3
import time
import base64
import numpy as np



app = Flask(__name__)
# Initialize YOLOv8 model
model = YOLO("yolov8x.pt")
# Initialize camera
cap = cv2.VideoCapture(0)
w, h = 300, 300
def gen_frames():  
    while True:
        _, img = cap.read()
        # Perform prediction
        results = model.predict(img, conf=0.7)
        for r in results:
            boxes = r.boxes
            for box in boxes:
            # Extract box coordinates
                x1, y1, x2, y2 = box.xyxy[0]
                center_x = int((x1 + x2) / 2)
                center_y = int((y1 + y2) / 2)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                position = ""
                if center_y < img.shape[0] // 3:
                    position += "top "
                elif center_y > img.shape[0] * 2 // 3:
                    position += "bottom "
                else:
                    position += "middle "
                if center_x < img.shape[1] // 3:
                    position += "left "
                elif center_x > img.shape[1] * 2 // 3:
                    position += "right "
                position += model.names[int(box.cls)]
                print("I see", position)
                engine = pyttsx3.init()
                engine.say("I see" + position)
                engine.runAndWait()
                 # Convert frame to JPEG format
        ret, buffer = cv2.imencode('.jpg', img)
        time.sleep(3)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 



def find_closest_match(user_input, sign_languages):

    #Calculate the edit distance (Levenshtein distance) between user input and each sign language
    distances = [(language, edit_distance(user_input, language)) for language in sign_languages]
    # Sort the distances by the edit distance in ascending order
    sorted_distances = sorted(distances, key=lambda x: x[1])
    # Return the sign language with the smallest edit distance
    return sorted_distances[0][0]

@app.route('/')
def index():
    return render_template('soundsight.html')  

@app.route('/stop')
def speech():
    cap.release()
    return render_template('object.html')

@app.route('/open_object')
def object():
    global cap
    cap = cv2.VideoCapture(0)
    return render_template('object.html') 

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/open_audio', methods=['GET', 'POST'])
def open_audio():
    if request.method == 'POST':
        if 'audio' in request.files:
            # Handle audio input
            audio_file = request.files['audio']
            recognizer = sr.Recognizer()
            with sr.AudioFile(audio_file) as source:
                audio_data = recognizer.record(source)
            try:
                user_input = recognizer.recognize_google(audio_data)
            except sr.UnknownValueError:
                user_input = ""  # If speech cannot be recognized, set user_input to an empty string
        else:
            # Handle text input
            user_input = request.form['sentence'].lower()

            print("User:",user_input)

        words = user_input.split()

        print("split:",words)

        avatar_videos = []

        # Dictionary mapping sign languages to file names
        sign_language_files = {
            "0":"0.mp4",
            "1":"1.mp4",
            "2":"2.mp4",
            "3":"3.mp4",
            "4":"4.mp4",
            "5":"5.mp4",
            "6":"6.mp4",
            "7":"7.mp4",
            "8":"8.mp4",
            "9":"9.mp4",
            "a":"A.mp4",
            "After":"After.mp4",
            "Again":"Again.mp4",
            "Against":"Against.mp4",
            "Age":"Age.mp4",
            "All":"All.mp4",
            "Alone":"ALone.mp4",
            "Also":"Also.mp4",
            "And":"And.mp4",
            "Ask":"Ask.mp4",
            "At":"At.mp4",
            "b":"B.mp4",
            "Be":"Be.mp4",
            "Beautiful":"Beautiful.mp4",
            "Before":"Before.mp4",
            "Best":"Best.mp4",
            "Better":"Better.mp4",
            "Busy":"Busy.mp4",
            "But":"But.mp4",
            "Bye":"bye.mp4",
            "c":"C.mp4",
            "Can":"Can.mp4",
            "Cannot":"Cannot.mp4",
            "Change":"Change.mp4",
            "College":"College.mp4",
            "Come":"Come.mp4",
            "Computer":"Computer.mp4",
            "d":"D.mp4",
            "Day":"Day.mp4",
            "deaf":"deaf.mp4",
            "Distance":"Distance.mp4",
            "Do":"Do.mp4",
            "Do Not":"Do Not.mp4",
            "Does Not":"Does Not.mp4",
            "e":"E.mp4",
            "Eat":"Eat.mp4",
            "Engineer":"Engineer.mp4",
            "f":"F.mp4",
            "Fight":"Fight.mp3",
            "Finish":"Finish.mp3",
            "From":"From.mp4",
            "g":"G.mp4",
            "Glitter":"Glitter.mp4",
            "Go":"Go.mp4",
            "God":"God.mp4",
            "Gold":"Gold.mp4",
            "Good":"Good.mp4",
            "Great":"Great.mp4",
            "h":"H.mp4",
            "Hand":"Hand.mp4",
            "Hands":"Hands.mp4",
            "Happy":"Happy.mp4",
            "Hello":"Hello.mp4",
            "Help":"Help.mp4",
            "Her":"Her.mp4",
            "Here":"Here.mp4",
            "His":"His.mp4",
            "Home":"Home.mp4",
            "Homepage":"Homepage.mp4",
            "How":"How.mp4",
            "i":"I.mp4",
            "Invent":"Invent.mp4",
            "It":"It.mp4",
            "india":"india.mp4",
            "j":"J.mp4",
            "k":"K.mp4",
            "Keep":"Keep.mp4",
            "l":"L.mp4",
            "Language":"Language.mp4",
            "Laugh":"Laugh.mp4",
            "Learn":"Learn.mp4",
            "m":"M.mp4",
            "Me":"ME.mp4",
            "More":"More.mp4",
            "my":"My.mp4",
            "n":"N.mp4",
            "Name":"Name.mp4",
            "Next":"Next.mp4",
            "Not":"Not.mp4",
            "Now":"Now.mp4",
            "o":"O.mp4",
            "Of":"Of.mp4",
            "On":"On.mp4",
            "Our":"Our.mp4",
            "Out":"Out.mp4",
            "p":"P.mp4",
            "Pretty":"Pretty.mp4",
            "q":"Q.mp4",
            "r":"R.mp4",
            "Right":"Right.mp4",
            "s":"S.mp4",
            "Sad":"Sad.mp4",
            "Safe":"Safe.mp4",
            "See":"See.mp4",
            "Self":"Self.mp4",
            "Sign":"Sign.mp4",
            "Sing":"Sing.mp4",
            "So":"So.mp4",
            "Sound":"Sound.mp4",
            "Stay":"Stay.mp4",
            "Study":"Study.mp4",
            "t":"T.mp4",
            "Talk":"Talk.mp4",
            "Television":"Television.mp4",
            "Thank":"Thank.mp4",
            "Thank You":"Thank You.mp4",
            "That":"That.mp4",
            "They":"They.mp4",
            "This":"This.mp4",
            "Those":"Those.mp4",
            "Time":"Time.mp4",
            "To":"to.mp4",
            "Type":"Type.mp4",
            "U":"U.mp4",
            "Us":"Us.mp4",
            "v":"V.mp4",
            "w":"W.mp4",
            "Walk":"Walk.mp4",
            "Wash":"wash.mp4",
            "Way":"Way.mp4",
            "We":"We.mp4",
            "Welcome":"Welcome.mp4",
            "what":"What.mp4",
            "When":"when.mp4",
            "Where":"Where.mp4",
            "Which":"Which.mp4",
            "Who":"Who.mp4",
            "Whole":"Whole.mp4",
            "Whose":"Whose.mp4",
            "Why":"Why.mp4",
            "Will":"Will.mp4",
            "With":"With.mp4",
            "Without":"Without.mp4",
            "Words":"Words.mp4",
            "Work":"Work.mp4",
            "World":"World.mp4",
            "Wrong":"Wrong.mp4",
            "x":"X.mp4",
            "y":"Y.mp4",
            "You":"You.mp4",
            "Your":"Your.mp4",
            "Yourself":"Yourself.mp4",
            "z":"Z.mp4",
            "thin":"thin.mp4",
            "weak":"weak.mp4",
            "women":"women.mp4",
            "wrong":"wrong.mp4",
            "yes":"yes.mp4",
            "you":"you.mp4",
            "namaste":"namaste.mp4",
            "sign":"sign.mp4",
            "sorry":"sorry.mp4",
            "teacher":"teacher.mp4",
            "fine":"fine.mp4",
            "language":"language.mp4",
            "man":"man.mp4",
            "no":"no.mp4",
            "please":"please.mp4",
            "deaf":"deaf.mp4",
            "he":"he.mp4",
            "correct":"correct.mp4",
            "bad":"bad.mp4"

            # Add more sign language mappings here
        }

        # for word in words:
        for word in words:
            if word in sign_language_files:
                avatar_videos.append(f'{word}.mp4')
                print(word)
            else:
                # closest_match=list(word)
                closest_match = find_closest_match(word, sign_language_files.keys())
                print(closest_match)
                avatar_videos.append(f'{closest_match}.mp4')

        return render_template('index.html', avatar_videos=avatar_videos)
    return render_template('index.html', avatar_videos=None)

@app.route('/videos/<path:filename>')
def download_file(filename):
    return send_from_directory(r'C:\Users\lenovo\Desktop\SoundSight\static\assets', filename, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
