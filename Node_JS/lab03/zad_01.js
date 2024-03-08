'use strict';

// Poniższe fragmenty kodu zostały zakomentowane w celu utrzymania porządku. 
// Odkomentowuj je na bieżąco i zapisuj odpowiedzi w komentarzu. 
// Ostatecznie przed wrzuceniem pliku na repozytorium zakomentowane powinny być tylko dodane odpowiedzi i fragmenty kodu powodujące ewentualne błędy.

// ========================= Zadanie 1 =========================
// Co wypisze funkcja dla każdego z poniższych przypadków?
// Wyjaśnij, dlaczego w niektórych przypadkach wyniki różnią się.

// ========================== UWAGA =============================
// Zapis 
// (impression) ? console.log('A') : console.log('B');
// Jest skróconą wersją:
// if (impression) {
//     console.log('A');
// } else {
//     console.log('B');
// }
// ==============================================================

function isEquals(val1, val2) {
    (val1 == val2) ? console.log('A') : console.log('B');
    (val1 === val2) ? console.log('C') : console.log('D');
}

isEquals(2, '2'); // A D
// == sprawdza czy są równe znaczenia 
// === sprawdza czy są równe znaczenia i typ danych
isEquals(null, undefined); // A D
isEquals(undefined, NaN); // B D
isEquals(['a', 'b', 'c'], ['b', 'c', 'd']); // B D
// nie sprawdzanie wartości tablic, ale gdzie są te tablicy znajdują się w pamięci
isEquals(0, ''); // A D
isEquals('0', ''); // B D
isEquals(+0, -0); // A C
isEquals(0, false); // A D
// porównanie z boolean
isEquals(0, 'false'); // B D
// porównanie z string
isEquals([1, 2], '1,2'); // A D

// Co zwróci każde z poniższych wyrażen?

!!false; // false
!!true; // true
!!undefined; // false, bo !undefined to true, a !!undefined to false
!!null; // false bo !null to true, a !!null to false

// ========================= Zadanie 2 =========================
// Jaki będzie efekt działania poniższego fragmentu kodu?
// Wyjaśnij wynik

const person = {
    firstName: 'Jan',
    lastName: 'Kowalski'
}

console.log(person);
// person = {}; BŁĄD, bo person jest konstantą
console.log(person);

// ========================= Zadanie 3 =========================
// Co zostanie wyświetlone na ekranie?
// Wyjaśnij wynik

let number = 3;
console.log(number); {
    let number = 4;
    console.log(number);
}
console.log(number);

// 3 bo number = 3 i to zmiena globalna
// 4 bo number = 4 i to zmiena lokalna
// 3 bo number = 3 i to zmniena globalna 

// ========================= Zadanie 4 =========================
// Czym się różnią poniższe dwa fragmenty kodu?
// Jak działa operator '...'?

const arr = [1, 2];
const newArr1 = [arr, 3, 4]; // dodajemy arr jako element
console.log(newArr1);
const newArr2 = [...arr, 3, 4]; // spłaszczamy array i dodajemy kazdy element oddzielnie 
console.log(newArr2);


// Co zostanie wyświetlone na ekranie?
// Wyjaśnij wynik

const word = 'javascript';
const arrWord = [...word]; // ...string rozdziela string na chary 
console.log(arrWord); 

// ========================= Zadanie 5 =========================
// Zapoznaj się z kodem poniżej. Jaki będzie jego wynik i dlaczego?

var hello = 'Hello world!';
var result = hello / 2;

console.log(result); // resultat z dzielenia string na int będzie nie błąd, a not a number

console.log(Number.isNaN(result)); // czy jest NaN? Tak, dlatego true
console.log(Number.isNaN(hello)); // czy jest "Hello world!" NaN? Nie, dlatego false

// ========================= Zadanie 6 =========================
// Zapoznaj się z przykładami poniżej. Jaka jest różnica między var a let/const?

if (true) {
    var a = 2; // globalna zmienna, dlatego będzie błąd 
}
console.log(a);

// if (true) {
//     const b = 2; to jest loclana zmienna
// }
// console.log(b);

// -------

// Dla sprawdzenia działania obu poniższych pętli odkomentuj najpierw jedną, później drugą.
// Jaki będzie rezultat, jeśli obie pętle bedą odkomentowane jednocześnie. Wyjaśnij dlaczego.

for (var i = 0; i < 10; i++) {
    console.log(i);
}
console.log(i);

// for (let i = 0; i < 10; i++) {
//     console.log(i);
// }
// console.log(i);

// tylko pierwszy działa 
// tylko drugi nie działa bo zmienna i jest lokalna
// pierwszy i drugi działa, bo w pierwszej pętle i jest globalna zmienna 

// -------

var test = "var1";
var test = "var2";

// let test2 = "let1";  już stworzyli zmieną test 2
// let test2 = "let2"; nie możemy stworzyć drugi raz

// ========================= Zadanie 7 =========================
// Do czego używany jest 'use strict' w pierwszej linijce skryptu?

// 'use strict'; włącza tryb ścisły w JavaScript.
// W trybie ścisłym JavaScript obsługuje kod bardziej rygorystycznie i zgłasza błędy tam, gdzie byłyby ostrzeżenia bez trybu ścisłego.
// Naprzykład zmienne muszą być zadeklarowane za pomocą var, let lub const, w przeciwnym razie wystąpi błąd.