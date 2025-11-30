from flask import Flask, request, redirect, render_template
import random
import string

app = Flask(__name__)

url_map = {}


def generate_short_id(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))


# --- Flask Routes (Endpoints) ---

# Handles the form submission
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the long URL from the submitted form data
        long_url = request.form['long_url']

        # Generate a unique ID
        short_id = generate_short_id()

        # Save the mapping
        url_map[short_id] = long_url

        # Get the full short link to display to the user
        short_link = request.url_root + short_id

        # Display a simple success message with the new link
        return f"""
        <h2>Success!</h2>
        <p>Your original URL: {long_url}</p>
        <p>Your short link is: <a href="{short_link}">{short_link}</a></p>
        <p><a href="/">Shorten another URL</a></p>
        """

    # For GET request (first time visiting the page)
    # Renders a simple HTML form
    return render_template('index.html')


# Redirect Endpoint: Handles the short link click
@app.route('/<short_id>')
def redirect_to_url(short_id):
    # Look up the long URL using the short ID
    long_url = url_map.get(short_id)

    if long_url:
        # If found, perform the redirect (status 302: Found)
        return redirect(long_url)
    else:
        # If not found, show a 404 error
        return "<h1>404: Link Not Found</h1>", 404


if __name__ == '__main__':
    # Runs the Flask application on port 5000
    app.run(debug=True)