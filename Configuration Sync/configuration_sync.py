import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

WEATHER_JSON_PATH = Path("Weather Registry Config Files/weather_spawn_chances.json")
weather_PATH = Path("Weather Registry Config Files/WeatherRegistry.cfg")

LUNAR_CONFIG_PATH = Path("Lunar Config Files/LunarConfigMoons.cfg")
SCRAP_PATH = Path("Lunar Config Files/scrap.json")
ENEMY_PATH = Path("Lunar Config Files/enemy.json")
POWER_PATH = Path("Lunar Config Files/power.json")

LINE_ENDING = "\r\n"

LUNAR_ENEMY_IGNORE_MOONS = []

LUNAR_SCRAP_IGNORE_MOONS = [
    "Trite",
    "Oldred",
    "Duckstroid14",
    "Filitrios",
    "Gratar",
    "Etern",
    "Dreck",
    "Release",
    "Motra",
    "Calist",
    "Alcatras",
    "FissionC",
    "Berunah",
    "Faith",
    "Crowd",
    "Lecaro",
    "Demetrica",
    "Gloom",
    "Roart",
    "Thalasso",
    "Cosmocos",
    "Hyx",
    "Atlantica",
    "Infernis",
    "Extort",
    "Desolation",
    "Narcotic",
    "Cubatres",
    "Empra",
    "Asteroid13",
    "Hyve",
    "Repress",
    "Utril",
    "Descent",
    "Acidir",
    "Junic",
    "Core",
    "Polarus",
    "Galetry",
]

def main():
    while True:
        choice = input(
            "Choose an action to perform:\n"
            "1: Weather Config\n"
            "2: Lunar Config\n"
            "3: Modify/View Ignore List\n"
            "4: Both (Lunar + Weather)\n"
            "5: Exit\n\n"
        )
        if choice == "1":
            weather_menu()
        elif choice == "2":
            lunar_config_menu()
        elif choice == "3":
            ignore_menu()
        elif choice == "4":
            update_lunar_config_enemy()
            update_lunar_config_power()
            update_lunar_config_scrap()
            update_weather()
        elif choice == "5":
            print("Exiting")
            break
        else:
            print("Invalid Selection")

def ignore_menu():
    while True:
            choice = input(
                "Choose an list you want view/modify:\n"
                "1: Scrap\n"
                "2: Enemy\n"
                "3: Back\n\n"
            )
            if choice == "1":
                ignore_scrap_menu()
            elif choice == "2":
                ignore_enemy_menu()
            elif choice == "3":
                print("Exiting")
                main()
            else:
                print("Invalid Selection")

def ignore_scrap_menu():
        while True:
            choice = input(
                "Choose an action:\n"
                "1: View\n"
                "2: Modify\n"
                "3: Return\n"
            )
            if choice == "1":
                view_enemy_ignore()
            elif choice == "2":
                modify_enemy_ignore()
            elif choice == "3":
                ignore_menu()
            else:
                print("Invalid Selection")

def view_enemy_ignore():
    print("\nList:")
    print(str(LUNAR_ENEMY_IGNORE_MOONS) + "\n\n")
    ignore_enemy_menu()

def ignore_enemy_menu():
        while True:
            choice = input(
                "Choose an action:\n"
                "1: View\n"
                "2: Modify\n"
                "3: Return\n"
            )
            if choice == "1":
                view_enemy_ignore()
            elif choice == "2":
                modify_enemy_ignore()
            elif choice == "3":
                ignore_menu()
            else:
                print("Invalid Selection")

def modify_enemy_ignore():
    while True:
        choice = input(
            "Choose an action:\n"
            "1: Add\n"
            "2: Remove\n"
            "3: Return\n"
            )
        if choice == "1":
            update_enemy_ignore(enemy_add = True)
        elif choice == "2":
            update_enemy_ignore(enemy_remove = True)
        elif choice == "3":
            ignore_enemy_menu()
        else:
            print("Invalid Selection")   

def modify_scrap_ignore():
    while True:
        choice = input(
            "Choose an action:\n"
            "1: Add\n"
            "2: Remove\n"
            "3: Return\n"
            )
        if choice == "1":
            update_scrap_ignore(scrap_add = True)
        elif choice == "2":
            update_scrap_ignore(scrap_remove = True)
        elif choice == "3":
            ignore_scrap_menu()
        else:
            print("Invalid Selection")        

