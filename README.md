# AWS Data Engineering Portfolio

A dynamic, high-performance portfolio website for **Shradha Dubey**, a Big Data Engineer with 6+ years of experience. This project showcases a modern tech stack and is designed for seamless deployment on cloud platforms like Render or PythonAnywhere.

## 🚀 Features

* **Dynamic Data Rendering**: Powered by a centralized `data.json` for easy updates without modifying code.
* **Modern Dark UI**: Features a "Glassmorphism" aesthetic with high-visibility neon accents for better readability.
* **Mobile Responsive**: Built using Bootstrap 5 to ensure a professional look on all devices.
* **Production Ready**: Configured for deployment with Gunicorn and absolute path handling.

## 🛠️ Tech Stack

* **Backend**: Python / Flask
* **Frontend**: HTML5, CSS3, Jinja2 Templates
* **Styling**: Bootstrap 5 + Custom Glassmorphism CSS
* **Deployment**: Render / Gunicorn

## 📂 Project Structure

```text
shradha-dubey-portfolio/

├── app.py              # Flask application logic
├── profile.json        # Keep your profile data here to keep app.py clean
├── vercel.json         # The bridge 
├── .gitignore          # Prevents venv and cache from being uploaded
├── static/             # Centralized resume data (Skills, Experience, etc.)
│   ├── css/
│   ├── js/
│   ├── images/
│   └── resume/
├── templates/          # Responsive Jinja2 template
|   └── index.html
├── requirements.txt
└── venv/               # Local virtual environment (ignored by git)

```

## ⚙️ Local Setup

1. **Clone the repository**:
```bash
git clone https://github.com/your-username/portfolio-repo.git
cd portfolio-repo

```


2. **Set up Virtual Environment**:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows: venv\Scripts\activate

```


3. **Install Dependencies**:
```bash
pip install -r requirements.txt

```


4. **Run Locally**:
```bash
python app.py

```


Visit `http://127.0.0.1:5000` in your browser.

## 🌐 Deployment

This project is configured for **Render**. To deploy:

1. Push your code to a GitHub repository.
2. Connect the repository to **Render.com**.
3. Use the following settings:
* **Build Command**: `pip install -r requirements.txt`
* **Start Command**: `gunicorn app:app`

