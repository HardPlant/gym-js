function GameTile(id, x, y, isPassable) {
    this.id = id;
    this.x = x;
    this.y = y;
    this.isPassable = isPassable;
}

function isTileTraversable(id) {
    var passTable = {
        0 : true,
        1 : false
    };

    return passTable[id];
}