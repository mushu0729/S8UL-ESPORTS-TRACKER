# 🎮 S8UL Esports Tracker  

## 📌 Project Overview  
The **S8UL Esports System** is a web-based platform designed to bring fans, players, and sponsors under one hub.  
It highlights the organization’s achievements, teams, tournaments, and creators while also providing analytics through APIs.  

Key Features:  
- Real-time **YouTube API** integration for creator stats (subscribers, views, videos).  
- Responsive web design with **Flask + Bootstrap**.  
- Admin panel for managing teams and tournaments.  
- Community engagement via suggestions and highlights.  
- Sponsor-focused analytics dashboards.  

---

## 🏗️ System Architecture  
- **Frontend**:  
  - HTML5, CSS3, Bootstrap 5  
  - JavaScript (dynamic UI)  
- **Backend**:  
  - Flask (Python)  
  - MySQL (SQLAlchemy ORM)  
  - REST API integrations (YouTube API, extendable)  
- **Authentication**:  
  - Flask-Login for admin  
  - Password hashing with Werkzeug  

---

## ⚙️ Installation & Setup  

### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/s8ul-esports-system.git
cd s8ul-esports-system
```

### 2. Create Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4. Database Setup (MySQL)  
- Create a database named `new`:  
```sql
CREATE DATABASE new;
```
- Update credentials in `main.py`:  
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/new'
```

### 5. Run the Server  
```bash
python main.py
```
Now open [http://127.0.0.1:5000](http://127.0.0.1:5000) 🎉  

---

## 📂 Project Structure  

```
S8UL-Esports-Tracker/
│── main.py                 # Flask app entry point
│── templates/              # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── creator.html
│   ├── tournaments.html
│── static/                 # Static files (CSS, JS, images, videos)
│── requirements.txt        # Dependencies
│── README.md               # Project documentation
```

---

## 📦 Requirements  

Create a `requirements.txt` file with:  

```
Flask==2.3.2
Flask-SQLAlchemy==3.0.5
Flask-Login==0.6.3
Werkzeug==2.3.7
requests==2.31.0
beautifulsoup4==4.12.2
mysqlclient==2.1.1

# Optional for development
Flask-Migrate==4.0.5
python-dotenv==1.0.0
```

Install via:  
```bash
pip install -r requirements.txt
```

---

## 🚀 Features  
✅ Centralized esports hub  
✅ Teams & player profiles (BGMI, Valorant)  
✅ Tournament updates & results  
✅ YouTube API-powered creator analytics  
✅ Community suggestions & feedback  
✅ Sponsor dashboards with digital reach data  
✅ Secure admin panel  

---

## 🔮 Future Enhancements  
- Live streaming support (WebRTC/RTMP).  
- OAuth login for fans (Google, Discord).  
- Expanded API support (Twitch, Instagram).  
- PWA version for mobile users.  
- E-commerce (merchandise & tickets).  


---
