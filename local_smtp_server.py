# --------------------------------------------------
# Local SMTP Debug Server
# Prints all received emails to console
# --------------------------------------------------

import asyncio
from aiosmtpd.controller import Controller


class DebugHandler:
    async def handle_DATA(self, server, session, envelope):
        print("\n" + "=" * 60)
        print("📩 New Email Received")
        print("=" * 60)
        print(f"From   : {envelope.mail_from}")
        print(f"To     : {envelope.rcpt_tos}")
        print("Content:")
        print(envelope.content.decode("utf-8", errors="replace"))
        print("=" * 60 + "\n")
        return "250 Message accepted for delivery"


def main():
    controller = Controller(
        DebugHandler(),
        hostname="localhost",
        port=1025
    )
    controller.start()
    print("🚀 Local SMTP Server running at localhost:1025")
    print("Press CTRL+C to stop")

    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print("\n🛑 SMTP Server stopped")
    finally:
        controller.stop()


if __name__ == "__main__":
    main()
