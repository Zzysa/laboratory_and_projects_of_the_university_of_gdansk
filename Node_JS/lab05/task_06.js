const games = require('./games.js').games;

function links(array) {
    return array.filter((game, index) => {if (game.imageUrl !== '') {
        return game
    }}).filter((game, index) => {if (index < 4) {
        return game
    }}).map((game) => game.imageUrl)
}

const gamesLinks = links(games)

console.log(gamesLinks);