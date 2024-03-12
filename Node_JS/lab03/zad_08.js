const persons = [
    { name: 'Jan', age: 22 },
    { name: 'Grzegorz', age: 19 },
    { name: 'Halina', age: null },
    { name: 'Agata', age: 24 },
    { name: 'Krzysztof', age: 40 },
    { name: 'Adam', age: 29 }
]

// function yearsOld(persons) {
//     return persons.reduce((acc, currPerson) => {
//         if (currPerson.age !== null) return [...acc, currPerson];
//         else return acc;
//     }, [])
// }
// const personsWithAge = yearsOld(persons)

function sortPerson(persons) {
    const sortPersonsNames = []
    const personsWithAge = persons.filter((person) => person.age !== null);
    const sortPersonsWithAge = personsWithAge.sort((a, b) => a.age - b.age)
    sortPersonsWithAge.forEach((person) => sortPersonsNames.push(person.name));
    return sortPersonsNames
}

console.log(sortPerson(persons));