// Team Casa Blanca -- Sam Cowan, Ameer Alnasser
// SoftDev pd2
// K28 -- Manipulating the DOM
// 2023-04-17
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO"); //Gets printed before you do anything

var i = "hello"; //typing i or j in the terminal will return these
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) { //adds 30 to input
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy', //Can do o["name"] in dev console to return
          age : 1024, //needs quotes
          items : [10, 20, 30, 40], //o["items"][1] returns 20
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) { //o["func"](7) runs the function
            return x+30;
          }
        };


var addItem = function(text) { //adds item to list on webpage
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) { //removes item index n from list
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() { //makes the first and last thing on the list red
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() { //makes the first red, all else blue
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
function fib(n){
  if(n === 0){
    return 0;
  }
  else if (n < 3) {
    return 1;
  }
  return fib(n-1)+fib(n-2);
}

function fact(n){
  if(n < 2){
    return 1;
  }
  return (n*fact(n-1));
}

function gcd(a,b){
  if (a > b){
    if (a % b === 0){
      return b;
    }
    return gcd(b, a%b);
  }
  if (a < b){
    if (b % a === 0){
      return a;
    }
    return gcd(a, b%a);
  }
  return a;
}

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (a, b) => {
  addItem("a: " + a);
  addItem("b: " + b);
  addItem("gcd(a,b): " + gcd(a,b));
  addItem("fact(a): " + fact(a));
  addItem("fib(b): " + fib(b));

  return "successssssss";
};


function getRandomInt(max) {
  return Math.floor(Math.random() * max) + 1;
}