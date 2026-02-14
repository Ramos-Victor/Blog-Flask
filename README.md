# 📝 Victor Blog

A simple blog project built with **Flask** and **SQLAlchemy**, allowing users to create, list, edit, and delete articles.

---

## 🚀 Technologies Used

- Python 3  
- Flask  
- Flask-SQLAlchemy  
- Flask-WTF  
- SQLite  
- HTML + Jinja2  

---

## 📌 Features

- ✅ List all articles on the homepage  
- ✅ Admin dashboard  
- ✅ Create new articles  
- ✅ Edit existing articles  
- ✅ Delete articles  
- ✅ Custom 404 error page  

---

## 📂 Project Structure

```
├── app.py
├── forms.py
├── artigos.db
├── templates/
│   ├── index.html
│   ├── artigo.html
│   ├── admin/
│   │   ├── dashboard.html
│   │   ├── new.html
│   │   └── edit.html
│   └── error/
│       └── 404.html
```

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install flask flask_sqlalchemy flask_wtf
```

### 4️⃣ Run the application

```bash
python app.py
```

The application will be available at:

```
http://127.0.0.1:5000
```

---

## 🧠 Database Model

```python
class Artigos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    conteudo = db.Column(db.String, nullable=False)
    publicado_em = db.Column(db.Date, nullable=False)
```

The database used is **SQLite**, automatically created as:

```
artigos.db
```

---

## 🔐 Security

- Uses `SECRET_KEY`
- CSRF protection via Flask-WTF
- `get_or_404()` to handle missing records safely

---

## 🌐 Main Routes

| Route | Description |
|-------|------------|
| `/` | Homepage with articles |
| `/admin_dashboard` | Admin panel |
| `/novo_artigo` | Create new article |
| `/artigo/<id>` | View article |
| `/artigo_update/<id>` | Edit article |
| `/artigo_delete/<id>` | Delete article |

---

## 🎯 Project Purpose

This project was built to:

- Practice CRUD operations with Flask  
- Work with Flask-WTF forms  
- Use SQLAlchemy ORM  
- Understand HTTP request flow (GET/POST)  

