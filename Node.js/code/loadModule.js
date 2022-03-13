const fs = require(fs);

function loadModule(filename, module, require){
    const wrappedSrc = `(function(module, exports, require){
        ${fs.readFileSync(filename, 'utf-8')}        
    })(module, module.exports, require)`
    eval(wrappedSrc);
}

function req(moduleName){
    console.log(`Required module: ${moduleName}`);
    const id = require.resolve(moduleName);
    if(require.cache[id]){
        return require.cache[id].exports;
    }

    const module = {
        exports: {},
        id
    }

    require.cache[id] = module;
    loadModule(id, module, require)
    return module.exports;
}