function foo(a,b) {
    console.log(a);
    console.log(b);
    return a+b
}

//匿名函数
let func =function (a,b){
    console.log(a);
    console.log(b);
    return a+b
};

function f2() {
    console.log('总共有'+arguments.length+'个参数');
    let ret = 0;
    for (let i=0;i<arguments.length;i++){
        ret+=arguments[i]
    }
    return ret
}
console.log(f2(1,2,3,4,5,6,7));



(function (a,b) {
    console.log('立即执行函数');
    console.log(a+b);
})(11,22);

console.log('=======================================');
let ret = foo(11,22);
console.log('a+b=',ret);

let c = func(11,22);
console.log(c);