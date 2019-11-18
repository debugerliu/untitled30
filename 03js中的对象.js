let person = {'name':'小强','age':30};
console.log(person);
//单独取
console.log(person.age);
console.log(person.name);
//循环取
for (let i in person){
    console.log(i);
    console.log(person[i])
}