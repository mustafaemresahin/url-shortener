# Importing required libraries and modules
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from urllib.parse import urlparse
import string
import random
from datetime import datetime, timedelta

# Initialize Flask application
app = Flask(__name__)
# Set the secret key for session data encryption
app.secret_key = 'l&Z1ly3aa!'

# Dictionary to hold the mapping of original URLs to their short URLs
url_list = {}

# Function to generate a random 6-character short URL
def generate_short_url():
    # Define the set of characters to use for generating short URLs
    characters = string.ascii_letters + string.digits
    # Generate a random 6-character string
    short_url = ''.join(random.choice(characters) for i in range(6))
    return short_url

# Function to check if a given URL is valid
def is_valid_url(url):
    # Parse the given URL into its components
    parsed_url = urlparse(url)
    # Check if the URL has both a valid scheme and a netloc (domain)
    return all([parsed_url.scheme in ['http', 'https'], parsed_url.netloc])

# Route for the index page
@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize local variables to hold request data
    short_url = None
    original_url = None
    expiration_time = None
    click_count = 0

    # Handle POST request for URL shortening
    if request.method == 'POST':
        # Extract URL and expiration time from form data
        original_url = request.form['url']
        expiration_time = request.form.get('expiration_time', None)
        # Capture the current time for expiration checks
        current_time = datetime.now()

        # Validate the URL and flash an error message if invalid
        if not is_valid_url(original_url):
            flash('Invalid URL format! Please enter a URL like https://mustafaemresahin.com')
            return render_template('index.html', url_list=url_list)

        # Check if the URL already exists in the dictionary and is not expired
        if original_url in url_list:
            # Capture any existing expiration time for the URL
            existing_expiration_time = url_list[original_url].get('expiration_time')
            if existing_expiration_time:
                # Convert the string to a datetime object
                dt_object = datetime.strptime(existing_expiration_time, '%Y-%m-%dT%H:%M')
                # Check if the URL has expired
                if current_time > dt_object:
                    flash('This URL has already been shortened but has expired.')
                    return render_template('index.html', url_list=url_list)
            # Inform the user that the URL already exists
            flash('This URL has already been shortened.')
            return render_template('index.html', url_list=url_list)

        # Generate and store a new short URL if it doesn't already exist
        if original_url not in url_list:
            short_url = generate_short_url()
            # Store the short URL, expiration time, and click count in the dictionary
            url_list[original_url] = {'short_url': short_url, 'expiration_time': expiration_time, 'click_count': 0}

        # Update the expiration times for all URLs in the dictionary
        current_time = datetime.now()
        for original, data in url_list.items():
            if data['expiration_time']:
                dt_object = datetime.strptime(data['expiration_time'], '%Y-%m-%dT%H:%M')
                # Convert the datetime object to a human-readable string
                data['formatted_expiration_time'] = dt_object.strftime('%B %d, %Y, %H:%M %p')
                # Check if the URL has expired
                data['is_expired'] = current_time > dt_object
        
        # Redirect to the index page after processing
        return redirect(url_for('index'))

    # Render the index page for GET requests
    return render_template('index.html', url_list=url_list)

# Route to handle URL redirection
@app.route('/<short_url>')
def redirect_to_original(short_url):
    # Loop through the dictionary to find the original URL
    for original, data in url_list.items():
        if data['short_url'] == short_url:
            # Check if the URL has expired
            if data.get('expiration_time') and datetime.now() > datetime.strptime(data['expiration_time'], '%Y-%m-%dT%H:%M'):
                flash('URL has expired!')
                return render_template('index.html', url_list=url_list)
            # Increment the click count for the URL
            data['click_count'] += 1
            # Redirect to the original URL
            return redirect(original)

    # Handle cases where the short URL is not found
    flash('URL not found!')
    return redirect(url_for('index'))

# Route to handle deletion of URLs
@app.route('/delete_url', methods=['POST'])
def delete_url():
    # Extract the short URL to delete from the JSON data
    data = request.json
    short_url_to_delete = data.get('url')
    
    # Loop through the dictionary to find and delete the URL
    for original, data in list(url_list.items()): 
        if data['short_url'] == short_url_to_delete:
            del url_list[original]
            return jsonify({'success': True}), 200

    # Handle cases where the URL is not found
    return jsonify({'success': False, 'message': 'URL not found'}), 404

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
