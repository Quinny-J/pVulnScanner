# 📜 pVulnScanner

A web-based vulnerability scanner that can for website vulnerability's

## ✨ Features

- Xss Scanner
- SQL Scanner
- Web GUI for easy use

## 📁 Project Structure

```
pVulnScanner/
│
├── app.py
├── xss_checker.py
├── sql_injection_checker.py
├── templates/
│   └── index.html
```

## 🛠️ Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/quinny-j/pVulnScanner.git
    cd pVulnScanner
    ```

2. **Create a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```sh
    pip install Flask
    ```

## 🚀 Usage

1. **Run the application:**

    ```sh
    python app.py
    ```

2. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```

3. **Scan for XSS and SQL Vulns using the web interface.**

## 🎨 Styling

This project uses [Tailwind CSS](https://tailwindcss.com/) for styling. The CSS is included via CDN for simplicity.

## 🧑‍💻 Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.
.