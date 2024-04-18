"use strict";

// ==============================================
// Przeanalizuj poniższe fragmenty kodu i zastanów się, co zostanie wypisane na ekranie.
// ==============================================

//#region EXAMPLES

// Przykład 1

const arr = ["Dog", "Cat", "Rabbit", "Parrot", "Monkey"];
const [dog, cat, rabbit, parrot, monkey] = arr;

// console.log(dog, rabbit); // Dog Rabbit

// Przykład 2

const book = {
  title: "Mistrz i Małgorzata",
  author: "Michaił Bułhakow",
  year: 1967
};

// a

const { title, author, year } = book;

// console.log(title); // Mistrz i Małgorzata
// console.log(author); // Michaił Bułhakow

// b

const {
  title: titleOfBook,
  author: authorOfBook,
  year: yearOfBook
} = book;

// console.log(titleOfBook); // Mistrz i Małgorzata
// console.log(authorOfBook); // Michaił Bułhakow

// c

const { title: onlyTitle, ...bookWithoutTitle } = book;

// console.log(onlyTitle); // Mistrz i Małgorzata
// console.log(bookWithoutTitle); // { author: 'Michaił Bułhakow', year: 1967 }


//#endregion EXAMPLES


// ==============================================
// ZADANIE
// ==============================================

// Wykorzystując wszystkie informacje zawarte powyżej stwórz obiekt zawierający poniższe pola:
// country: USA
// title: Zielona Mila
// director: Frank Darabont
// genre: Dramat

const movie1 = {
  country: "USA",
  title: "Zielona Mila",
  director: "Frank Darabont",
  genre: "Dramat"
};

// Następnie wykorzystując zabieg przedstawiony w powyższych przykładach zmodyfikuj obiekt tak, aby po wyświetleniu obiektu dostać następujący output:

const {
  country: movieCountry,
  genre: movieGenre,
  ...newMovie1
} = movie1;

// console.log(newMovie1);
// Oczekiwany output: { title: 'Zielona Mila', director: 'Frank Darabont' }
