{
    "app_name": "Etherea Living OS",
    "version": "1.0.0",
    "environment": "production",
    "debug_mode": false,

    "paths": {
        "data_dir": "data/",
        "database_dir": "database/",
        "ui_dir": "ui/",
        "templates_dir": "templates/",
        "themes_dir": "themes/",
        "avatars_dir": "avatars/",
        "ai_engine_dir": "ai_engine/",
        "logs_dir": "analytics/logs/",
        "cache_dir": "data/cache/",
        "plugins_dir": "plugins/",
        "extensions_dir": "extensions/",
        "modules_dir": "modules/"
    },

    "security": {
        "enable_encryption": true,
        "jwt_secret_key": "CHANGE_THIS_TO_A_REAL_SECRET_KEY",
        "allowed_devices": [],
        "firewall_enabled": true
    },

    "cloud_sync": {
        "enabled": true,
        "sync_interval": 30,
        "provider": "mindfulscreen_cloud",
        "backup_enabled": true
    },

    "ui": {
        "theme": "default",
        "animations_enabled": true,
        "language": "en-IN"
    },

    "system": {
        "auto_update": true,
        "check_updates_interval": 1440,
        "performance_mode": "balanced"
    },

    "voice_system": {
        "enabled": true,
        "default_voice": "etherea_default",
        "wake_word": "Etherea"
    },

    "assistants": {
        "enabled": true,
        "default_assistant": "core_assistant"
    }
}
