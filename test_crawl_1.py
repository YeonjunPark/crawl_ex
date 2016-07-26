import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'programming.settings')
import django
django.setup()

from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
