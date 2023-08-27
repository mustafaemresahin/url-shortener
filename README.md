# URL Shortener

## Introduction

This is a simple yet powerful URL shortener built using Flask. The application allows users to shorten long URLs, making them easier to share and manage. It also provides features like setting expiration times for URLs and tracking the number of visits.

## Features

- **URL Shortening**: Convert long URLs into manageable short URLs.
- **Expiration Time**: Set an expiration time for the short URLs.
- **Visit Counter**: Track the number of visits for each short URL.
- **Delete URLs**: Ability to delete short URLs.
- **Responsive UI**: Built with Bootstrap for a clean and responsive interface.

## Installation

### Prerequisites

- Python 3.x
- pip
- virtualenv

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/url-shortener.git
    ```

2. Navigate to the project directory:

    ```bash
    cd url-shortener
    ```

3. Create a virtual environment:

    ```bash
    virtualenv venv
    ```

4. Activate the virtual environment:

    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

5. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the Flask application:

    ```bash
    flask run
    ```
    or
    ```bash
    py app.py
    ```

7. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## How to Use

1. **Shorten URL**: Enter the long URL in the input field and optionally set an expiration time. Click the "Shorten URL" button.
2. **Manage URLs**: Below the input field, you'll see a list of all shortened URLs. Each entry shows the original URL, the shortened URL, and the number of visits.
3. **Delete URLs**: Click the "Delete" button next to any URL to remove it.
4. **Expiration**: If set, the expiration time will be displayed next to the URL. The text will turn red when the URL has expired.

## Contributing

Feel free to fork the project, open an issue, or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
