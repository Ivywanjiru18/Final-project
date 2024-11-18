# Alert system

import smtplib
from twilio.rest import Client

# Twilio configuration
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_number'
TO_PHONE_NUMBER = 'recipient_phone_number'

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'  # Change if using a different email provider
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_email_password'
TO_EMAIL_ADDRESS = 'recipient_email@example.com'

# Define critical thresholds
def check_thresholds(vital_signs):
    alerts = []
    
    # Check heart rate
    if vital_signs['heart_rate'] < 60 or vital_signs['heart_rate'] > 100:
        alerts.append("Critical Heart Rate Alert!")

    # Check blood pressure
    systolic, diastolic = map(int, vital_signs['blood_pressure'].split('/'))
    if systolic >= 140 or diastolic >= 90:
        alerts.append("Critical Blood Pressure Alert!")

    # Check creatinine levels
    if vital_signs['creatinine'] > 1.2:
        alerts.append("Critical Creatinine Level Alert!")
    
    return alerts

# Send SMS alert using Twilio
def send_sms(alert_message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=alert_message,
        from_=TWILIO_PHONE_NUMBER,
        to=TO_PHONE_NUMBER
    )
    print(f"SMS sent: {message.sid}")

# Send email alert using SMTP
def send_email(alert_message):
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(
            EMAIL_ADDRESS,
            TO_EMAIL_ADDRESS,
            f"Subject: Vital Signs Alert\n\n{alert_message}"
        )
        print("Email sent!")

# Main function to monitor vital signs
def monitor_vital_signs(vital_signs):
    alerts = check_thresholds(vital_signs)
    
    for alert in alerts:
        send_sms(alert)
        send_email(alert)

# Example incoming data (this would typically come from a database or API)
incoming_data = {
    'heart_rate': 105,
    'blood_pressure': '150/95',
    'creatinine': 1.5
}

# Monitor the incoming data
monitor_vital_signs(incoming_data)
