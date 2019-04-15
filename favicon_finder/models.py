import re

from django.db import models, IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from bs4 import BeautifulSoup
import requests


class Favicon(models.Model):
    url = models.CharField(max_length=255, unique=True)
    fav_url = models.URLField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.url

    # Check 'url/favicon.ico' for fav_url
    def _get_fav_url_from_domain(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
            response = requests.get(url + '/favicon.ico', headers=headers, timeout=6)
        except requests.exceptions.RequestException as e:
            print(e)
            return False
        else:
            if response.status_code == 200:
                # if 'url/favicon.ico' redirects to 'newURL.com', try 'newURL/favicon.ico'
                if not re.search('ico$', response.url):
                    try:
                        new_url = response.url
                        new_response = requests.get(new_url + '/favicon.ico', headers=headers, timeout=6)
                    except requests.exceptions.RequestException as e:
                        print(e)
                        return False
                    else:
                        if re.search('ico$', new_response.url) and new_response.status_code == 200\
                                and new_response.headers.get('Content-Length') != '0':
                            self.fav_url = new_response.url
                            return self.fav_url
                        else:
                            return False
                else:
                    if response.headers.get('Content-Length') != '0':
                        self.fav_url = response.url
                        return self.fav_url
                    else:
                        return False
            else:
                return False

    # Scrape url for the first <link> element with 'rel' attribute containing 'icon'
    def _scrape_fav_url(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
            response = requests.get(url, headers=headers, timeout=6)
        except requests.exceptions.RequestException as e:
            print(e)
            return False
        else:
            soup = BeautifulSoup(response.text)
            results = [i['href'] for i in soup.findAll('link', rel=re.compile('^icon$'))]
            if results:
                # check for absolute urls (eg. '/images/favicon.ico') and, if so, prepend root URL
                if not re.match('https?://(www.)?', results[0]):
                    if re.match('^/', results[0]):
                        absolute_url = results[0]
                        self.fav_url = url + absolute_url
                        return self.fav_url
                    else:
                        absolute_url = results[0]
                        self.fav_url = url + '/' + absolute_url
                        return self.fav_url
                else:
                    self.fav_url = results[0]
                    return self.fav_url
            else:
                return False

    def get_fav_url(self, host_name):
        url = 'http://' + host_name

        if self._get_fav_url_from_domain(url):
            print(f'{url}: Successful domain search')
            return True
        elif self._scrape_fav_url(url):
            print(f'{url}: Successful scrape search')
            return True
        else:
            print(f'{url}: Favicon not found')
            return False

    @staticmethod
    def get_from_db_or_request(host_name, get_fresh):
        response_data = {}
        favicon = Favicon(url=host_name)
        if get_fresh == 'true':
            # Grab fav_url from site; if object with that url already in db, call get_fav_url() with that object
            try:
                if favicon.get_fav_url(host_name):
                    favicon.save()
            except IntegrityError:
                favicon = Favicon.objects.get(url=host_name)

                if favicon.get_fav_url(host_name):
                    favicon.save()
        else:
            try:
                favicon = Favicon.objects.get(url=host_name)
            except ObjectDoesNotExist:
                favicon = Favicon(url=host_name)

                if favicon.get_fav_url(host_name):
                    favicon.save()

        response_data['fav_image'] = favicon.fav_url
        response_data['website'] = favicon.url
        return response_data

    @staticmethod
    def clean_url(url):
        regex = re.compile('https?://(www.)?')
        host = regex.sub('', url)
        return host
