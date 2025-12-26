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
# test_email_model MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import unittest
from email_builder import EmailMessageModel


# --------------------------------------------------
# test email model
# --------------------------------------------------
class TestEmailModel(unittest.TestCase):
    
    def test_empty_recipients(self):
        with self.assertRaises(ValueError):
            EmailMessageModel("Subject", [])
        
    def test_valid_email(self):
        email = EmailMessageModel("Hi", ["a@b.com"])
        self.assertEqual(email.subject, "Hi")


if __name__ == "__main__":
    unittest.main()
