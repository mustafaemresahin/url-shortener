from flask import Flask, render_template, request, redirect, url_for, flash
from urllib.parse import urlparse
import string
import random
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'l&Z1ly3aa!'

# Dictionary to store short_urls
url_list = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for i in range(6))
    return short_url

def is_valid_url(url):
    parsed_url = urlparse(url)
    return all([parsed_url.scheme in ['http', 'https'], parsed_url.netloc])

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    original_url = None
    expiration_time = None
    click_count = 0

    if request.method == 'POST':
        original_url = request.form['url']
        expiration_time = request.form.get('expiration_time', None)

        if not is_valid_url(original_url):
            flash('Invalid URL format! Please enter a URL like https://mustafaemresahin.com')
            return render_template('index.html', url_list=url_list)

        if original_url in url_list:
            short_url = url_list[original_url]['short_url']
        else:
            short_url = generate_short_url()
            url_list[original_url] = {'short_url': short_url, 'expiration_time': expiration_time, 'click_count': 0}

    return render_template('index.html', short=short_url, original=original_url, url_list=url_list)

@app.route('/<short_url>')
def redirect_to_original(short_url):
    for original, data in url_list.items():
        if data['short_url'] == short_url:
            if data.get('expiration_time') and datetime.now() > datetime.strptime(data['expiration_time'], '%Y-%m-%dT%H:%M'):
                flash('URL has expired!')
                return redirect(url_for('index'))
            data['click_count'] += 1
            return redirect(original)
    flash('URL not found!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
