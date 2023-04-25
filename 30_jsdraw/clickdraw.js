// Sam Cowan, Ameer Alnasser
// SoftDev pd2
// K30 -- canvas based JS drawing
// 2023-04-25
// HTML file for JavaScript canvas work


//retrieve node in DOM via ID
var c = document.getElementById("slate");
var toggle = document.getElementById("buttonToggle");
var wipe = document.getElementById("buttonClear");
//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init global state var
var mode = "rect";

var toggleMode = function(e){
    console.log("toggling");
    if (mode === "rect"){
        mode = "circ";
    }
    else{
        mode = "rect";
    }
    toggle.textContent = `${mode}`;
}

var drawRect = function(e){
    var mouseX = e.clientX;
    var mouseY = e.clientY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    console.log(e.offsetX, e.offsetY);
    ctx.fillStyle = "red";
    ctx.fillRect(e.offsetX, e.offsetY, 50, 100);
}

var drawCircle = function(e){
    var mouseX = e.clientX;
    var mouseY = e.clientY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    console.log(e.offsetX, e.offsetY);
    ctx.fillStyle = "red";
    ctx.strokeStyle = "black";
    ctx.beginPath();
    ctx.arc(e.offsetX, e.offsetY, 45, 0, 2 * Math.PI);
    ctx.fill()
}


var draw = function(e){
    if (mode === "rect"){
        drawRect(e);
    }
    else{
        drawCircle(e);
    }
}

var wipeCanvas = function(e){
    ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click", draw);
toggle.addEventListener("click", toggleMode);
wipe.addEventListener("click", wipeCanvas)