**Web Application Firewall (WAF) Project**


**Overview**
This is a Web Application Firewall (WAF) project developed using Flask and Python. The WAF is designed to protect web applications from various malicious activities and attacks by filtering incoming requests and detecting potential security threats. It includes advanced features such as logging, real-time alerts, and the ability to identify and block malicious payloads.

**Features**

**Malicious IP Detection:** The WAF maintains a simulated database of known malicious IP addresses and can flag and block requests from these IPs.

**Malicious Payload Detection:** It identifies and blocks requests containing known malicious payloads, preventing SQL injection, XSS attacks, and more.

**Real-time Logging:** Requests are logged with detailed information, including IP address, User-Agent, and request data, for further analysis.

**Telegram Notifications:** The WAF sends real-time notifications to a Telegram channel, allowing administrators to take immediate action.
Contact Form Protection: The integrated contact form is protected against potential attacks by analyzing form submissions for malicious content.

**Responsive UI:** The UI is designed using Bootstrap, making it accessible and visually appealing across devices.

**About Us Page:** An About Us page with information about the project creator, Bicky Yadav, an IT student, and the project details.
Usage

**Configure Telegram API Token and Chat ID:** Replace TOKEN and CHAT_ID in app.py with your Telegram bot token and desired chat ID.
Run the application: python app.py

**Access the application at http://localhost:5000.**

**Note:** All html files under templates folder and all project is under app folder..
**License**
This project is licensed under the MIT License.
