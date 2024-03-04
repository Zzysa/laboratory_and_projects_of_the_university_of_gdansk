const person1 = { name: "Agata", age: 21 }
const person2 = { name: "Tomasz", age: 25 }
const person3 = { name: "Alicja", age: 31 }
const person4 = { name: "Jan", age: 20 }
people = []
sum = 0
more_average_age = []
less_average_age = []

people.push(person1)
people.push(person2)
people.push(person3)
people.push(person4)

for (let i = 0; i < people.length; i++) {
    sum += people[i].age
}

average_age = sum / 4

for (let j = 0; j < people.length; j++ ) {
    if (people[j].age > average_age) {
        more_average_age.push(people[j].name)
    } else {
        less_average_age.push(people[j].name)
    }
}

console.log(`Average age of people is ${average_age}`)
console.log(`Names people that have more than average age: ${more_average_age}`)
console.log(`Names people that have less than average age: ${less_average_age}`)
