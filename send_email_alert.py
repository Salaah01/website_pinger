#!/usr/bin/python3

"""Send an email alert saying that the bluish pink server is down."""

import sys
import os
import json
import ssl
import smtplib
from datetime import datetime
from collections import namedtuple
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmailAlert:
    def __init__(
        self,
        configFile: str = None,
        mailFrom: str = None,
        mailTo: str = None,
        host: str = None,
        port: int = None,
        user: str = None,
        password: str = None,
        subject: str = '',
        messagePrefix: str = '',
        messageSuffix: str = '',
    ):
        """
        Sets the paramaters for sending the email and creates the email to be
        sent.

        Args:
            configFile - (str) Path to a JSON file containing the email params.
            mailFrom - (str) The email account from which the email should be
                sent from.
            mailTo - (str) Recipient email address.
            host - (str) Email host.
            port - (int) Email port.
            user - (str) Email User.
            password - (str) Email password.
            subject - (str) Email subject.
            messagePrefix - (str) Text to be prepended to the to email body.
            messageSuffix - (str) Text to be appended to the email body.
        """
        self._Parms = self._set_params(configFile, mailFrom, mailTo, host,
                                       port, user, password)

        self._msg = self._set_msg(subject, messagePrefix, messageSuffix)

    @staticmethod
    def _set_params(
        configFile: str = None,
        mailFrom: str = None,
        mailTo: str = None,
        host: str = None,
        port: int = None,
        user: str = None,
        password: str = None
    ) -> namedtuple:
        """Sets the email connection parameters including the email address of
        the recipient.

        Args:
            configFile - (str) Path to a JSON file containing the email params.
            mailFrom - (str) The email account from which the email should be
                sent from.
            mailTo - (str) Recipient email address.
            host - (str) Email host.
            port - (int) Email port.
            user - (str) Email User.
            password - (str) Email password.

        Returns:
            namedtuple - Collection of the email connection parameters.
        """
        connParams = {}
        if configFile:
            with open(configFile, 'r') as jsonFile:
                connParams = json.load(jsonFile)

        if mailFrom:
            connParams['FROM'] = mailFrom
        if mailTo:
            connParams['TO'] = mailTo
        if host:
            connParams['HOST'] = host
        if port:
            connParams['PORT'] = port
        if user:
            connParams['USER'] = user
        if password:
            connParams['PASSWORD'] = password

        return namedtuple('connectionParams', connParams)(**connParams)

    def _set_msg(self, subject: str, messagePrefix: str, messageSuffix: str):
        """Creates the message object to be sent.

        Args:
            subject - (str) Email subject.
            messagePrefix - (str) Text to be prepended to the to email body.
            messageSuffix - (str) Text to be appended to the email body.
        """
        msg = MIMEMultipart("alternative")
        msg['Subject'] = subject
        msg['From'] = self.get_params().FROM
        msg['To'] = self.get_params().TO
        msg.attach(
            MIMEText(
                f'PINGING THE SERVER FAILED AT {datetime.now()}',
                'plain')
        )
        msgBody = f"""
            {messagePrefix}
            Pinging the server failed at {datetime.now()}
            {messageSuffix}
            """
        msg.attach(MIMEText(msgBody))

        return msg

    def send_email(self):
        """Creates a connection to the mailing server and sends email."""
        context = ssl.create_default_context()
        params = self.get_params()
        with smtplib.SMTP(params.HOST, params.PORT) as server:
            server.starttls(context=context)
            server.login(params.USER, params.PASSWORD)
            server.sendmail(params.FROM, params.TO, self.get_msg().as_string())

    def get_params(self):
        """Getter for retrieving the email parameters."""
        return self._Parms

    def get_msg(self):
        """Getter for retrieving the message object."""
        return self._msg


if __name__ == '__main__':

    # Parse the arguments and send the email.
    from args_parser import args_parser
    args = args_parser()
    SendEmailAlert(args.config_file, args.mail_from, args.mail_to, args.host,
                   args.port, args.user, args.password, args.subject,
                   args.msg_prefix, args.msg_suffix).send_email()
