const { kill } = require("process");

const myModule = (() => {
    const moduleMethodA = () => {
        console.log('this is module method A');
    };

    const moduleMethodB = () => {
        console.log('this is module method B');
    };

    const exported = {
        publicA: () => {
            console.log('this is public a')
        }
    }
    return exported;
})();

console.log(myModule);
console.log(myModule.a)
console.log(myModule.b);
console.log(myModule.publicA)
const publicA = myModule.publicA
publicA()

