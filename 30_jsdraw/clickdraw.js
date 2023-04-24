//retrieve node in DOM via ID
var c = document.getElementById("slate");

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
}

var drawRect = function(e){
    //offsetX = -50;
    var mouseX = e.clientX;
    var mouseY = e.clientY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillStyle = "red";
    ctx.beginPath();
    ctx.lineTo(mouseX + 50, mouseY);
    ctx.moveTo(mouseX + 50, mouseY);
    ctx.lineTo(mouseX + 50, mouseY + 100);
    ctx.moveTo(mouseX + 50, mouseY + 100);
    ctx.lineTo(mouseX, mouseY + 100);
    ctx.moveTo(mouseX, mouseY + 100);
    ctx.lineTo(mouseX, mouseY);
    ctx.moveTo(mouseX, mouseY);
    ctx.fill();
    ctx.stroke();
    //ctx.fillRect(mouseX, mouseY, 50, 100);
}

var draw = function(e){
    if (mode === "rect"){
        drawRect(e)
    }
}

c.addEventListener("click", draw);