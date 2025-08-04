Automated Reconnaissance Tool
Automates the reconnaissance phase of web application testing by combining:

Subdomain Enumeration (Sublist3r)

Status and Technology Detection (HTTPX)

Directory Bruteforce (Dirsearch)

This tool provides a Flask-based web interface with a dark-themed frontend to scan domains, check live hosts, and discover hidden directories. Results are organized into timestamped folders for easy review.

Features
Automated Subdomain Enumeration using Sublist3r

HTTPX integration for live status codes, titles, technologies, and IPs

Dirsearch for directory and file brute-forcing

Timestamped result storage for each scan

Flask-based UI for user-friendly interaction

Project Structure
graphql
Copy
Edit
├── app.py                # Flask backend
├── templates/
│   └── input.html        # Frontend UI
├── Sublist3r/            # Sublist3r tool
├── dirsearch/            # Dirsearch tool
├── scan_results_*        # Auto-generated folders with results
Prerequisites
Python 3.x

Flask

Sublist3r

HTTPX

Dirsearch

Linux (recommended for tool compatibility)

Install dependencies:

bash
Copy
Edit
pip install flask
git clone https://github.com/aboul3la/Sublist3r.git
git clone https://github.com/projectdiscovery/httpx.git
git clone https://github.com/maurosoria/dirsearch.git
How to Run
Clone this repository

Install all dependencies

Run the Flask app:

nginx
Copy
Edit
python app.py
Open http://127.0.0.1:5000 in your browser

Usage
Enter a domain (e.g., example.com) in the web interface.

The tool performs:

Sublist3r → Enumerates subdomains

HTTPX → Checks active hosts and gathers status codes, titles, and technologies

Dirsearch → Brute-forces directories

View results:

In the web interface

Inside timestamped folders (e.g., scan_results_example.com_20250801_133045)

Example Output
HTTPX Result Example (JSON):

json
Copy
Edit
{
  "url": "https://sub.example.com",
  "status-code": 200,
  "title": "Login Page",
  "tech": ["Apache", "PHP"],
  "ip": "192.168.1.1"
}
Dirsearch Example:

bash
Copy
Edit
/admin (200)
/uploads (403)
/backup.zip (200)
Future Enhancements
Quick Scan vs Deep Scan modes

Export results to PDF or CSV

Add Nmap for port scanning

Authentication support for restricted directories

Disclaimer
This tool is intended for educational and ethical security testing only.
Do not use it on systems you do not own or are not authorized to test.Automated Reconnaissance Tool
Automates the reconnaissance phase of web application testing by combining:

Subdomain Enumeration (Sublist3r)

Status and Technology Detection (HTTPX)

Directory Bruteforce (Dirsearch)

This tool provides a Flask-based web interface with a dark-themed frontend to scan domains, check live hosts, and discover hidden directories. Results are organized into timestamped folders for easy review.

Features
Automated Subdomain Enumeration using Sublist3r

HTTPX integration for live status codes, titles, technologies, and IPs

Dirsearch for directory and file brute-forcing

Timestamped result storage for each scan

Flask-based UI for user-friendly interaction

Project Structure
graphql
Copy
Edit
├── app.py                # Flask backend
├── templates/
│   └── input.html        # Frontend UI
├── Sublist3r/            # Sublist3r tool
├── dirsearch/            # Dirsearch tool
├── scan_results_*        # Auto-generated folders with results
Prerequisites
Python 3.x

Flask

Sublist3r

HTTPX

Dirsearch

Linux (recommended for tool compatibility)

Install dependencies:

bash
Copy
Edit
pip install flask
git clone https://github.com/aboul3la/Sublist3r.git
git clone https://github.com/projectdiscovery/httpx.git
git clone https://github.com/maurosoria/dirsearch.git
How to Run
Clone this repository

Install all dependencies

Run the Flask app:

nginx
Copy
Edit
python app.py
Open http://127.0.0.1:5000 in your browser

Usage
Enter a domain (e.g., example.com) in the web interface.

The tool performs:

Sublist3r → Enumerates subdomains

HTTPX → Checks active hosts and gathers status codes, titles, and technologies

Dirsearch → Brute-forces directories

View results:

In the web interface

Inside timestamped folders (e.g., scan_results_example.com_20250801_133045)

Example Output
HTTPX Result Example (JSON):

json
Copy
Edit
{
  "url": "https://sub.example.com",
  "status-code": 200,
  "title": "Login Page",
  "tech": ["Apache", "PHP"],
  "ip": "192.168.1.1"
}
Dirsearch Example:

bash
Copy
Edit
/admin (200)
/uploads (403)
/backup.zip (200)
Future Enhancements
Quick Scan vs Deep Scan modes

Export results to PDF or CSV

Add Nmap for port scanning

Authentication support for restricted directories

Disclaimer
This tool is intended for educational and ethical security testing only.
Do not use it on systems you do not own or are not authorized to test.
