#!/usr/bin/node
import { students as data } from "./data.js";

/* Array Methods*/

/* forEach */
data.forEach((student, index) => {
    /*console.log(student.name);*/
})

/* map */
const result0 = data.map((student, index) => {
    return {
        /*Two ways to do the same taks*/
        /*name: student.name,
        lastname: student.lastname,
        age: student.age,
        course: student.course,*/
        ...student,
        fullname: `${student.name} ${student.lastname}`
    }
})

/* Filter */

const result1 = data.filter((element, index) => {
    return element.age > 22;
})

/* Reduce */

const result2 = data.reduce((previus, current, currentIndex) => {
    return previus + current.age;
}, 0);

/* sort */
//sort the array nased in the condiction
const result3 = data.sort((first, second) => {
    /*if (first.age < second.age) {
        return 1;
    }
    else {
        return -1;
    }*/
    /*first.age > second.age ? 1 : -1;*/
    /*return first.age - second.age;*/
})

/* find */

const result4 = data.find((student) => student.age === 20);
//return the fisrt object finded, or undefined


/* Some */
//return false or true if one object meets the condition
const result5 = data.some((student) => student.age > 25);


/* every*/
//True if all object meets the condiction, else: false
const result6 = data.every((student) => student.age >= 20);


/* Combine and destructure data */

const result = data.map(({ name, lastname, age }) => { //create a diferent array
    return {
        student: `${name} ${lastname}`,
        /*age: age*/
        age
    };
})
    .filter((student) => student.age > 20) //filert students older than 20
    .sort((a, b) => a.age - b.age) //sort minor to major
    .reduce((total, student) => total + student.age, 0);

console.log(result);