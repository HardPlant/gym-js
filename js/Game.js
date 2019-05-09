assert(Node !== undefined);

function Game(width, height){
    this.width = width || this.width;
    this.height = height || this.height;
};

Game.prototype = {
    entities: [],
    width: 10,
    height: 10,
    turn: 0,
    
    playerTurn: function(){},
    enemyTurn: function(){},
    
    update: function(){},
    isGameEnded: function() {}
};

Game.prototype.init = function() {
    var player = new Node;
}

Game.prototype.update = function() {
    this.playerTurn();
    this.enemyTurn();
}

Game.prototype.playerTurn = function() {
    var players = this.entities.filter(function(node) {
        return !(node.isEnemy());
    });

    players.forEach(function(node) {
        node.controller.move();
    });

};

Game.prototype.enemyTurn = function() {
    var enemies = this.entities.filter(function(node) {
        return node.isEnemy();
    });
    
    enemies.forEach(function(node) {
        node.controller.move();
    });
};

Game.prototype.isUnaccepableMove = function(node, x, y) {
    var isUnacceptable = false;

    this.entities.forEach(function(item) {
        if (item === node) return;

        if (item.x === x && item.y === y) {
            isUnacceptable = true;
        }
    });

    return isUnacceptable;
};

Game.prototype.validateMove = function(node) {
    if (node.x < 0) node.x = 0;
    if (node.y < 0) node.y = 0;

    if (this.width <= node.x) node.x = this.width - 1;
    if (this.height <= node.y) node.y = this.height - 1;
};

Game.prototype.moveNode = function(node, x, y) {
    if (this.isUnaccepableMove(node, x, y)) {
        return false;
    } else {
        node.x += x;
        node.y += y;
        
        this.validateMove(node);
    }
}