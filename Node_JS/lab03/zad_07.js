// sortWords(['pies', 'kot', 'chomik', 'królik', 'wiewiórka']) => ['kot', 'pies', 'chomik', 'królik', 'wiewiórka']

function sortWords(arr) {
    for (var i = 0; i < arr.length; i++) {
        for (var j = 0; j < (arr.length - i - 1); j++) {
            if (arr[j].length > arr[j + 1].length) {

                var temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            }

            if (arr[j].length === arr[j + 1].length) {
                array1 = [arr[j], arr[j+1]].sort()
                arr[j] = array1[0]
                arr[j + 1] = array1[1]
            }
        }

    return arr
    }
}

console.log(sortWords(['pies', 'kot', 'królik', 'chomik', 'wiewiórka']))