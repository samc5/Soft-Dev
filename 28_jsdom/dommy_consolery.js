/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-05w
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


var red = function() { //makes the last thing on the list red
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() { //makes the first and last thing red, all else blue
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
// FIB
// FAC
// GCD

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};


