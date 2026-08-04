function exportWeatherConfigJSON() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Weather Configuration");

  function round(value) {
    return Math.round(Number(value) * 100) / 100;
  }

  function buildNormalWeather(namesRange, spawnRange, amountRange, valueRange) {
    const names = sheet.getRange(namesRange).getValues()[0];
    const spawns = sheet.getRange(spawnRange).getValues()[0];
    const amounts = sheet.getRange(amountRange).getValues()[0];
    const values = sheet.getRange(valueRange).getValues()[0];

    const section = {};
    for (let i = 0; i < names.length; i++) {
      const name = names[i];
      const spawn = spawns[i];
      const amount = amounts[i];
      const value = values[i];
      if (name && spawn) {
        section[name] = {
          SpawnChance: String(spawn),
          ScrapAmount: round(amount),
          ScrapValue: round(value)
        };
      }
    }
    return section;
  }

  function buildComboWeather(nameRanges, spawnRanges, amountRange, valueRange) {
    const names1 = sheet.getRange(nameRanges[0]).getValues()[0];
    const names2 = sheet.getRange(nameRanges[1]).getValues()[0];
    const spawns1 = sheet.getRange(spawnRanges[0]).getValues()[0];
    const spawns2 = sheet.getRange(spawnRanges[1]).getValues()[0];

    const allNames = names1.concat(names2);
    const allSpawns = spawns1.concat(spawns2);
    const amounts = sheet.getRange(amountRange).getValues()[0];
    const values = sheet.getRange(valueRange).getValues()[0];

    const section = {};
    for (let i = 0; i < allNames.length; i++) {
      const name = allNames[i];
      const spawn = allSpawns[i];
      const amount = amounts[i];
      const value = values[i];
      if (name && spawn) {
        section[name] = {
          SpawnChance: String(spawn),
          ScrapAmount: round(amount),
          ScrapValue: round(value)
        };
      }
    }
    return section;
  }

  const output = {
    // NormalWeather updated: columns C to T, spawn row shifted to 202 after the insert at 164
    NormalWeather: buildNormalWeather("C1:T1", "C202:T202", "C63:T63", "C64:T64"),

    // CombinationAndTransitioningWeather updated: name rows and spawn rows each shifted by one
    CombinationAndTransitioningWeather: buildComboWeather(
      ["C203:T203", "C205:T205"], // names
      ["C204:T204", "C206:T206"], // spawns
      "S63:AY63",                 // amounts
      "S64:AY64"                  // values
    )
  };

  const pretty = JSON.stringify(output, null, 2);
  const file = DriveApp.createFile("weather_spawn_chances.json", pretty, MimeType.PLAIN_TEXT);
  Logger.log("File created: " + file.getUrl());
}
