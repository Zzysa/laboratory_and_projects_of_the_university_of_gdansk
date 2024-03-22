const wishlist = [
    { name: 'Czajnik', netto: 100 },
    { name: 'Lodówka', netto: 2730 },
    { name: 'Mikrofalówka', netto: 940 },
    { name: 'Mikser', netto: 120 },
    { name: 'Piekarnik', netto: 3100 },
    { name: 'Zmywarka', netto: 2400 },
    { name: 'Toster', netto: 260 }
]

function allPrices(array) {
    return array.map((object) => object.netto)
}

console.log(allPrices(wishlist))



function nameWithNetto(array, func) {
    return array.map((element) => (func(element)))
}

const namesWithPrices = nameWithNetto(wishlist, (object) => object.name + ": " + object.netto);
console.log(namesWithPrices); 



function filterPrice(array, func) {
    return array.filter((element) => func(element))
}

const filteredArray = filterPrice(wishlist, (object) => object.netto < 500)
console.log(filteredArray);

  