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
# config MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import os
from dotenv import load_dotenv

load_dotenv()

# # --------------------------------------------------
# # env loader (smtplib only)
# # --------------------------------------------------
# def load_env(path=".env"):
#     """
#     Load environment variables from a .env file
#     without using third-part libraries
#     """
#     if not os.path.exists(path):
#         return
    
#     with open(path, "r", encoding="utf-8") as f:
#         for line in f:
#             line = line.strip()

#             # Skip comments and empty lines
#             if not line or line.startswith("#"):
#                 continue

#             if "=" not in line:
#                 continue

#             key, value = line.split("=", 1)

#             # Do not override existing environment varaibles
#             os.environ.setdefault(
#                 key.strip(), value.strip()
#             )

# # Load .env at import time
# load_env()


# --------------------------------------------------
# email config
# --------------------------------------------------
class EmailConfig:
    SMTP_HOST = os.getenv("SMTP_HOST", "smtp.example.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    USERNAME = os.getenv("SMTP_USERNAME", "")
    PASSWORD = os.getenv("SMTP_PASSWORD", "")
    USE_TLS = os.getenv(
        "USE_TLS", "true"
    ).lower() == "true"
    DEFAULT_SENDER = os.getenv(
        "DEFAULT_SENDER", "noreply@example.com"
    )