def update_enemy_ignore(
        enemy_add: bool = False,
        enemy_remove: bool = False
):
    if enemy_add == True:
        while True:
            moon_to_add = input("Enter the name of the moon to add to the ignore list (or type 'exit' to return):\n\n")
            if moon_to_add.lower() == 'exit':
                break
            if moon_to_add not in LUNAR_ENEMY_IGNORE_MOONS:
                LUNAR_ENEMY_IGNORE_MOONS.append(moon_to_add)
                print(f"{moon_to_add} has been added to the ignore list.")
            else:
                print(f"{moon_to_add} is already in the ignore list.")
    elif enemy_remove == True:
        while True:
            moon_to_remove = input("Enter the name of the moon to remove from the ignore list (or type 'exit' to return):\n\n")
            if moon_to_remove.lower() == 'exit':
                break
            if moon_to_remove in LUNAR_ENEMY_IGNORE_MOONS:
                LUNAR_ENEMY_IGNORE_MOONS.remove(moon_to_remove)
                print(f"{moon_to_remove} has been removed from the ignore list.")
            else:
                print(f"{moon_to_remove} is not in the ignore list.")
    else:
        modify_enemy_ignore()

def update_scrap_ignore(
        scrap_add: bool = False,
        scrap_remove: bool = False
):
    if scrap_add == True:
        while True:
            moon_to_add = input("Enter the name of the moon to add to the ignore list (or type 'exit' to return):\n\n")
            if moon_to_add.lower() == 'exit':
                break
            if moon_to_add not in LUNAR_SCRAP_IGNORE_MOONS:
                LUNAR_SCRAP_IGNORE_MOONS.append(moon_to_add)
                print(f"{moon_to_add} has been added to the ignore list.")
            else:
                print(f"{moon_to_add} is already in the ignore list.")
    elif scrap_remove == True:
        while True:
            moon_to_remove = input("Enter the name of the moon to remove from the ignore list (or type 'exit' to return):\n\n")
            if moon_to_remove.lower() == 'exit':
                break
            if moon_to_remove in LUNAR_SCRAP_IGNORE_MOONS:
                LUNAR_SCRAP_IGNORE_MOONS.remove(moon_to_remove)
                print(f"{moon_to_remove} has been removed from the ignore list.")
            else:
                print(f"{moon_to_remove} is not in the ignore list.")
    else:
        modify_scrap_ignore()
    
def view_scrap_ignore():
    print("\nList:")
    print(str(LUNAR_SCRAP_IGNORE_MOONS) + "\n\n")
    ignore_scrap_menu()

def weather_menu():
    while True:
        choice = input(
            "Choose what to update in Weather Config:\n"
            "1: Spawn Chance\n"
            "2: Scrap Amount\n"
            "3: Scrap Value\n"
            "4: Clear WeatherToWeather Weights\n"
            "5: All\n"
            "6: Back\n\n"
        )
        if choice == "1":
            update_weather(update_spawn=True)
        elif choice == "2":
            update_weather(update_amount=True)
        elif choice == "3":
            update_weather(update_value=True)
        elif choice == "4":
            clear_weather_to_weather_weights()
        elif choice == "5":
            update_weather()
            clear_weather_to_weather_weights()
        elif choice == "6":
            break
        else:
            print("Invalid selection\n")

def clear_weather_to_weather_weights():
    with weather_PATH.open("r", encoding="utf-8", newline="") as f:
        lines = f.readlines()

    pattern = re.compile(r"^(\s*WeatherToWeather weights\s*=).*", re.IGNORECASE)
    for i, line in enumerate(lines):
        match = pattern.match(line)
        if match:
            newline = LINE_ENDING if line.endswith(LINE_ENDING) else "\n"
            lines[i] = match.group(1) + newline

    with weather_PATH.open("w", encoding="utf-8", newline="") as f:
        f.writelines(lines)
    print("Weather-to-weather weights cleared.\n")

