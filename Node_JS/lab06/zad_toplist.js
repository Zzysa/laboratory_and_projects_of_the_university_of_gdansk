const { lp3 } = require('./toplist');
const _ = require('lodash');

// // 1 task
// let songsQueen = _.filter(lp3, song => song.author == "Queen").reduce((acc, song) => {
//     acc.push(song.song)
//     return acc
// }, [])

// console.log(songsQueen)

// // 2 task
// let popularPingFloydSongs = _.filter(lp3, song => song.author == "Pink Floyd").reduce((acc, song) => {

//     if (song.change >= 10) {
//         acc.push(song.song)
//     }

//     return acc

// }, [])

// console.log(popularPingFloydSongs);

// console.dir(bandSongs, { depth: null });

// // 3 task
// const howMuchDelete = 5

// console.log(_.sortBy(lp3, [function(song) { return song.change; }]).slice(0, -howMuchDelete));

// // 4 task
// console.log(_.create(null, {'author' : lp3[0].author, "song" : lp3[0].song}))

// // 5 task
// let places = [-5, 4, 6, 15, 24, 31, 37]

// function songsPlaces(places) {
//     for (let i = 0; i < places.length - 1; i++) {
//         if (!_.isNumber(places[i])) {
//             return `Element "${places[i]}" isn't a number`
//         }
//     }

//     for (let j = 0; j < places.length - 1; j++) {
//         console.log(lp3[places[j] - 1])
//     }
// }

// console.log(songsPlaces(places))

// // 7 task 
// for (let i = 0; i < 10; i++) {
//     _.delay(() => {
//         console.log(lp3[i]);
//     }, 2000);
// }

// // 8 task
// let unPopularSongs = _.filter(lp3, song => song.change < 0).reduce((acc, song) => {

//     if (song.change < 0) {
//         acc.push(song.song)
//     }

//     return acc

// }, [])

// console.log(unPopularSongs);

// // 9 task
// let songNameAndInformation = _.reduce(lp3, function(acc, song) { 
//     acc[song.song] = song

//     return acc; 
//     }, {}); 

// console.log(songNameAndInformation);

// // 10 task 
// let bandSongs = (lp3.reduce((acc, song) => {
    
//     if (!acc[song.author]) {
//         acc[song.author] = [];
//     }

//     acc[song.author].push({ 
//         song: song.song,
//         place: song.place,
//     })

//     return acc

// }, []))
// console.log(bandSongs)

// // 11 task 
// let amountReferences = (lp3.reduce((acc, song) => {
    
//     if (!acc[song.author]) {
//         acc[song.author] = 0;
//     }

//     acc[song.author] = acc[song.author] + 1

//     return acc

// }, {}))

// console.log(amountReferences)

// // 12 task 
// let mostDownChange = _.sortBy(lp3, [function(song) { return song.change; }])[0];
// let mostUpChange = _.sortBy(lp3, [function(song) { return song.change; }])[lp3.length - 1];
// console.log(mostDownChange);
// console.log(mostUpChange);