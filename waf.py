#import http.client
import logging
import itertools
from flask import Flask, request, render_template, jsonify
import requests
TOKEN = 'Your Token ID from botfather'
CHAT_ID = 'Your Chat ID'
app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Simulated database of malicious IP addresses
malicious_ips = set()

# Read malicious payloads from file
malicious_payloads = []
with open('E:/Web_Application Firewall/app/malicious_payload.txt', 'r') as f:
    for line in f:
        malicious_payloads.append(line.strip())

# Generate all combinations of lowercase and uppercase letters for payloads
all_combinations = set()
for payload in malicious_payloads:
    combinations = [''.join(combination) for combination in itertools.product(*zip(payload.upper(), payload.lower()))]
    all_combinations.update(combinations)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about-us', methods=['GET', 'POST'])
def about():
    return render_template("about-us.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact_form():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        ip_address = request.remote_addr
        user_agent = request.headers.get('User-Agent', '')
        request_data = request.form['name'] + request.form['email'] + request.form['message']

        if is_request_malicious(ip_address, user_agent, request_data):
            log_malicious_request(ip_address, user_agent, request_data)
            #send_sms_notification("Warning! Malicious request detected from IP: " + ip_address)
            return render_template("403.html")
        
        log_valid_request(ip_address, user_agent, request_data)
        #send_sms_notification("Valid request received from IP: " + ip_address)
        return jsonify(message='Your request has been received successfully.')
    
    return render_template("contact.html")

def is_request_malicious(ip_address, user_agent, request_data):
    # Check if the IP address or user agent matches any known malicious patterns
    if ip_address in malicious_ips:
        return True

    # Check for malicious payloads in the request data
    for payload in all_combinations:
        if payload in request_data:
            return True

    return False

def log_malicious_request(ip_address, user_agent, request_data):
    # Log the malicious request
    logging.warning(f'Malicious request from IP: {ip_address}, User-Agent: {user_agent}')
    alert_message = "Malicious request from IP: " + ip_address + " User-Agent: " + user_agent
    response = send_telegram_message(alert_message)
    if response.get('ok'):
        print("Message sent successfully!")
    else:
        print("Message sending failed.")
        print("Response:", response)
    logging.warning(f'Request Data: {request_data}')
    alert_message = "Request Data: " + request_data
    response = send_telegram_message(alert_message)


def log_valid_request(ip_address, user_agent, request_data):
    # Log the valid request
    logging.info(f'Valid request from IP: {ip_address}, User-Agent: {user_agent}')
    logging.info(f'Request Data: {request_data}')

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.get(url, params=params)
    return response.json()


if __name__ == '__main__':
    app.run(debug=True)


