
function max_of_2(a,b)
{
    if (a > b)
    {
        return a;
    }
    
    else if (a = b)
    {
    console.log("Both are equal");
    }
    else 
    {
        return b;
    }
}
console.log("This func prints greatest of 2 numbers :");
let a = 10;
let b = 33;
let result = max_of_2(a,b);
// console.log("The Greatest of" + a + "and" + b + "is" + result);
console.log(result);