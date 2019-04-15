import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exercise.settings')
django.setup()

import concurrent.futures
import threading

from django.db import IntegrityError
import requests
import pandas as pd
from favicon_finder.models import Favicon

thread_local = threading.local()


def get_site_urls(file_path):
    results = pd.read_csv(file_path, header=None, delimiter=',', nrows=1000000)
    url_list = results[1].tolist()
    return url_list


def get_session():
    if not getattr(thread_local, "session", None):
        thread_local.session = requests.Session()
        thread_local.session.headers.update(
            {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})
    return thread_local.session


def get_favicon_url(url):
    session = get_session()
    full_url = "http://" + url
    try:
        with session.get(full_url, timeout=6) as response:
            if response.status_code == 200:
                favicon = Favicon(url=url)
                try:
                    if favicon.get_fav_url(url):
                        favicon.save()
                        return
                    else:
                        print(f'{full_url}: could not find favicon')
                        return
                except IntegrityError:
                    return
            else:
                print(f'{response.status_code}:' + f' {full_url}')
                return
    except requests.exceptions.RequestException as e:
        print(e)


def get_all_favicon_url(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=75) as executor:
        executor.map(get_favicon_url, sites)


content = get_site_urls('/users/patricktonne/documents/top-1m.csv')
while len(Favicon.objects.all()) < 200000:
    get_all_favicon_url(content)
