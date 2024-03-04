const person1 = { name: "Agata", age: 21 }
const person2 = { name: "Tomasz", age: 25 }
const person3 = { name: "Alicja", age: 31 }
const person4 = { name: "Jan", age: 20 }
people = []
sum = 0

people.push(person1)
people.push(person2)
people.push(person3)
people.push(person4)

console.log(people)

for (let i = 0; i < 4; i++) {
    sum += people[i].age
}

console.log(`${sum} total years old have the listed people`)
console.log(`${sum / 4} average age the listed people`)