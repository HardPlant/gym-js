var {Given, When, Then} = require("cucumber");
var jsload = require("../../jsload.js");
var assert = require("assert");

eval(jsload.include("js/GameEntity.js"));
eval(jsload.include("js/Game.js"));

var game;
var lastNode;

function isAlly(entity) {
    if (entity === "아군") return true;
    else return false;
}

Given('{string} * {string} 게임판이 초기화된다', function (x, y) {
    game = new Game(Number(x), Number(y));
    assert.notEqual(game, undefined);
});

Given('{string}이 {string}, {string} 위치에 배치된다', function (entity, x, y) {
    assert.notEqual(game.entities, undefined);
    var id = 0;
    lastNode = new GameEntity(id, Number(x), Number(y));

    if (!isAlly(entity)) {
        nodeFn.makeFoe(lastNode);
    }

    game.entities.push(lastNode);
});

Given('{string}은 랜덤하게 움직인다', function (node) {
    var node = lastNode;

    assert.notEqual(node.controller, undefined);
    
    assert.strictEqual(typeof(node.controller.move), "function");
});

When('턴이 진행되면', function () {
    assert.notEqual(game, undefined);
    assert.equal(game.entities.length, 2);
    
    game.update();
});

Then('{string}이 {string}, {string} 위치에 있다', function (type, x, y) {
    var nodes;

    if (isAlly(type)) {
        nodes = game.entities.filter(entity => {
            return !entity.isEnemy();
        });
    } else {
        nodes = game.entities.filter(entity => {
            return entity.isEnemy();
        });
    }
    assert.equal(nodes.length, 1);
    assert.equal(nodes[0].x,Number(x));
    assert.equal(nodes[0].y,Number(y));
});

Given('아군은 x:1로 움직인다', function () {
    var program = [
        {x:1, y:0},
        {x:1, y:0},
        {x:1, y:0},
    ]
    nodeFn.ProgrammedController(game, game.entities[0], program);
});

Given('적군은 y:-1 움직인다', function () {
    var program = [
        {x:0, y:-1},
        {x:0, y:-1},
        {x:0, y:-1},
    ]
    nodeFn.ProgrammedController(game, game.entities[1], program);
});

Then('{string} 턴이 경과한다', function (turn) {
    assert.equal(game.turn, Number(turn));
});