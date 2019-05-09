
Node = function(x, y) {
    this.x = x;
    this.y = y;
}
Node.prototype = {
    x: 0,
    y: 0,
    range: 1,
    hp: 1,
    isEnemy: false
};
Node.prototype.attack = function() {
    _attack(game, this, this.range, this.x, this.y);

    function _attack(game, node, range, x, y) {
        if (x < 0 || y < 0) return;
        if (x > game.width || y > game.height) return;

        if (typeof(game.entities[x][y]) !== undefined) {
            if (this.isEnemy ^ game.entities[x][y]) {
                game.entities[x][y] = 0;
            }
        }

        _attack(game, range-1, x-1, y);
        _attack(game, range-1, x, y-1);
        _attack(game, range-1, x+1, y);
        _attack(game, range-1, x, y+1);
    }
};