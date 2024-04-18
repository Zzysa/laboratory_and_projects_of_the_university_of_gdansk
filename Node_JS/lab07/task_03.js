class Book {
    constructor(title, author, year) {
        this.title = title;
        this.author = author;
        this.year = year;
    }

    printDetails() {
        return `Author of ${this.title} is ${this.author}. Year of publication: ${this.year}`;
    }

    isRecent() {
        if (this.year >= 2014) {
            return true;
        } else {
            return false;
        }
    }

    isByAuthor(author) {
        if (this.author === author) {
            return true;
        } else {
            return false;
        }
    }
}

const book1 = new Book("Mistrz i Małgorzata", "Michaił Bułhakow", 1967);
console.log(book1.isRecent());
console.log(book1.isByAuthor("Michaił Bułhakow"));
console.log(book1.printDetails());

const book2 = new Book("Nowa Książka", "Ktoś", 2015);
console.log(book2.isRecent());
console.log(book2.isByAuthor("Carlos Ungar"));
console.log(book2.printDetails());
