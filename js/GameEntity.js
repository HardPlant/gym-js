var nodeFn = {};
var type_limit = 10000;

function GameEntity(id, x, y) {
    this.id = id;
    this.x = x;
    this.y = y;
    this.controller = {};
}

GameEntity.prototype = {
    id: 1,
    x: 0,
    y: 0,
    range: 1,
    hp: 1,
    moveCount: 0,
    attackCount: 0,
    isEnemy: function() {
        return this.id >= type_limit;
    }
};

nodeFn.attack = function (game, node) {
    _attack(game, node, node.range, node.x, node.y);

    function _attack(game, node, range, x, y) {
        if (x < 0 || y < 0) return;
        if (x > game.width || y > game.height) return;

        if (isNodeExists()) {
            if (node.isEnemy ^ game.entities[x][y]) {
                game.entities[x][y] = 0;
            }
        }

        _attack(game, range-1, x-1, y);
        _attack(game, range-1, x, y-1);
        _attack(game, range-1, x+1, y);
        _attack(game, range-1, x, y+1);
    }
};

nodeFn.getRandom = function(isFoe) {

}

nodeFn.makeFoe = function(node) {
    if (!node.isEnemy()) {
        node.id += type_limit;
    }
}

nodeFn.isExist = function(game, x, y) {

}

nodeFn.RandomController = function(game, node) {

    function nextMove() {
        return {
            x: Math.random() < 0.5 ? -1 : 1,
            y: Math.random() < 0.5 ? -1 : 1
        }
    };

    node.controller = {
        move: function() {
            var move = nextMove();
        
            game.moveNode(node, move.x, move.y);
        }
    };

    return node.controller;
}

nodeFn.ProgrammedController = function(game, node, program) {
    var programTurn = 0;

    function nextMove() {

        result = {
            x: program[programTurn].x,
            y: program[programTurn].y
        }
        programTurn++;

        return result;
    };

    node.controller.move = function() {
            var move = nextMove();
        
            game.moveNode(node, move.x, move.y);
    };

    return node.controller;
}