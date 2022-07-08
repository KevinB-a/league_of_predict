from flask import (Blueprint, render_template, request, redirect, flash, Flask, url_for)
from werkzeug.utils import secure_filename
from flapp.auth import login_required
import os
import joblib


bp = Blueprint('web_page', __name__)

UPLOAD_FOLDER = '/home/apprenant/simplon_project/league_of_predicts/App_Flask/flapp/static/uploads'

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route('/')
@login_required
def index():
    return render_template('web_page/index.html')

@bp.route('/', methods=['GET', 'POST'])
def upload_image():
    timeline = request.form.get('timeline')
    blue_destr_tower = request.form.get('blue_destr_tower')
    blue_gold = request.form.get('bluegold')
    red_destr_tower = request.form.get('red_destr_tower')
    red_gold = request.form.get('redgold')
    k_d_a_1 = request.form.get('k/d/a1')
    k_d_a_2 = request.form.get('k/d/a2')
    k_d_a_3 = request.form.get('k/d/a3')
    k_d_a_4 = request.form.get('k/d/a4')
    k_d_a_5 = request.form.get('k/d/a5')
    k_d_a_6 = request.form.get('k/d/a6')
    k_d_a_7 = request.form.get('k/d/a7')
    k_d_a_8 = request.form.get('k/d/a8')
    k_d_a_9 = request.form.get('k/d/a9')
    k_d_a_10 = request.form.get('k/d/a10')
    if k_d_a_1 != None and k_d_a_2 != None and k_d_a_3 != None and k_d_a_4 != None and k_d_a_5 != None and k_d_a_6 != None and k_d_a_7 != None and k_d_a_8 != None and k_d_a_9 != None and k_d_a_10 != None: 
        
        time = timeline.replace(':', ' ').split()
        timeline = time[0]
        print(timeline)

        blue_1 = k_d_a_1.replace('/', ' ').split()
        kill_1 = blue_1[0]
        death_1 = blue_1[1]
        assist_1 = blue_1[2]
        print('kill_1', kill_1, 'death_1', death_1, 'assist_1', assist_1)

        blue_2 = k_d_a_2.replace('/', ' ').split()
        kill_2 = blue_2[0]
        death_2 = blue_2[1]
        assist_2 = blue_2[2]
        print('kill_2', kill_2, 'death_2', death_2, 'assist_2', assist_2)

        blue_3 = k_d_a_3.replace('/', ' ').split()
        kill_3 = blue_3[0]
        death_3 = blue_3[1]
        assist_3 = blue_3[2]
        print('kill_3', kill_3, 'death_3', death_3, 'assist_3', assist_3)

        blue_4 = k_d_a_4.replace('/', ' ').split()
        kill_4 = blue_4[0]
        death_4 = blue_4[1]
        assist_4 = blue_4[2]
        print('kill_4', kill_4, 'death_4', death_4, 'assist_4', assist_4)

        blue_5 = k_d_a_5.replace('/', ' ').split()
        kill_5 = blue_1[0]
        death_5 = blue_1[1]
        assist_5 = blue_1[2]
        print('kill_5', kill_5, 'death_5', death_5, 'assist_5', assist_5)

        red_1 = k_d_a_6.replace('/', ' ').split()
        kill_6 = red_1[0]
        death_6 = red_1[1]
        assist_6 = red_1[2]
        print('kill_6', kill_6, 'death_6', death_6, 'assist_6', assist_6)

        red_2 = k_d_a_7.replace('/', ' ').split()
        kill_7 = red_2[0]
        death_7 = red_2[1]
        assist_7 = red_2[2]
        print('kill_7', kill_7, 'death_7', death_7, 'assist_7', assist_7)

        red_3 = k_d_a_8.replace('/', ' ').split()
        kill_8 = red_3[0]
        death_8 = red_3[1]
        assist_8 = red_3[2]
        print('kill_8', kill_8, 'death_8', death_8, 'assist_8', assist_8)

        red_4 = k_d_a_9.replace('/', ' ').split()
        kill_9 = red_4[0]
        death_9 = red_4[1]
        assist_9 = red_4[2]
        print('kill_9', kill_9, 'death_9', death_9, 'assist_9', assist_9)

        red_5 = k_d_a_10.replace('/', ' ').split()
        kill_10 = red_5[0]
        death_10 = red_5[1]
        assist_10 = red_5[2]
        print('kill_10', kill_10, 'death_10', death_10, 'assist_10', assist_10)
           
        list_of_variable = [int(timeline), int(blue_destr_tower), int(red_destr_tower), int(blue_gold), int(red_gold), int(kill_1), int(death_1), int(assist_1), int(kill_2), int(death_2), int(assist_2), int(kill_3), int(death_3), int(assist_3), int(kill_4), int(death_4), int(assist_4), int(kill_5), int(death_5), int(assist_5),
        int(kill_6), int(death_6), int(assist_6), int(kill_7), int(death_7), int(assist_7), int(kill_8), int(death_8), int(assist_8), int(kill_9), int(death_9), int(assist_9), int(kill_10), int(death_10), int(assist_10)]
        filepred = "/home/apprenant/simplon_project/league_of_predicts/App_Flask/flapp/xgboost"
        classifier = joblib.load(open(filepred, 'rb'))
        predictions = classifier.predict([list_of_variable])
        predictions_proba = classifier.predict_proba([list_of_variable])

        print(predictions)
        print(predictions_proba)
        labels = ["Lose","Win"]
        data = {
        'Blue Win' : {
            'Probabilities' : predictions_proba[0][1]
        },
        'Blue lose' : {
            'Probabilities' : predictions_proba[0][0]
        },
        'Prediction' : labels[predictions[0]]

               }
        print(data)


    
    print('timeline : ', timeline, 'blue_destr_tower :', blue_destr_tower, 'blue gold : ', blue_gold, 'red_destr_tower :', red_destr_tower, 'red gold: ', red_gold, 'kda1: ', k_d_a_1, 'kda2:', k_d_a_2, 'kda3: ', k_d_a_3, 'kda4: ', k_d_a_4, 'kda5: ', k_d_a_5, 'kda6: ', k_d_a_6, 'kda7: ', k_d_a_7, 'kda8: ', k_d_a_8, 'kda9: ', k_d_a_9, 'kda10: ', k_d_a_10) 


    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename('image.png')
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('web_page/index.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)

    return redirect('web_page/index.html')
 
@app.route('/display/<filename>')
def display_image():
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/image.png'))





            