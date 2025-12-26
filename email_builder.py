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
# email_builder MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------


# --------------------------------------------------
# email message model
# --------------------------------------------------
class EmailMessageModel:
    def __init__(self, subject, recipients,
            body_text="", body_html=None,
            attachments=None):
            if not recipients:
                raise ValueError(
                    "Recipient list cannot be empty"
                )
            
            self.subject = subject
            self.recipients = recipients
            self.body_text = body_text
            self.body_html = body_html
            self.attachments = attachments or []
