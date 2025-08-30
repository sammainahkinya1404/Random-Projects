const person={
    names:"Samson Kinyanjui",
    age:27,
    state:"alive"

}

// destructure object person ans using numeral literals
const{names}=person;
console.log(`The Name is : ${names}`)
const{age}=person;
console.log(`The age is: ${age}`)

let message=(age>35)? "You are no longer a young person" : "You are still a young man";
console.log(`${message}`)

const functionSum=(a,b,c)=>{
    const sum=a+b/c;
    return sum;
}

export default functionSum