def update_weather(
    update_spawn: bool = False,
    update_amount: bool = False,
    update_value: bool = False,
):
    with WEATHER_JSON_PATH.open("r", encoding="utf-8") as f:
        raw = json.load(f)

    weathers = {}
    containers = raw.get("WeatherSpawnChances", raw) if isinstance(raw, dict) else {}
    for section in containers.values():
        if isinstance(section, dict):
            for name, values in section.items():
                if isinstance(values, dict):
                    weathers[name] = {
                        "spawn_chance": values.get("SpawnChance"),
                        "scrap_amount": values.get("ScrapAmount"),
                        "scrap_value": values.get("ScrapValue"),
                    }

    with weather_PATH.open("r", encoding="utf-8", newline="") as f:
        lines = f.readlines()

    header_re = re.compile(r"\[(?:Modded|Vanilla|WeatherTweaks) Weather:\s*(.+?)\]")
    alias_map = {"DustClouds": "Dust Clouds", "SolarFlare": "Solar Flare"}
    spawn_re = re.compile(r"^\s*Level weights\s*=")
    amount_re = re.compile(r"^\s*Scrap amount multiplier\s*=")
    value_re = re.compile(r"^\s*Scrap value multiplier\s*=")

    i = 0
    while i < len(lines):
        match = header_re.match(lines[i])
        if match:
            weather = match.group(1).strip()
            lookup = alias_map.get(weather, weather)
            info = weathers.get(weather) or weathers.get(lookup)
            if info:
                j = i + 1
                while j < len(lines) and not header_re.match(lines[j]):
                    j += 1

                for idx in range(i + 1, j):
                    if update_spawn and spawn_re.match(lines[idx]) and info["spawn_chance"] is not None:
                        lines[idx] = f"Level weights = {info['spawn_chance']}{LINE_ENDING}"
                    if update_amount and amount_re.match(lines[idx]) and info["scrap_amount"] is not None:
                        lines[idx] = f"Scrap amount multiplier = {info['scrap_amount']}{LINE_ENDING}"
                    if update_value and value_re.match(lines[idx]) and info["scrap_value"] is not None:
                        lines[idx] = f"Scrap value multiplier = {info['scrap_value']}{LINE_ENDING}"
                i = j
        i += 1

    with weather_PATH.open("w", encoding="utf-8", newline="") as f:
        f.writelines(lines)

    print("Weather config updated.\n")

def lunar_config_menu():
    while True:
        choice = input(
            "Choose what to update in Lunar Config:\n"
            "1: Enemy List\n"
            "2: Power Level\n"
            "3: Scrap List\n"
            "4: All\n"
            "5: Back\n\n"
        )
        if choice == "1":
            update_lunar_config_enemy()
        elif choice == "2":
            update_lunar_config_power()
        elif choice == "3":
            update_lunar_config_scrap()
        elif choice == "4":
            update_lunar_config_enemy()
            update_lunar_config_power()
            update_lunar_config_scrap()
        elif choice == "5":
            break
        else:
            print("Invalid selection")

def update_lunar_config_enemy():
    with ENEMY_PATH.open("r", encoding="utf-8") as f:
        moons = json.load(f, object_pairs_hook=OrderedDict)

    with LUNAR_CONFIG_PATH.open("r", encoding="utf-8", newline="") as f:
        lines = f.readlines()

    updated_lines = lines[:]
    enemy_re = re.compile(r"^\s*Spawnable Interior Enemies\s*=\s*(.+)$")

    ignored_enemy_moons = []

    for moon in LUNAR_ENEMY_IGNORE_MOONS:
        ignored_enemy_moons.append(normalize_lookup_key(moon))

    i = 0
    while i < len(lines):    
        moon = extract_lunar_moon_name(lines[i])
        if normalize_lookup_key(moon) in ignored_enemy_moons:
            print(f"Skipping {moon}; configured to ignore enemy replacement.")
            i += 1
            continue            
        if moon is not None and moon in moons:
            enemy_list = moons[moon]
            j = i + 1
            while j < len(lines) and extract_lunar_moon_name(lines[j]) is None:
                if enemy_re.match(lines[j]):
                    newline = LINE_ENDING if lines[j].endswith(LINE_ENDING) else "\n"
                    updated_lines[j] = f"Spawnable Interior Enemies = {enemy_list}{newline}"
                    break
                j += 1
            i = j
        i += 1

    with LUNAR_CONFIG_PATH.open("w", encoding="utf-8", newline="") as f:
        f.writelines(updated_lines)
    print("Lunar config enemy lists updated.\n")

def extract_lunar_moon_name():
    line = line.strip()
    if not line.startswith("[") or not line.endswith("]"):
        return None

    inner = line[1:-1].strip()

    if inner.lower().startswith("lll -"):
        inner = inner[5:].strip()

    inner = re.split(r"\s*\(", inner, 1)[0]
    inner = re.split(r"\s*-\s*", inner, 1)[0]

    return inner.strip() or None

