function createNameValueJsonFile() {
  const SHEET_NAME = 'scrap';
  const START_COLUMN = 3; // C
  const END_COLUMN = 17;  // Q

  const HEADER_ROW = 1;
  const VALUE_ROW = 42; # Value row (Change if you add more rows)

  const OUTPUT_FILE_NAME = 'name_value_lists.json';

  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Scrap");

  if (!sheet) {
    throw new Error('Sheet named "' + SHEET_NAME + '" was not found.');
  }

  const numColumns = END_COLUMN - START_COLUMN + 1;

  const headers = sheet
    .getRange(HEADER_ROW, START_COLUMN, 1, numColumns)
    .getDisplayValues()[0];

  const values = sheet
    .getRange(VALUE_ROW, START_COLUMN, 1, numColumns)
    .getDisplayValues()[0];

  const output = {};

  headers.forEach((header, columnIndex) => {
    if (header === '') return;

    output[header] = values[columnIndex];
  });

  const json = JSON.stringify(output, null, 2);

  const file = DriveApp.createFile(
    OUTPUT_FILE_NAME,
    json,
    MimeType.PLAIN_TEXT
  );

  Logger.log('Created file: ' + file.getUrl());
}

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('Export Lists')
    .addItem('Create name/value JSON file', 'createNameValueJsonFile')
    .addToUi();
}