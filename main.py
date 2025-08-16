from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_required, LoginManager, UserMixin, current_user, login_user
import os
from flask import jsonify
import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime

local_server= True
app = Flask(__name__)
app.secret_key='EMS'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Admin, int(user_id))

app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return filename  # Return the filename only
    return None



app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/new'
db=SQLAlchemy(app)

# Database model for Admin
class Admin(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Bgmi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    youtube = db.Column(db.String(200))
    instagram = db.Column(db.String(200))
    twitter = db.Column(db.String(200))

class Valorant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    youtube_url = db.Column(db.String(200), nullable=True)
    instagram_url = db.Column(db.String(200), nullable=True)
    twitter_url = db.Column(db.String(200), nullable=True)

class Suggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    twitter_username = db.Column(db.String(100), nullable=True)  # Optional field
    suggestion = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


def __repr__(self):
        return f"<Suggestion {self.name}>"

# Routes
@app.route('/')
def base():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/video.html')
def video():
    channel_id = request.args.get('channelId')
    return render_template('video.html', channel_id=channel_id)

@app.route('/allvideo')
def allvideo():
    return render_template('allvideos.html')

@app.route('/creator')
def creator():
    return render_template('creator.html')



@app.route('/valo')
def valo():
    valorant_team = Valorant.query.all()  # Fetch all Valorant team members from the database
    return render_template('valo.html', valorant_team=valorant_team)

@app.route('/add-valorant-member', methods=['GET', 'POST'])
@login_required
def add_valo_member():
    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
        image = request.files['image']
        youtube = request.form['youtube']
        instagram = request.form['instagram']
        twitter = request.form['twitter']
        if not image:
            flash('Please upload an image.', 'danger')
            return render_template('add_valo_member.html')

        image_filename = secure_filename(image.filename)
        try:
            image.save(f"static/{image_filename}")
        except Exception as e:
            flash('Error uploading image.', 'danger')
            return render_template('add_valo_member.html')

        new_valomember = Valorant(name=name, role=role, image_url=f"static/{image_filename}", youtube_url=youtube, instagram_url=instagram, twitter_url=twitter)
        try:
            db.session.add(new_valomember)
            db.session.commit()
            flash('New Valorant team member added successfully!', 'success')
            return redirect(url_for('valo'))
        except Exception as e:
            flash('Error adding Valorant team member.', 'danger')
            return render_template('add_valo_member.html')
    else:
        return render_template('add_valo_member.html')


@app.route('/edit_valo_member/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_valo_member(id):
    valomember = Valorant.query.get(id)
    if request.method == 'POST':
        valomember.name = request.form['name']
        valomember.role = request.form['role']
        image = request.files['image']
    
        if image:
            image_filename = secure_filename(image.filename)
            try:
                image.save(f"static/{image_filename}")
                valomember.image_url = f"static/{image_filename}"
            except Exception as e:
                flash('Error uploading image.', 'danger')
        valomember.youtube_url = request.form['youtube']
        valomember.instagram_url = request.form['instagram']
        valomember.twitter_url = request.form['twitter']
        db.session.commit()
        return redirect(url_for('valo'))
    return render_template('edit_valo_member.html', member=valomember)


@app.route('/delete_valo_member/<int:id>', methods=['POST'])
@login_required
def delete_valo_member(id):
    valomember = Valorant.query.get(id)
    db.session.delete(valomember)
    db.session.commit()
    return redirect(url_for('valo'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Admin.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            flash('Login successful!', 'success')
            next_url = request.args.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))
@app.route('/grant-access', methods=['GET', 'POST'])
def grant_access():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        existing_user = Admin.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose another one.', 'danger')
            return render_template('newuser.html')

        new_user = Admin(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('New user created and granted access!', 'success')
        return render_template('home.html')

    return render_template('newuser.html')


@app.route('/bgmi')
def bgmi():
    team_members = Bgmi.query.all()
    print(current_user.is_authenticated)  # Print if the user is authenticated
    print(current_user)  # Print details about the logged-in user
    return render_template('bgmi.html', team_members=team_members)


@app.route('/add-member', methods=['GET', 'POST'])
@login_required
def add_member():
    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
        image = request.files['image']
        youtube = request.form['youtube']
        instagram = request.form['instagram']
        twitter = request.form['twitter']

        # Check if image is uploaded
        if not image:
            flash('Please upload an image.', 'danger')
            return render_template('add_member.html')

        # Save image to a folder (ensure the folder exists)
        image_filename = secure_filename(image.filename)
        try:
            image.save(f"static/{image_filename}")
        except Exception as e:
            flash('Error uploading image.', 'danger')
            return render_template('add_member.html')

        # Add member to the database
        new_member = Bgmi(name=name, role=role, image=f"static/{image_filename}", youtube=youtube, instagram=instagram, twitter=twitter)
        try:
            db.session.add(new_member)
            db.session.commit()
            flash('New team member added successfully!', 'success')
            return redirect(url_for('bgmi'))
        except Exception as e:
            flash('Error adding team member.', 'danger')
            return render_template('add_member.html')
    else:
        return render_template('add_member.html')
    


@app.route('/edit_member/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_member(id):
    member = Bgmi.query.get(id)
    if request.method == 'POST':
        member.name = request.form['name']
        member.role = request.form['role']
        image = request.files['image']
        if image:
            image_filename = secure_filename(image.filename)
            try:
                image.save(f"static/{image_filename}")
                member.image = f"static/{image_filename}"
            except Exception as e:
                flash('Error uploading image.', 'danger')
        db.session.commit()
        return redirect(url_for('bgmi'))
    return render_template('edit_member.html', member=member)

@app.route('/delete_member/<int:id>', methods=['POST'])
@login_required
def delete_member(id):
    member = Bgmi.query.get(id)
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for('bgmi'))

@app.route('/allteams')
def allteams():
    return render_template('allteams.html')



def fetch_team_results():

    url = 'https://liquipedia.net/pubgmobile/api.php'
    params = {
        'action': 'parse',
        'page': 'Team_SouL/Results',
        'format': 'json',
        'prop': 'text',
    }

    headers = {
        'User-Agent': 'Esports management system for collage project /1.0 (http://localhost; example@example.com)',
        'Accept-Encoding': 'gzip'
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        return None  # Handle API error gracefully

    # Parse and process the results
    data = response.json()
    page_content = data['parse']['text']['*']
    soup = BeautifulSoup(page_content, 'html.parser')

    # Extract the results data
    results = []
    result_table = soup.find('table', {'class': 'wikitable'})

    if result_table:
        for row in result_table.find_all('tr')[1:]:
            cols = row.find_all('td')
            if len(cols) >= 5:
                result = {
                    'date': cols[0].text.strip(),
                    'placement': cols[1].text.strip(),
                    'tier': cols[2].text.strip(),
                    'tournament': cols[4].text.strip(),
                    'prize': cols[5].text.strip(),
                }
                results.append(result)

    return results

@app.route('/results')
def results():
    team_name = "Team SouL"  # Or fetch dynamically if needed
    results = fetch_team_results()
    
    if not results:
        results = []  # In case there are no results or an error
    
    return render_template('results.html', team_name=team_name, results=results)

def fetch_tournaments():
    url = 'https://liquipedia.net/pubgmobile/api.php'
    params = {
        'action': 'parse',
        'page': 'Team_SouL/Results',  # Make sure this is the correct page for tournaments
        'format': 'json',
        'prop': 'text',
    }

    headers = {
        'User-Agent': 'Esports management system for collage project /1.0 (http://localhost; example@example.com)',
        'Accept-Encoding': 'gzip'
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        return None  # Handle API error gracefully

    # Parse the response content
    data = response.json()
    page_content = data['parse']['text']['*']
    soup = BeautifulSoup(page_content, 'html.parser')

    # Extract the results data (date and tournament)
    results = []  # Make sure the variable is named results, not tournaments
    result_table = soup.find('table', {'class': 'wikitable'})

    if result_table:
        for row in result_table.find_all('tr')[1:]:
            cols = row.find_all('td')
            if len(cols) >= 5:
                tournament = {
                    'date': cols[0].text.strip(),
                    'tournament': cols[4].text.strip(),
                }
                results.append(tournament)

    return results

@app.route('/tournaments')
def tournaments():
    tournament_data = fetch_tournaments()
    if tournament_data:
        return render_template('tournaments.html', tournaments=tournament_data)
    else:
        return render_template('tournaments.html', tournaments=tournament_data)    
    
@app.route('/suggestion')
def suggestion():
    suggestion = Suggestion.query.all()  # Retrieve all suggestions from the database
    return render_template('suggestion.html', suggestion=suggestion)




@app.route("/add-suggestion", methods=["POST"])
def add_suggestion():
    name = request.form.get("user_name")
    twitter_username = request.form.get("twitter_username")
    suggestion = request.form.get("suggestion")


    if name and suggestion:
        new_suggestion = Suggestion(name=name, twitter_username=twitter_username, suggestion=suggestion)
        db.session.add(new_suggestion)
        db.session.commit()

    return redirect(url_for("suggestion"))

@app.route('/contributors')
def contributors():
    return render_template('contributors.html')


if __name__ == '__main__':
    app.run(debug=True)
