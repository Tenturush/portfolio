from flask import Flask, render_template

app = Flask(__name__)

# ========== BURAYA KENDİ BİLGİLERİNİZİ GİRİN ==========
PORTFOLIO_DATA = {
    "name": "Adınız Soyadınız",
    "title": "Web Developer & Designer",
    "bio": "Merhaba! Ben tutkulu bir yazılım geliştiriciyim. Modern ve kullanıcı dostu web uygulamaları geliştirmeyi seviyorum.",
    "email": "email@example.com",
    "github": "https://github.com/kullaniciadi",
    "linkedin": "https://linkedin.com/in/kullaniciadi",
    
    "skills": [
        {"name": "Python", "level": 90},
        {"name": "JavaScript", "level": 85},
        {"name": "HTML/CSS", "level": 95},
        {"name": "React", "level": 75},
        {"name": "Flask", "level": 80},
    ],
    
    "projects": [
        {
            "title": "E-Ticaret Platformu",
            "description": "Modern bir online alışveriş deneyimi sunan full-stack uygulama.",
            "tech": ["Python", "Flask", "PostgreSQL"],
            "link": "#"
        },
        {
            "title": "Task Manager App",
            "description": "Görev yönetimi için minimalist ve kullanışlı bir web uygulaması.",
            "tech": ["React", "Node.js", "MongoDB"],
            "link": "#"
        },
        {
            "title": "Weather Dashboard",
            "description": "Gerçek zamanlı hava durumu takibi yapan interaktif dashboard.",
            "tech": ["JavaScript", "API", "Chart.js"],
            "link": "#"
        },
    ],
    
    "blog_posts": [
        {
            "title": "Python ile Web Geliştirmeye Başlamak",
            "date": "28 Kasım 2025",
            "summary": "Flask framework'ü kullanarak ilk web uygulamanızı nasıl oluşturacağınızı öğrenin.",
            "slug": "python-web-gelistirme"
        },
        {
            "title": "Modern CSS Teknikleri",
            "date": "20 Kasım 2025", 
            "summary": "Flexbox, Grid ve CSS değişkenleri ile responsive tasarımlar oluşturun.",
            "slug": "modern-css-teknikleri"
        },
    ]
}
# ======================================================

@app.route('/')
def home():
    return render_template('index.html', data=PORTFOLIO_DATA)

@app.route('/blog')
def blog():
    return render_template('blog.html', data=PORTFOLIO_DATA)

@app.route('/blog/<slug>')
def blog_post(slug):
    post = next((p for p in PORTFOLIO_DATA['blog_posts'] if p['slug'] == slug), None)
    return render_template('post.html', data=PORTFOLIO_DATA, post=post)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

