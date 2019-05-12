function Game(width, height){
    this.width = width || this.width;
    this.height = height || this.height;
};

Game.prototype = {
    tiles: [],
    entities: [],
    width: 10,
    height: 10,
    turn: 0,

    update: function(){},
    isGameEnded: function() {}
};

Game.prototype.init = function(tileData, entityData) {
    for(var y = 0; y < this.height; y++) {
        var currentRow = [];

        for (var x = 0; x < this.width; x++) {
            var tileId = tileData[y*this.height + x];

            currentRow.push(new GameTile(
                tileId, x, y, 
                isTileTraversable(tileId)
            ));
        }   
        this.tiles.push(currentRow); 
    }

    entityData.forEach(function(entity) {
        this.entities.push(
            new GameEntity(
                entity.id, entity.x, entity.y)
        );
    });
}

Game.prototype.update = function() {
    var players = this.entities.filter(function(node) {
        return !(node.isEnemy());
    });
    var enemies = this.entities.filter(function(node) {
        return node.isEnemy();
    });

    this.processTurn(players);

    this.processTurn(enemies);
}

Game.prototype.processTurn = function(nodes) {

    nodes.forEach(function(node) {
        node.controller.move();
    });

    this.turn++;
};

Game.prototype.isUnaccepableMove = function(node, x, y) {
    var isUnacceptable = false;

    if (!isTileTraversable(this.tiles[x][y])) return false;

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

Game.prototype.getTileIndexByXY = function(x, y) {
    return y * this.height + x;
}

Game.prototype.replaceTile = function(x, y, id) {
    var tile = this.tiles[x][y];
    
    tile.id = id;

    console.log(this.tiles);
}
