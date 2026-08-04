function exportInteriorEnemyPowerLevels() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Interior Enemy Configuration");

  const moons = sheet.getRange("A145:A277").getValues().flat();
  const risks = sheet.getRange("C145:C277").getValues().flat();

  const riskMap = {
    "D-": 4,
    "D": 5,
    "D+": 6,
    "C-": 7,
    "C": 8,
    "C+": 9,
    "B-": 10,
    "B": 11,
    "B+": 12,
    "A-": 13,
    "A": 14,
    "A+": 16,
    "S-": 18,
    "S": 20,
    "S+": 22
  };

  const result = {};

  for (let i = 0; i < moons.length; i++) {
    const moon = moons[i];
    const risk = risks[i];
    const power = riskMap[risk];
    if (moon && power !== undefined) {
      result[moon] = power;
    }
  }

  const json = JSON.stringify(result, null, 2);
  const file = DriveApp.createFile("interior_enemy_power_levels.json", json, MimeType.PLAIN_TEXT);
  Logger.log("✅ File created: " + file.getUrl());
}
