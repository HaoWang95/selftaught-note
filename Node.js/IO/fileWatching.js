const fs = require('fs');
const path = require('path');

const watch = (filePath) => {
    fs.watchFile(filePath, (current, previous) => {
        console.log(`${filePath} previos update: ${previous.mtime}`)
        console.log(`${filePath} updated at ${current.mtime}`);
    })
}

const file = path.join(process.cwd(), 'file.txt');

watch(file);