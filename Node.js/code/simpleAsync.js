const additionAsync = (a, b, sampleCallback) => {
    setTimeout(() => {
        sampleCallback(a + b)
    }, 1000)
}

console.log('before');

additionAsync(1, 2, result => console.log(`Result -> ${result}`));

console.log('after');