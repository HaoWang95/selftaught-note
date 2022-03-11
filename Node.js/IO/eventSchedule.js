const fs = require('fs');

const asyncOperation = (callback) => {
    const start = Date.now();
    fs.readFile("./file.txt", callback);
    const end = Date.now();
    console.log(`async op has taken ${end - start}ms`)
}

const timeoutScheduled = Date.now();

setTimeout(() => {
    const delay = Date.now() - timeoutScheduled;

    console.log(`${delay}ms have passed since I was scheduled`);
}, 100);

asyncOperation(() => {
    console.log(`async operation`)
});