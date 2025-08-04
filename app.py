from flask import Flask, render_template, request, jsonify
import subprocess
import os
import json
from datetime import datetime

app = Flask(_name_, template_folder='templates')

@app.route('/')
def index():
    return render_template('input.html')  # If your file is named input.html

@app.route('/scan_sublist3r', methods=['POST'])
def scan_sublist3r():
    domain = request.json.get('domain')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"scan_results_{domain}_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)

    subdomain_file = f"{output_dir}/subdomains.txt"

    try:
        subprocess.run([
            "python3", "Sublist3r/sublist3r.py", "-d", domain,
            "-o", subdomain_file,
            "-e", "Google,Baidu,Ask,Dogpile,Exalead,Yahoo,Bing,Netcraft"
        ], check=True)

        with open(subdomain_file) as f:
            subdomains = [line.strip() for line in f if line.strip()]
        return jsonify({"status": "ok", "subdomains": subdomains, "output_dir": output_dir})

    except subprocess.CalledProcessError as e:
        return jsonify({"status": "error", "error": str(e)})

@app.route('/scan_httpx', methods=['POST'])
def scan_httpx():
    output_dir = request.json.get('output_dir')
    subdomain_file = f"{output_dir}/subdomains.txt"
    httpx_output = f"{output_dir}/httpx_results.json"

    try:
        subprocess.run([
            "bash", "-c",
            f"cat {subdomain_file} | httpx -silent -status-code -title -tech-detect -ip -cname -json -o {httpx_output}"
        ], check=True)

        with open(httpx_output) as f:
            lines = f.read().splitlines()

        parsed_results = []
        for line in lines:
            try:
                parsed_results.append(json.loads(line))
            except json.JSONDecodeError:
                continue

        return jsonify({"status": "ok", "httpx": parsed_results})

    except subprocess.CalledProcessError as e:
        return jsonify({"status": "error", "error": str(e)})

@app.route('/scan_dirsearch', methods=['POST'])
def scan_dirsearch():
    output_dir = request.json.get('output_dir')
    subdomain_file = f"{output_dir}/subdomains.txt"
    results = []

    try:
        with open(subdomain_file) as f:
            subdomains = [line.strip() for line in f if line.strip()]
        for sub in subdomains:
            safe_name = ''.join(c if c.isalnum() else '_' for c in sub)
            outfile = f"{output_dir}/{safe_name}.txt"
            subprocess.run([
                "python3", "dirsearch/dirsearch.py", "-u", f"http://{sub}",
                "-e", "php,html,js", "-o", outfile
            ], check=True)
            if os.path.exists(outfile):
                with open(outfile) as f:
                    lines = [line.strip() for line in f if line.strip()]
                results.append({"subdomain": sub, "paths": lines})
        return jsonify({"status": "ok", "dirsearch": results})

    except subprocess.CalledProcessError as e:
        return jsonify({"status": "error", "error": str(e)})

if _name_ == '_main_':
    app.run(debug=True)
