#!/usr/bin/env python3
"""
Etherea Living OS - Minimal, Clean, Fully Working Launcher
"""

import asyncio
import signal
import sys

# Core Modules
from core.system_manager import SystemManager
from ai_engine.emotion_processor import EmotionProcessor
from user_settings.user_manager import UserManager
from security.auth_manager import AuthManager


class EthereaOS:
    def __init__(self):
        self.running = False
        self.tasks = []

        self.system_manager = SystemManager()
        self.emotion_processor = EmotionProcessor()
        self.user_manager = UserManager()
        self.auth_manager = AuthManager()

    async def initialize(self):
        print("🌱 Initializing Etherea Living OS...")

        # Authentication
        authenticated = await self.auth_manager.authenticate()
        if not authenticated:
            print("❌ Authentication failed.")
            sys.exit(1)

        # User Profile
        profile = self.user_manager.load_user_profile()
        print(f"👋 Welcome back, {profile.get('name', 'Creator')}!")

        # Start systems
        await self.system_manager.start_services()
        await self.emotion_processor.initialize()

        print("✅ All systems online. Etherea is alive! 💫")

    async def main_loop(self):
        self.running = True
        print("🚀 Entering Etherea runtime loop...")

        while self.running:
            try:
                # Status snapshot
                system_status = self.system_manager.get_status()
                emotion_state = await self.emotion_processor.get_state()

                # Adaptive behavior
                await self.system_manager.update_environment(
                    emotion=emotion_state,
                    system_info=system_status
                )

                await asyncio.sleep(1)

            except asyncio.CancelledError:
                break
            except Exception as e:
                print(f"⚠️ Runtime error: {e}")
                await asyncio.sleep(1)

    async def shutdown(self):
        print("\n🛑 Shutting down Etherea gracefully...")
        await self.system_manager.stop_services()
        await self.emotion_processor.shutdown()
        print("✨ Shutdown complete. See you next time!")


async def run():
    os = EthereaOS()

    await os.initialize()

    loop = asyncio.get_running_loop()
    stop_event = asyncio.Event()

    def stop_signal(*args):
        os.running = False
        stop_event.set()

    # Signal handling
    loop.add_signal_handler(signal.SIGINT, stop_signal)
    loop.add_signal_handler(signal.SIGTERM, stop_signal)

    main_task = asyncio.create_task(os.main_loop())

    await stop_event.wait()
    main_task.cancel()

    await os.shutdown()


if __name__ == "__main__":
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("\n🛑 Forced exit")
