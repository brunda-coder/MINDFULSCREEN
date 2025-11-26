import os

# Create everything INSIDE the current GitHub repository
base = "Etherea Living OS"

folders = [
    "core",
    "ai_engine",
    "voice_system",
    "templates",
    "themes",
    "avatars",
    "ui",
    "data",
    "database",
    "security",
    "cloud_sync",
    "collaboration",
    "analytics",
    "media",
    "camera",
    "chat_system",
    "modules",
    "os_integration",
    "tasks_and_automation",
    "assistants",
    "plugins",
    "extensions",
    "user_settings",
    "customization_engine"
]

files = [
    "main.py",
    "launcher.py",
    "readme.md",
    "app_config.json",
    "requirements.txt"
]

# Create base folder inside repo
os.makedirs(base, exist_ok=True)

# Create subfolders & __init__.py
for f in folders:
    path = os.path.join(base, f)
    os.makedirs(path, exist_ok=True)

    # Python package initializer
    init_file = os.path.join(path, "__init__.py")
    with open(init_file, "w") as file:
        file.write(f"# Init for {f}\n")

# Create top-level files
for f in files:
    file_path = os.path.join(base, f)
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write("")

print("✨ GitHub project structure created successfully vruuuuuuuuuuu! 🚀")
