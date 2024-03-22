// Input: 
// [
//     { id: 'a', name: 'Ala' },
//     { id: 'b', name: 'Tomek' },
//     { id: 'c', name: 'Jan' }
//   ]
  
//   Output: 
//   [
//     { a: { id: 'a', name: 'Ala' } },
//     { b: { id: 'b', name: 'Tomek' } },
//     { c: { id: 'c', name: 'Jan' } }
//   ]
  

const persons = [
    { id: 'a', name: 'Ala' },
    { id: 'b', name: 'Tomek' },
    { id: 'c', name: 'Jan' }
]

const idPersons = (array) => {return array.map((element) => ({[element.id]: element}))}
console.log(idPersons(persons))
  
