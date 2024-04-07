function detectChanges(obj1, obj2) {
  const keys = Object.keys(obj1)
  const amountKeys = keys.length
  let differences = []
  
  for (let i = 0; i < amountKeys; i++) {
    if (obj1[keys[i]] instanceof Array) {
      if (obj1[keys[i]].flat !== obj2[keys[i]].flat) {
        let temp = [keys[i], obj2[keys[i]]]
        differences.push(temp)
      }
    } else {
      if (obj1[keys[i]] !== obj2[keys[i]]) {
        let temp = [keys[i], obj2[keys[i]]]
        differences.push(temp)
      }
    }
  }
  return differences
}

const object1 = {
    id: 2,
    name: 'Przyjaciele',
    startYear: 1994,
    endYear: 2004,
    type: ["Komedia"],
    seasons: 10
  };
  
  const object2 = {
    id: 2,
    name: 'Przyjaciele edytowany',
    startYear: 1994,
    endYear: 2010,
    type: ["Komedia"],
    seasons: 10
  };

  const object3 = {
    value: { field: "old value" },
    name: 'test'
  }
  
  const object4 = {
    value: { field: "new value" },
    name: 'test'
  }
  
  
  console.log(detectChanges(object3, object4)); // => [ [ 'name', 'Przyjaciele edytowany' ], [ 'endYear', 2010 ] ]
  