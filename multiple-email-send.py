from dotenv import load_dotenv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import time

# Load .env file
load_dotenv()

# ✅ SMTP Server Details (GoDaddy SMTP)
SMTP_SERVER = "smtpout.secureserver.net"
SMTP_PORT = 465  # SSL Port

# ✅ Your Email & Password
SENDER_EMAIL = "azfar@helpopshub.com"
SENDER_PASSWORD = os.getenv("SENDER_EMAIL_PASSWORD")  # Loaded from .env file

if not SENDER_PASSWORD:
    raise ValueError("⚠️ Error: SENDER_EMAIL_PASSWORD not found in .env file!")

# ✅ CSV File Path (Ensure the file is in the correct location)
csv_file = "honabro.csv"  # ⚠️ Update the path if needed

# ✅ Email Subject
subject = "🎉 Shortlisted for Friendly Interview"

# ✅ Dynamic Email Content (Easily Editable)
INTERVIEW_DATE = "Monday, 25th February 2025"
INTERVIEW_TIME = "3:00 PM IST"
TEST_LINK = "https://meet.google.com/wde-svis-hfv"
WHATSAPP_GROUP = "https://chat.whatsapp.com/Bl04la4yUb801sK7S0in8m"
DISCORD_SERVER = "https://discord.gg/9acQsABb"
GITHUB_ORG = "https://github.com/HelpOps-Hub"
LINKEDIN_PAGE = "https://www.linkedin.com/company/helpops-hub"
TWITTER = "https://twitter.com/helpopshub"
INSTAGRAM = "https://instagram.com/helpopshub"
FACEBOOK = "https://facebook.com/helpopshub"
SUPPORT_EMAIL = "azfar@helpopshub.com"

# ✅ Read Email List from CSV
df = pd.read_csv(csv_file)
email_list = list(zip(df["Email"], df["Name"]))

# ✅ Connect to SMTP Server (SSL Secure Connection)
server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
server.login(SENDER_EMAIL, SENDER_PASSWORD)

for index, (email, name) in enumerate(email_list):
    # ✅ Email Body (HTML Format)
    email_body = f'''
    <html>
    <head>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                background-color: #f7f7f7;
                margin: 0;
                padding: 0;
                color: #333;
            }}
            .email-container {{
                max-width: 600px;
                margin: 20px auto;
                background: #ffffff;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                background: linear-gradient(135deg, #6a11cb, #2575fc);
                color: white;
                padding: 30px 20px;
                text-align: center;
            }}
            .header h1 {{
                margin: 0;
                font-size: 28px;
                font-weight: bold;
            }}
            .content {{
                padding: 30px 20px;
            }}
            .content h2 {{
                color: #2575fc;
                font-size: 24px;
                margin-bottom: 20px;
            }}
            .content p {{
                font-size: 16px;
                line-height: 1.6;
                margin-bottom: 20px;
            }}
            .content ul {{
                margin: 0;
                padding: 0 0 0 20px;
            }}
            .content ul li {{
                margin-bottom: 10px;
            }}
            .button {{
                display: inline-block;
                padding: 12px 24px;
                margin: 10px 0;
                font-size: 16px;
                color: white;
                background: #25D366;
                text-decoration: none;
                border-radius: 6px;
                transition: background 0.3s ease;
            }}
            .button.discord {{
                background: #5865F2;
            }}
            .button:hover {{
                opacity: 0.9;
            }}
            .footer {{
                text-align: center;
                padding: 20px;
                background: #f1f1f1;
                color: #666;
                font-size: 14px;
            }}
            .footer a {{
                color: #2575fc;
                text-decoration: none;
            }}
            .footer a:hover {{
                text-decoration: underline;
            }}
            .social-links {{
                margin-top: 20px;
            }}
            .social-links a {{
                display: inline-block;
                margin: 0 10px;
                color: #2575fc;
                text-decoration: none;
                font-size: 24px;
                transition: color 0.3s ease;
            }}
            .social-links a:hover {{
                color: #6a11cb;
            }}
        </style>
        <!-- Add Font Awesome for Icons -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <h1>🎉 Congratulations, {name}!</h1>
            </div>
            <div class="content">
                <h2>You're Shortlisted for the Software Developer Internship!</h2>
                <p>We are thrilled to inform you that you have been shortlisted for the <strong>Software Developer Internship</strong> at <strong>HelpOps-Hub</strong>! 🚀</p>
                <p>Here are the details for your upcoming interview:</p>
                <ul>
                    <li><strong>Date:</strong> {INTERVIEW_DATE}</li>
                    <li><strong>Time:</strong> {INTERVIEW_TIME}</li>
                    <li><strong>Mode:</strong> Google Meet (Link will be shared in groups)</li>
                </ul>
                <p>To stay updated and receive the Google Meet link, please join our official groups:</p>
                <a href="{WHATSAPP_GROUP}" class="button">Join WhatsApp Group</a>
                <a href="{DISCORD_SERVER}" class="button discord">Join Discord Server</a>
                <p>These groups are designed for smooth communication and instant updates regarding the interview process. Make sure to join them ASAP!</p>
                <hr>
                <p><strong>💡 Stay Connected for Future Opportunities!</strong></p>
                <p>🔗 <a href="{GITHUB_ORG}">GitHub Organization</a></p>
                <p>🔗 <a href="{LINKEDIN_PAGE}">LinkedIn Page</a></p>
                <hr>
                <div class="social-links">
                    <p>📧 <strong>Follow Us:</strong></p>
                    <a href="{GITHUB_ORG}"><i class="fab fa-github"></i></a>
                    <a href="{LINKEDIN_PAGE}"><i class="fab fa-linkedin"></i></a>
                    <a href="{TWITTER}"><i class="fab fa-twitter"></i></a>
                    <a href="{INSTAGRAM}"><i class="fab fa-instagram"></i></a>
                    <a href="{FACEBOOK}"><i class="fab fa-facebook"></i></a>
                </div>
            </div>
            <div class="footer">
                <p>For any queries, feel free to contact us at: <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a></p>
                <p>Best regards,<br><strong>HelpOps-Hub Team</strong></p>
            </div>
        </div>
    </body>
    </html>
    '''

    # ✅ Setup Email Message
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(email_body, 'html'))

    try:
        # ✅ Send the email
        server.sendmail(SENDER_EMAIL, email, msg.as_string())
        print(f"✅ Email sent to {name} ({email})")
    except Exception as e:
        print(f"❌ Error sending to {name} ({email}): {e}")

    # ✅ To avoid spam detection, wait after every 10 emails
    if (index + 1) % 10 == 0:
        print("⏳ Waiting for 10 seconds to avoid rate limits...")
        time.sleep(10)

# ✅ Close SMTP Server Connection
server.quit()
print("🎉 All emails sent successfully!")
