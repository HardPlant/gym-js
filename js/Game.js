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

    if(!this.isGameEnded()) {
        this.update();
    }
}

Game.prototype.playerTurn = function() {
    var players = this.entities.filter(function(node) {
        return !node.isEnemy;
    });

    players.attack();
};

Game.prototype.enemyTurn = function() {
    var enemyTurn = this.entities.filter(function(node) {
        return node.isEnemy;
    });
    
    enemyTurn.attack();
};