def update_lunar_config_scrap():
    with SCRAP_PATH.open("r", encoding="utf-8") as f:
        scrap_by_risk_raw = json.load(f, object_pairs_hook=OrderedDict)

    with LUNAR_CONFIG_PATH.open("r", encoding="utf-8", newline="") as f:
        lines = f.readlines()

    updated_lines = lines[:]

    risk_re = re.compile(r"^\s*Risk Level\s*=\s*(.*?)\s*$", re.IGNORECASE)

    scrap_re = re.compile(
        r"^(\s*(?:"
        r"Spawnable Scrap"
        r"|Spawnable Scrap List"
        r"|Spawnable Scrap Items"
        r"|Scrap Spawning List"
        r"|Scrap List"
        r"|Scrap"
        r")\s*=\s*).*$",
        re.IGNORECASE,
    )

    updated_count = 0
    ignored_scrap_moons = []

    for moon in LUNAR_SCRAP_IGNORE_MOONS:
        ignored_scrap_moons.append(normalize_lookup_key(moon))

    i = 0
    while i < len(lines):
        moon = extract_lunar_moon_name(lines[i])

        if moon is None:
            i += 1
            continue

        section_start = i
        section_end = i + 1

        while section_end < len(lines) and extract_lunar_moon_name(lines[section_end]) is None:
            section_end += 1

        if normalize_lookup_key(moon) in ignored_scrap_moons:
            print(f"Skipping {moon}; configured to ignore scrap replacement.")
            i = section_end
            continue

        risk_level = None
        scrap_line_index = None

        for idx in range(section_start + 1, section_end):
            risk_match = risk_re.match(lines[idx])
            if risk_match:
                risk_level = clean_cfg_value(risk_match.group(1))

            scrap_match = scrap_re.match(lines[idx])
            if scrap_match:
                scrap_line_index = idx

        if not risk_level:
            print(f"Skipping {moon}; no Risk Level found.")
            i = section_end
            continue

        resolved_json_key = resolve_risk_level_to_json_key(risk_level, scrap_by_risk_raw)

        if resolved_json_key is None:
            print(f"Skipping {moon}; risk level '{risk_level}' could not be matched.")
            i = section_end
            continue

        scrap_list = scrap_by_risk_raw[resolved_json_key]

        if scrap_line_index is None:
            print(f"Skipping {moon}; no scrap list line found.")
            i = section_end
            continue

        scrap_match = scrap_re.match(lines[scrap_line_index])
        newline = LINE_ENDING if lines[scrap_line_index].endswith(LINE_ENDING) else "\n"
        formatted_scrap_list = format_scrap_value(scrap_list)

        updated_lines[scrap_line_index] = scrap_match.group(1) + formatted_scrap_list + newline
        updated_count += 1

        if normalize_lookup_key(risk_level) != normalize_lookup_key(resolved_json_key):
            print(f"{moon}: risk level '{risk_level}' matched to '{resolved_json_key}'.")

        i = section_end

    with LUNAR_CONFIG_PATH.open("w", encoding="utf-8", newline="") as f:
        f.writelines(updated_lines)

    print(f"Lunar config scrap lists updated by risk level. Updated {updated_count} moons.\n")

def update_lunar_config_power():
    with POWER_PATH.open("r", encoding="utf-8") as f:
        powers = json.load(f, object_pairs_hook=OrderedDict)

    with LUNAR_CONFIG_PATH.open("r", encoding="utf-8", newline="") as f:
        lines = f.readlines()

    updated_lines = lines[:]
    power_re = re.compile(r"^\s*Max Interior Power\s*=\s*(.+)$")

    i = 0
    while i < len(lines):
        moon = extract_lunar_moon_name(lines[i])
        if moon is not None and moon in powers:
            power = powers[moon]
            j = i + 1
            while j < len(lines) and extract_lunar_moon_name(lines[j]) is None:
                if power_re.match(lines[j]):
                    newline = LINE_ENDING if lines[j].endswith(LINE_ENDING) else "\n"
                    updated_lines[j] = f"Max Interior Power = {power}{newline}"
                    break
                j += 1
            i = j
        i += 1

    with LUNAR_CONFIG_PATH.open("w", encoding="utf-8", newline="") as f:
        f.writelines(updated_lines)

    print("Lunar config power levels updated.\n")

def normalize_lookup_key(value: str):
    return re.sub(r"\s+", " ", str(value).strip()).casefold()

def clean_cfg_value():
    value = value.strip()
    value = re.split(r"\s*[#;]", value, 1)[0].strip()
    value = value.strip('"').strip("'").strip()
    return value

def resolve_risk_level_to_json_key(risk_level: str, scrap_by_risk_raw: dict):
    normalized_to_original_key = {
        normalize_lookup_key(key): key
        for key in scrap_by_risk_raw.keys()
    }

def format_scrap_value(value):
    if isinstance(value, list):
        return ",".join(str(item) for item in value)

    if isinstance(value, dict):
        return ",".join(f"{key}:{val}" for key, val in value.items())

    return str(value)

main()