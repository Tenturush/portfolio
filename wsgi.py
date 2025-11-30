# PythonAnywhere için WSGI dosyası
import sys
import os

# Proje klasörünüzün yolunu buraya yazın (PythonAnywhere'de)
project_home = '/home/KULLANICI_ADINIZ/mysite'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application


