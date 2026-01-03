from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Shradha Dubey | Data Engineer</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; background: #f9fafb; color: #111827; }
        header { padding: 60px 20px; max-width: 1000px; margin: auto; }
        h1 { font-size: 40px; margin-bottom: 10px; }
        h2 { margin-top: 40px; }
        section { max-width: 1000px; margin: auto; padding: 40px 20px; }
        .card { background: white; padding: 20px; margin-bottom: 20px; border-radius: 8px; }
        footer { background: #111827; color: white; padding: 30px 20px; }
        a { color: #2563eb; text-decoration: none; }
        ul { padding-left: 20px; }
    </style>
</head>
<body>

<header>
    <h1>Shradha Dubey</h1>
    <p><strong>Senior Data Engineer | AWS | Big Data Platforms</strong></p>
    <p>Big Data Engineer with 6+ years of experience building scalable AWS-based data pipelines, real-time processing systems, and analytics-ready data lakes.</p>
</header>

<section>
    <h2>Professional Experience</h2>

    <div class=\"card\">
        <h3>AWS Data Engineer – Melius Infotech</h3>
        <p><em>Jan 2025 – Present</em></p>
        <ul>
            <li>Designed scalable AWS cloud architectures with high availability and cost efficiency.</li>
            <li>Built ELT pipelines using AWS Glue, Lambda, Redshift, and Step Functions.</li>
            <li>Implemented serverless data processing solutions.</li>
        </ul>
    </div>

    <div class=\"card\">
        <h3>Big Data Engineer – Rocket Mortgage</h3>
        <p><em>Jun 2021 – Sept 2024</em></p>
        <ul>
            <li>Reduced data processing time by 15% using optimized AWS pipelines.</li>
            <li>Cut storage costs by 20% via EMR and Glue optimization.</li>
            <li>Built data models and marts improving query efficiency by 25%.</li>
        </ul>
    </div>
</section>

<section>
    <h2>Skills</h2>
    <div class=\"card\">
        <p><strong>Big Data & ETL:</strong> Python, SQL, Spark, Hadoop, Kafka, Data Modeling</p>
        <p><strong>Cloud:</strong> AWS S3, EMR, Glue, Redshift, Lambda, IAM</p>
        <p><strong>Analytics:</strong> Tableau, Power BI, CI/CD, Agile</p>
    </div>
</section>

<footer>
    <section>
        <h2>Contact</h2>
        <p>Email: <a href=\"mailto:shradha.dubeyy@gmail.com\">shradha.dubeyy@gmail.com</a></p>
        <p>LinkedIn: <a href=\"https://www.linkedin.com/in/shradhadubey\">linkedin.com/in/shradhadubey</a></p>
    </section>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
