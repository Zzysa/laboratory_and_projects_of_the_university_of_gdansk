const shoppingList = require('./shoppingList.js').shoppingList;

let grouped = shoppingList.reduce((acc, item) => {

    if (!acc[item.type]) {
        acc[item.type] = {};
    }

    acc[item.type][item.product] = {
        quantity: item.quantity,
        price: item.price,
        unit: item.unit
    };
    
    return acc;
}, {});

console.log(grouped);

let list = shoppingList.sort((a, b) => a.type.length - b.type.length).reduce((acc, item) => {

    if (acc.includes(item.type)) { 
        counter = counter + 1
        acc = acc + counter + '. ' + item.product + '\n'
    } else {
        counter = 1
        acc = '\n' + acc + '\n' + item.type + ':\n' + counter + '. ' + item.product + '\n'
    }

    return acc
}, '');

console.log(list);