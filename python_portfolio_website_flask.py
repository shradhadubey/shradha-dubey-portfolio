from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Shradha Dubey | Data Engineer</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #2563eb;
      --dark: #0f172a;
      --light: #f8fafc;
      --muted: #64748b;
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      font-family: 'Inter', sans-serif;
      background: var(--light);
      color: var(--dark);
      line-height: 1.6;
    }

    nav {
      position: sticky;
      top: 0;
      background: white;
      border-bottom: 1px solid #e5e7eb;
      padding: 16px 40px;
      display: flex;
      justify-content: space-between;
      z-index: 100;
    }

    nav a {
      margin-left: 20px;
      text-decoration: none;
      color: var(--muted);
      font-weight: 500;
    }

    nav a:hover { color: var(--primary); }

    header {
      max-width: 1100px;
      margin: auto;
      padding: 100px 40px 80px;
      display: grid;
      grid-template-columns: 1.2fr 1fr;
      gap: 40px;
    }

    header h1 { font-size: 48px; margin-bottom: 16px; }
    header p.lead { font-size: 18px; color: var(--muted); }

    .cta {
      margin-top: 30px;
    }

    .cta a {
      display: inline-block;
      padding: 12px 24px;
      background: var(--primary);
      color: white;
      border-radius: 8px;
      text-decoration: none;
      font-weight: 600;
    }

    section {
      max-width: 1100px;
      margin: auto;
      padding: 80px 40px;
    }

    h2 {
      font-size: 32px;
      margin-bottom: 40px;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 24px;
    }

    .card {
      background: white;
      padding: 24px;
      border-radius: 14px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.05);
      transition: transform .2s ease, box-shadow .2s ease;
    }

    .card:hover {
      transform: translateY(-6px);
      box-shadow: 0 20px 40px rgba(0,0,0,0.08);
    }

    .role { font-weight: 600; }
    .meta { color: var(--muted); font-size: 14px; margin-bottom: 10px; }

    footer {
      background: var(--dark);
      color: white;
      padding: 60px 40px;
    }

    footer a { color: #93c5fd; text-decoration: none; }

    @media(max-width: 900px) {
      header { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

<nav>
  <strong>Shradha Dubey</strong>
  <div>
    <a href="#experience">Experience</a>
    <a href="#skills">Skills</a>
    <a href="#contact">Contact</a>
  </div>
</nav>

<header>
  <div>
    <h1>Data Engineer building scalable cloud data platforms</h1>
    <p class="lead">6+ years of experience designing AWS-based data pipelines, real-time systems, and analytics-ready data lakes for enterprise teams.</p>
    <div class="cta">
      <a href="#contact">Get in touch</a>
    </div>
  </div>
  <div>
    <div class="card">
      <p><strong>Core Focus</strong></p>
      <p>Big Data • AWS • ETL • Analytics Engineering</p>
      <p><strong>Current Role</strong></p>
      <p>AWS Data Engineer, Melius Infotech</p>
    </div>
  </div>
</header>

<section id="experience">
  <h2>Professional Experience</h2>
  <div class="grid">
    <div class="card">
      <p class="role">AWS Data Engineer – Melius Infotech</p>
      <p class="meta">Jan 2025 – Present</p>
      <ul>
        <li>Architected scalable AWS cloud solutions with strong security and cost controls.</li>
        <li>Built ELT pipelines using Glue, Lambda, Redshift, and Step Functions.</li>
        <li>Implemented serverless data processing to reduce infra overhead.</li>
      </ul>
    </div>

    <div class="card">
      <p class="role">Big Data Engineer – Rocket Mortgage</p>
      <p class="meta">Jun 2021 – Sept 2024</p>
      <ul>
        <li>Reduced data processing latency by 15% through pipeline optimization.</li>
        <li>Lowered storage costs by 20% via EMR and Glue tuning.</li>
        <li>Designed analytics-ready data marts improving query efficiency by 25%.</li>
      </ul>
    </div>
  </div>
</section>

<section id="skills">
  <h2>Skills & Technologies</h2>
  <div class="grid">
    <div class="card">
      <strong>Big Data & ETL</strong>
      <p>Python, SQL, Spark, Hadoop, Kafka, Data Modeling, Data Governance</p>
    </div>
    <div class="card">
      <strong>Cloud</strong>
      <p>AWS S3, EMR, Glue, Redshift, Lambda, IAM, CloudWatch</p>
    </div>
    <div class="card">
      <strong>Analytics & Tools</strong>
      <p>Tableau, Power BI, CI/CD, Agile, GitHub</p>
    </div>
  </div>
</section>

<footer id="contact">
  <h2>Contact</h2>
  <p>Email: <a href="mailto:shradha.dubeyy@gmail.com">shradha.dubeyy@gmail.com</a></p>
  <p>LinkedIn: <a href="https://www.linkedin.com/in/shradhadubey">linkedin.com/in/shradhadubey</a></p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
