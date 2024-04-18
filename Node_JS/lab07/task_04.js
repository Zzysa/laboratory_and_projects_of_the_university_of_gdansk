class Student {
    constructor(name, age, major) {
        this.name = name;
        this.age = age;
        this.major = major;
        this.courses = [];
    }

    intorduce() {
        return `Student's name is ${this.name}, student's age is ${this.age} years old and student's major is ${this.major}.`
    }

    enroll(course) {
        console.log(`You have been enrolled in ${course} course.`);
        this.courses.push(course);
    }

    displayCourses() {
        console.log("Your cources are: ")
        if (this.courses.length !== 0) {
            this.courses.forEach((course) => console.log(course))
        } else {
            return `You are not enrolled in any courses`
        }
    }

    dropCourse(course) {
        if (this.courses.includes(course)) {
            console.log(`You have been dropped from ${course} course.`);
            this.courses = this.courses.filter((c) => c !== course)
        } else {
            console.log(`You are not enrolled in ${course} course`)
        }
    }
}

const student1 = new Student("John", 22, "Computer Science");
console.log(student1.intorduce());

student1.displayCourses()
student1.enroll("Mathematics")
student1.displayCourses()
student1.enroll("Physics")
student1.displayCourses()
student1.dropCourse("Physics")
student1.displayCourses()
student1.dropCourse("Phylosophy")
student1.displayCourses()


