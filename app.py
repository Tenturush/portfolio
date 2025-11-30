from flask import Flask, render_template

app = Flask(__name__)

# ========== BURAYA KENDİ BİLGİLERİNİZİ GİRİN ==========
SITE_DATA = {
    "company_name": "Bilge Güven",
    "slogan": "Danışmanlıkta Güvenilir Yol Arkadaşınız",
    "description": "Her projede net yol haritası, titiz uygulama ve açık iletişimle danışmanlık süreçlerinize aynı disiplin ve kaliteyle eşlik ediyoruz.",
    "phone": "+90 212 XXX XX XX",
    "email": "info@bilgeguven.info",
    "address": "İstanbul, Türkiye",
    
    "services": [
        {
            "title": "Kurumsal Danışmanlık",
            "description": "Şirketinizin büyüme hedeflerine ulaşması için stratejik danışmanlık hizmetleri sunuyoruz.",
            "icon": "📊"
        },
        {
            "title": "Finansal Danışmanlık",
            "description": "Mali yapınızı güçlendirmek ve sürdürülebilir büyüme için finansal çözümler üretiyoruz.",
            "icon": "💰"
        },
        {
            "title": "İş Geliştirme",
            "description": "Yeni pazarlara açılma ve iş fırsatlarını değerlendirme konusunda yanınızdayız.",
            "icon": "🚀"
        },
        {
            "title": "Proje Yönetimi",
            "description": "Projelerinizi zamanında ve bütçe dahilinde tamamlamak için profesyonel yönetim desteği.",
            "icon": "📋"
        },
        {
            "title": "Dijital Dönüşüm",
            "description": "İşletmenizi geleceğe taşıyacak dijital çözümler ve teknoloji danışmanlığı.",
            "icon": "💻"
        },
        {
            "title": "Eğitim ve Gelişim",
            "description": "Ekiplerinizin yetkinliklerini artıracak özelleştirilmiş eğitim programları.",
            "icon": "🎓"
        }
    ],
    
    "about": {
        "title": "Köklü Tecrübe, Güncel Bakış Açısı",
        "text": "Bilge Güven olarak, yıllara yayılan danışmanlık tecrübemizi güncel yaklaşımlar ve teknolojilerle birleştiriyoruz. Amacımız yalnızca görüş sunmak değil, uygulanabilir ve ölçülebilir bir yol haritası üretmektir.",
        "stats": [
            {"number": "10+", "label": "Yıllık Tecrübe"},
            {"number": "200+", "label": "Tamamlanan Proje"},
            {"number": "50+", "label": "Mutlu Müşteri"}
        ]
    },
    
    "publications": [
        {
            "title": "Kurumsal Başarının Anahtarları",
            "category": "Kurumsal",
            "date": "25 Kasım 2025",
            "slug": "kurumsal-basarinin-anahtarlari"
        },
        {
            "title": "Dijital Dönüşümde Dikkat Edilmesi Gerekenler",
            "category": "Teknoloji",
            "date": "20 Kasım 2025",
            "slug": "dijital-donusum"
        },
        {
            "title": "Etkili Proje Yönetimi İpuçları",
            "category": "Yönetim",
            "date": "15 Kasım 2025",
            "slug": "proje-yonetimi"
        }
    ]
}
# ======================================================

@app.route('/')
def home():
    return render_template('index.html', data=SITE_DATA)

@app.route('/hizmetler')
def services():
    return render_template('services.html', data=SITE_DATA)

@app.route('/hakkimizda')
def about():
    return render_template('about.html', data=SITE_DATA)

@app.route('/yayinlar')
def publications():
    return render_template('publications.html', data=SITE_DATA)

@app.route('/iletisim')
def contact():
    return render_template('contact.html', data=SITE_DATA)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
