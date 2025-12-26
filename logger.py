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
# logger MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import logging
import logging.handlers
import os


# --------------------------------------------------
# logger factory
# --------------------------------------------------
class LoggerFactory:
    """
    Centralized logger configuration for Email Automation
    Tool
    """
    
    @staticmethod
    def get_logger(
        name: str = "email_automation_tool",
        level: int = logging.INFO,
        log_dir: str = "logs",
        log_file: str = "email_automation.log"
    ) -> logging.Logger:
        """
        Create or retrieve a configured logger instance
        """

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        logger = logging.getLogger(name)

        # Prevent duplicate handlers when re-imported
        if logger.handlers:
            return logger
        
        logger.setLevel(level)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | " +
            "%(name)s | %(message)s"
        )

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(level)

        # Rotating file handler (safe for long-running jobs)
        file_handler = logging.handlers.RotatingFileHandler(
            os.path.join(log_dir, log_file),
            maxBytes=5 * 1024 * 1024,   # 5 MB
            backupCount=5,
            encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        return logger
