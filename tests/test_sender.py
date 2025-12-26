# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the email_automation_tool Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# email_automation_tool - Send bulk emails or scheduled emails
#                   Skills: smtplib, MIME types, security
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# test_sender MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import unittest
from unittest.mock import patch
from sender import EmailSender
from config import EmailConfig
from email.mime.text import MIMEText


# --------------------------------------------------
# test email sender
# --------------------------------------------------
class TestEmailSender(unittest.TestCase):

    @patch("smtplib.SMTP")
    def test_send_email(self, mock_smtp):
        sender = EmailSender(EmailConfig)
        msg = MIMEText("Hello")
        sender.send(msg)
        self.assertTrue(mock_smtp.called)


if __name__ == "__main__":
    unittest.main()
