"""Parses the arguments for the `send_email_alert` module."""

import argparse


def args_parser():
    """Parses the arguments for the `send_email_alert` module."""

    argsParser = argparse.ArgumentParser(
        description='Sends an email notifiying recipient that pinging the \
            server has failed.'
    )
    argsParser.add_argument(
        '-c',
        '--config-file',
        action='store',
        help='Path to JSON config file containing the email settings.'
    )
    argsParser.add_argument(
        '-f',
        '--mail_from',
        action='store',
        help='Email from'
    )
    argsParser.add_argument(
        '-t',
        '--mail_to',
        action='store',
        help='Email to'
    )
    argsParser.add_argument(
        '-i',
        '--host',
        action='store',
        help='Email host'
    )
    argsParser.add_argument(
        '-j',
        '--port',
        action='store',
        help='Email port'
    )
    argsParser.add_argument(
        '-u',
        '--user',
        action='store',
        help='User'
    )
    argsParser.add_argument(
        '-p',
        '--password',
        action='store',
        help='Password'
    )
    argsParser.add_argument(
        '-s',
        '--subject',
        action='store',
        help='Email subject'
    )
    argsParser.add_argument(
        '-a',
        '--msg-prefix',
        action='store',
        help='Email body prefix'
    )
    argsParser.add_argument(
        '-z',
        '--msg-suffix',
        action='store',
        help='Email body suffix'
    )

    return argsParser.parse_args()
