(function() {
    this.include = function(jsfile) {
        var fs = require("fs");
        if (!fs.existsSync(`${jsfile}`)) {
         
            console.error("Non-exist");
            return;
        }
        file = fs.readFileSync(`${jsfile}`) + '';
        
        return file;
    }
}).call(this);