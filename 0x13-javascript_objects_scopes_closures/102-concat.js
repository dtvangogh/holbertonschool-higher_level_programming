#!/usr/bin/node
if (process.argv.length === 5) {
  const fs = require('fs');
  const file1 = fs.readFileSync(process.argv[2]).toString();
  const file2 = fs.readFileSync(process.argv[3]).toString();
  fs.writeFile(process.argv[4], file1 + file2, function (err) {
    if (err) throw err;
  });
}
