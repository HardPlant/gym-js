function GameTile(id, x, y) {
    this.id = id;
    this.x = x;
    this.y = y;
}

function isTileTraversable(gameTile) {
    var passTable = {
        0 : true,
        1 : false
    };

    return passTable[gameTile.id];
}

