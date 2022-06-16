import os
from dotenv import load_dotenv

from notifications_python_client.notifications import NotificationsAPIClient

load_dotenv('.env')
api_key = os.getenv('API_KEY')
template_id = os.getenv('TEMPLATE_ID')
email_address = os.getenv('EMAIL_TO')

feedback = "This is some feedback"
name = "Supplied name"
email = "supplied@email.com"

personalisation = {
    "feedback": feedback,
    "name": name,
    "email": email
}
notifications_client = NotificationsAPIClient(api_key)
response = notifications_client.send_email_notification(
    email_address=email_address,
    template_id=template_id,
    personalisation=personalisation
)
