(function(jsfile) {
    var fs = require("fs");
    assert(fs.existsSync(`${jsfile}.js`));
    file = fs.readFileSync(`${jsfile}.js`) + '';
    eval(file);

}).call(this);