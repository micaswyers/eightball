import os

from flask import (
	Flask,
	request,
	redirect,
)
from twilio.twiml.messaging_response import MessagingResponse

from eightball import EightBall

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def respond_sms():
	"""Respond to incoming texts"""

	e = EightBall()
	resp = MessagingResponse()
	resp.message(e.shake())

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)
