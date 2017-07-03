import json, os, urllib2

from django.conf import settings

def get_invoice_api_data():
    auth_token_file = os.path.join(settings.PROJECT_ROOT, 'auth_token.txt')
    with open(auth_token_file) as f:
        AUTH_TOKEN = f.read().strip()

    url = 'https://falcon.simplelegal.com/api/v1/invoices/'
    request = urllib2.Request(url)
    request.add_header('Authorization', 'Token ' + AUTH_TOKEN)
    response = urllib2.urlopen(request)
    data = json.load(response)

    return data
