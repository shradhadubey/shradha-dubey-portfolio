# AWS Data Engineering Portfolio

A dynamic, high-performance portfolio website for **Shradha Dubey**, a Big Data Engineer with 6+ years of experience. This project showcases a modern tech stack and is designed for seamless deployment on cloud platforms like Render or PythonAnywhere.
https://shradha-dubey-portfolio-jb1zy44fa-shradhadubeys-projects.vercel.app/

## System Design Patterns
In this portfolio and my featured projects, I implement the following Data Engineering principles:
- **Idempotency:** Ensuring pipelines can be re-run without duplicating data.
- **Data Quality:** Implementing automated checks (Great Expectations/Dequy) during the Bronze-to-Silver transition.
- **Scalability:** Leveraging distributed computing (Spark) for high-volume transformations.

### Tech Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-FDEE21?style=for-the-badge&logo=apachespark&logoColor=black)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=shradhadubey&theme=tokyonight)](https://git.io/streak-stats)

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

