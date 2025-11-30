# SimpleURL: A Minimalist URL Shortener Utility

[![Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask-brightgreen.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

SimpleURL is a lightweight, self-hosted web application designed to solve a common problem: turning long, unwieldy URLs into short, clean, and memorable links.

This project is built with **Python and Flask** and is intentionally minimal, using an in-memory dictionary for link storage to keep the setup virtually instantaneous. It is an excellent starting point for those looking to understand basic web application routing and data handling.

---

## ✨ Features

* **Fast Shortening:** Convert any URL into a 6-character short link.
* **Simple Web Interface:** A single page for submitting new URLs.
* **Automatic Redirection:** Short links automatically redirect visitors to the original destination URL.
* **Minimal Dependencies:** Requires only the Flask framework.

---

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have **Python 3** installed on your system.

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/TheAustinMiller/python-url-shortener
    ```
2.  **Install Dependencies:**
    ```bash
    pip install Flask
    ```
3.  **Run the Application:**
    ```bash
    python app.py
    ```

The application will start running at `http://127.0.0.1:5000/`.

---

## 💡 How to Use

1.  Open your browser to `http://127.0.0.1:5000/`.
2.  Paste a long URL into the input box and click **Shorten**.
3.  The resulting short link (e.g., `http://127.0.0.1:5000/aBcDeF`) will be displayed on the screen.
4.  Sharing that short link will automatically redirect users to the original long URL.

---

## ⚠️ Important Note on Persistence

This version of SimpleURL uses a Python **in-memory dictionary** (`url_map`) for storage.

* **Pro:** Setup is instant; no database required.
* **Con:** **All links are LOST when the `app.py` server is shut down or restarted.**

See the section below for upgrade paths if you want permanent storage.

---

## ⏭️ Future Enhancements & Contributions

This project is a perfect sandbox for learning and expansion. Here are some immediate next steps, especially leveraging your knowledge in other languages:

| Upgrade Path | Skills Required | Description |
| :--- | :--- | :--- |
| **Database Persistence** | Python, SQL/Database Knowledge | Replace the in-memory `url_map` with a permanent storage solution like **SQLite** or **PostgreSQL** to save links permanently. |
| **Separate Frontend** | TypeScript, Angular, API Calls | Detach the frontend by creating a dedicated **Angular application** that communicates with the Flask app as a dedicated **REST API**. |
| **Analytics** | Database, Logging | Track how many times each short link is clicked. |
| **Custom Links** | Python Logic | Allow users to specify their own short identifier instead of a random one. |

Feel free to fork this repository and submit pull requests for any of these improvements!
