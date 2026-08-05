# Thunderstore Modpack Development Tools

![GitHub stars](https://img.shields.io/github/stars/unluckyjori/Thunderstore-Modpack-Development-Tools?style=for-the-badge&logo=github) ![GitHub forks](https://img.shields.io/github/forks/unluckyjori/Thunderstore-Modpack-Development-Tools?style=for-the-badge&logo=github) ![GitHub issues](https://img.shields.io/github/issues/unluckyjori/Thunderstore-Modpack-Development-Tools?style=for-the-badge&logo=github) ![Last commit](https://img.shields.io/github/last-commit/unluckyjori/Thunderstore-Modpack-Development-Tools?style=for-the-badge&logo=github) ![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

## Purpose

The Thunderstore Modpack Development Tools repository provides utilities designed to increase the productivity of Thunderstore modpack maintence. It removes the manual workload of individually updating package dependencies and uploading large modpacks. This collection of utilities is intended for modpack creators and maintainers who want to automate repetitive configuration edits and package publishing tasks. Used in famous and popular modpack [Lethal Enhanced](https://thunderstore.io/c/lethal-company/p/lethal_coder/Lethal_Enhanced_Party_Edition/).

## Features

- **Configuration Sync** — Transfers configuration settings directly from the data spreadsheet into [Lunar Config](https://thunderstore.io/c/lethal-company/p/Crafty/LunarConfig/) and [Weather Registry](https://thunderstore.io/c/lethal-company/p/mrov/WeatherRegistry/) .cfg files.
- **Package Uploads & Updates** — Automates package uploading and dependency updates for modpack distributions.
- **Data Spread Sheet** - Required for configuration sync, make a copy of the [sheet](https://docs.google.com/spreadsheets/d/1i4IFDg8eMr53LOaFw8gsh40l4-GBJ-McjStiVx8AAHo/edit?usp=sharing)

## How to use

```bash

# 1. Clone the repository
git clone https://github.com/unluckyjori/Thunderstore-Modpack-Development-Tools.git

# 2a. Open .bat files
Easy way to run scripts

# 2b. Run python files
Alternatively, you can just run the python scripts

python configuration_sync.py
python updater.py

```

## Project Structure

```python
├── Configuration Sync
│   │ 
│   ├── Google Script Code # Script used to extract data from spreadsheet onto .json files
│   │   ├── Interior Enemy Power Level.gs
│   │   └── Moon Interior Enemy.gs
│   │ 
│   ├── Lunar Config Files
│   │   ├── LunarConfigMoons.cfg
│   │   └── name_value_lists.json
│   │ 
│   ├── Weather Registry Config Files
│   │   ├── WeatherRegistry.cfg
│   │   └── weather_spawn_chances.json
│   │ 
│   └── sync_enemies.py # Script File
│
├── Updater
│   ├── Core
│   │   ├── icon.png
│   │   └── manifest.json
│   │   
│   ├── Cosmetic
│   │   ├── icon.png
│   │   └── manifest.json
│   │ 
│   ├── Cosmos
│   │   ├── icon.png
│   │   └── manifest.json
│   │ 
│   ├── Extra
│   │   ├── icon.png
│   │   └── manifest.json
│   │ 
│   ├── Main
│   │   ├── CHANGELOG.md
│   │   ├── icon.png
│   │   └── manifest.json
│   │ 
│   ├── mod_manager.py # Script File
│   ├── package_list.txt
│   └── settings.json
│
├─── Updater.bat
└── Configuration Sync.bat
```

## Credit

### Thanks to everyone who has contributed to this project:

[Unluckyjori](https://github.com/unluckyjori)
- Mainly developed by me

[SSSteveexe](https://github.com/SSStevexe)
- Some code is derived from the original configuration sync and updater

EasyIdle
- Coded formulas on sheet

## Contributing

Contributions are welcome! 

Please follow the existing code style and ensure new behavior is functional through tests.

## License

This project is licensed under the **MIT** License.
