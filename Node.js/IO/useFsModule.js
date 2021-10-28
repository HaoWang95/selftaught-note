'use strict';
const fs = require('fs');
const path = require('path');
const os = require('os');

console.log(process.argv[0], process.argv[1]);

const currentDir = path.join(process.cwd(), 'file.txt');
console.log(currentDir);

const useOs = () => {
    console.log(`Your os type: ${os.type()}`);
    console.log(`Your os total mem: ${os.totalmem()}`);
    console.log(`Your node.js platform: ${os.platform()}`);
    console.log(`Your os free mem: ${os.freemem()}`);
}

const fileMetaData = (filePath) => {
    fs.stat(filePath, (err, stats) => {
        if(err){
            console.log(`err at fileMetaData -> ${err}`);
            return err;
        }
        console.log(stats);
    });
}

const clearAndWriteFileSync = (filePath, content) => {
    try {
        fs.writeFileSync(filePath, content, 'utf-8');   
    } catch (error) {
        console.log(`err at clearAndWriteFileSync -> ${error}`);
        return error;
    }
}

const clearAndWriteFileAsync = (filePath, content) => {
    fs.writeFile(filePath, content, 'utf-8', (err) => {
        if(err){
            console.log(`err at clearAndWriteFileAync -> ${err}`);
            return err;
        }
    });
}

const appendAndWriteFileSync = (filePath, content) => {
    try{
        fs.appendFileSync(filePath, content, 'utf-8');
    }catch(err){
        console.error(`err at appendAndWriteFile -> ${err}`);
        return err;
    }
}

const appendAndWriteFileAsync = (filePath, content) => {
    fs.appendFile(filePath, content, 'utf-8', (err) => {
        if(err){
            console.error(`err at appendAndWriteFileSync -> ${err}`);
        }
    })
}


const readAndUpdateSync = (filePath, newContent, callback) => {
    try{
        const fileContent = fs.readFileSync(filePath, 'utf-8');
        console.log(`File content:\n ${fileContent}`);
        fs.writeSync(filePath, newContent);
        callback();
    }catch(err){
        console.error(`err at readAndUpdateSync -> ${err}`);
        return err;
    }
}


const readAndUpdateAsync = (filePath, newContent, callback) => {
    fs.readFile(filePath, 'utf-8', (err, content) => {
        if(err){
            console.error(`err at readAndUpdateAsync ${err}`);
            return err;
        }
        console.log(`File content:\n ${content}`);
        fs.writeFile(filePath, newContent, (err) => {
            if(err){
                console.error(`err at writeFile in readAndUpdateAsync ${err}`);
                return err;
            }
        })
    });
}


const onSuccess = () => {console.log('Completed!')}

useOs();
fileMetaData(currentDir);

