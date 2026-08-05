# Thunderstore Modpack Development Tools

![GitHub stars](https://img.shields.io/github/stars/unluckyjori/Thunderstore-Modpack-Development-Tools?style=for-the-badge&logo=github) ![GitHub forks](https://img.shields.io/github/forks/unluckyjori/Thunderstore-Modpack-Development-Tools?style=for-the-badge&logo=github) ![GitHub issues](https://img.shields.io/github/issues/unluckyjori/Thunderstore-Modpack-Development-Tools?style=for-the-badge&logo=github) ![Last commit](https://img.shields.io/github/last-commit/unluckyjori/Thunderstore-Modpack-Development-Tools?style=for-the-badge&logo=github) ![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

## Introductory Information

The Thunderstore Modpack Development Tools repository provides utilities designed to increase the productivity of Thunderstore modpack maintence. It removes the manual workload of individually updating package dependencies and uploading large modpacks. This collection of utilities is intended for modpack creators and maintainers who want to automate repetitive configuration edits and package publishing tasks.

## Features

- **Configuration Sync** — Transfers configuration settings directly from the data spreadsheet into [Lunar Config](https://thunderstore.io/c/lethal-company/p/Crafty/LunarConfig/) and [Weather Registry](https://thunderstore.io/c/lethal-company/p/mrov/WeatherRegistry/) .cfg files.
- **Package Uploads & Updates** — Automates package uploading and dependency updates for modpack distributions.

## Quick Start

```bash

# 1. Clone the repository
git clone https://github.com/unluckyjori/Thunderstore-Modpack-Development-Tools.git

# 2. Open .bat files

or

# 2. Run python files
python configuration_sync.py

or

python updater.py

```

## Project Structure

```
.
├── Configuration Sync
│   ├── Google Script Code - Script used to extract data from spreadsheet onto .json files
│   │   ├── Interior Enemy Power Level.gs
│   │   ├── Moon Interior Enemy.gs
│   │   └── Weather.gs
│   ├── Lunar Config Files
│   │   ├── LunarConfigMoons.cfg
│   │   └── name_value_lists.json
│   ├── Weather Registry Config Files
│   │   ├── WeatherRegistry.cfg
│   │   └── weather_spawn_chances.json
│   └── sync_enemies.py
│
├── Updater
│   ├── Core
│   │   ├── icon.png
│   │   └── manifest.json
│   ├── Cosmetic
│   │   ├── icon.png
│   │   └── manifest.json
│   ├── Cosmos
│   │   ├── icon.png
│   │   └── manifest.json
│   ├── Extra
│   │   ├── icon.png
│   │   └── manifest.json
│   ├── Main
│   │   ├── CHANGELOG.md
│   │   ├── icon.png
│   │   └── manifest.json
│   ├── mod_manager.py
│   ├── package_list.txt
│   └── settings.json
├─── Updater.bat
└── Configuration Sync.bat
```

## Contributors

Thanks to everyone who has contributed to this project:

<p align="left">
<a href="https://github.com/unluckyjori" title="unluckyjori"><img src="https://avatars.githubusercontent.com/u/83521035?v=4&s=64" width="64" height="64" alt="unluckyjori" style="border-radius:50%" /></a>
</p>

## Contributing

Contributions are welcome! 

Please follow the existing code style and ensure new behavior is functional through tests.

## License

This project is licensed under the **MIT** License.
