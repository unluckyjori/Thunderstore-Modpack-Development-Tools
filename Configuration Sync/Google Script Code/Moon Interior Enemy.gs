function exportReadableJSONWithSpacing() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Interior Enemy Configuration");
  const data = sheet.getRange("A145:B155").getValues(); # Range for selection (Change if you add more rows/columns)
  let lines = [];

  lines.push("{");

  const entries = [];

  for (let i = 0; i < data.length; i++) {
    const name = data[i][0];
    const value = data[i][1];
    if (name && value) {
      const line = `  "${name}": "${value}"`;
      entries.push(line);
    }
  }

  // Add commas and blank lines between entries
  for (let i = 0; i < entries.length; i++) {
    const isLast = i === entries.length - 1;
    lines.push(entries[i] + (isLast ? "" : ","));
    if (!isLast) lines.push(""); // Add blank line between entries
  }

  lines.push("}");

  const output = lines.join("\n");
  const file = DriveApp.createFile("moons_readable_spaced.json", output, MimeType.PLAIN_TEXT);
  Logger.log("File created: " + file.getUrl());
}