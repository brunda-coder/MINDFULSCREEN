#!/usr/bin/env python3
"""
Etherea Living OS - Launcher
Handles entry point execution and clean initialization.
"""

import asyncio
import sys
from main import EthereaOS

async def run():
    """Start the Etherea Operating System."""
    os_instance = EthereaOS()

    await os_instance.initialize()
    await os_instance.main_loop()

def start():
    """Sync wrapper for environments that require a normal function."""
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("\n🛑 Etherea shutdown requested. Exiting gracefully...")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start()
