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
# mime_builder MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


# --------------------------------------------------
# mime builder
# --------------------------------------------------
class MimeBuilder:
    @staticmethod
    def build(sender, email_model):
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = ",".join(email_model.recipients)
        msg["Subject"] = email_model.subject

        msg.attach(
            MIMEText(email_model.body_text, "plain")
        )

        if email_model.body_html:
            msg.attach(
                MIMEText(email_model.body_html, "html")
            )
        
        for path in email_model.attachments:
            if not os.path.exists(path):
                raise FileNotFoundError(path)
            
            with open(path, "rb") as f:
                part = MIMEBase(
                    "application", "octet-stream"
                )
                part.set_payload(f.read())
            
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                'attachment: filename=' +
                f'"{os.path.basename(path)}"'
            )
            msg.attach(part)
        
        return msg
