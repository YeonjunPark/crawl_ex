import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawl.settings')
import django
django.setup()

from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

from university.models import Graduate_school

def main():
    url_set = { gs.url for gs in Graduate_school.objects.all() }

    graduate_school_list = []

    for page in range(1, 10000):
        params = {
            'field_resetype_value': 'E',
            'department': 'All',
            'page': page,
            'language': 'ko',
        }

        page_url = 'http://eng.snu.ac.kr/research'
        html = requests.get(page_url, params=params).text
        soup = BeautifulSoup(html, 'html.parser')

        for li_tag in soup.select('.item-list .research > li'):
            print(li_tag)

            continue

            title = a_tag.text
            link = urljoin(page_url, a_tag['href'])

            if link in url_set:
                print('End!')
                return graduate_school_list

            url_set.add(link)

            print(title, link)
            graduate_school_list.append(Graduate_school(title=title, url=link))

if __name__ == '__main__':
    # from django.db import connection

    graduate_school_list = main()
    Graduate_school.objects.bulk_create(graduate_school_list)

    # for idx, query in enumerate(connection.queries, 1):
        # print(idx, query)
