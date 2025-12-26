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
# sender MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import smtplib
import ssl
from logger import LoggerFactory

logger = LoggerFactory.get_logger()


# --------------------------------------------------
# email sender
# --------------------------------------------------
class EmailSender:
    def __init__(self, config):
        self.config = config

        if (not self.config.SMTP_HOST 
            or self.config.SMTP_HOST == "smtp.example.com"
        ):
            raise ValueError(
                "Invalid SMTP_HOST configuration"
            )

        if (self.config.SMTP_HOST != "localhost"
            and (not self.config.USERNAME 
            or not self.config.PASSWORD)):
            raise ValueError(
                "SMTP credentials are missing"
            )
    
    def send(self, message):
        logger.info("Connecting to SMTP server")
        context = ssl.create_default_context()

        with smtplib.SMTP(
            self.config.SMTP_HOST,
            self.config.SMTP_PORT
        ) as server:
            if self.config.USE_TLS:
                server.starttls(context=context)
        
            # Login only if credentials provided
            if (self.config.USERNAME 
                and self.config.PASSWORD):
                server.login(
                    self.config.USERNAME,
                    self.config.PASSWORD
                )
            
            server.send_message(message)
        logger.info("Email sent successfully")
