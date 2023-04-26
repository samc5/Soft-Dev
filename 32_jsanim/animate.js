var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");
var dvdButton = document.getElementById("buttonDvd");
var ctx = c.getContext("2d");

ctx.fillStyle = "turquoise"

var requestID;

var clear = (e) => {
    e.preventDefault();
    ctx.clearRect(0,0, c.width, c.height);
};

dvd = document.getElementById("dvd");
// var dvdX = 0;
// var dvdY = 0;
var growing = true;
var radius = 0;


var dvdLogoSetup = function() {
    window.cancelAnimationFrame(requestID);
    var rectWidth = 60;
    var rectHeight = 40;
    var rectX = getRandomInt(c.width - rectWidth);
    var rectY = getRandomInt(c.height - rectHeight);
    var xVel = 2;
    var yVel = 2;
    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = (e) =>{
        ctx.clearRect(0,0, c.width, c.height);
        ctx.drawImage(logo, rectX, rectY,rectWidth, rectHeight);
        //const progress = timestamp - start;
        window.cancelAnimationFrame(requestID); 
        //requestID = requestAnimationFrame(drawDvd);
    
        if (rectX <= 0 || rectX + rectWidth >= c.width){
            xVel *= -1;
        }
        if (rectY <= 0 || rectY + rectHeight >= c.height){
            yVel *= -1;
        }
        rectX += xVel;
        rectY += yVel;
        requestID = window.requestAnimationFrame(dvdLogo)
    }
    dvdLogo();
}



function getRandomInt(max) {
    return Math.floor(Math.random() * max) + 1;
  }
  

var drawDot = (e) =>{
    ctx.clearRect(0,0,c.width,c.height)
    ctx.beginPath();
    ctx.arc(c.width/2, c.height/2, radius, 0, 2 * Math.PI);
    ctx.fill();
    //const progress = timestamp - start;
    window.cancelAnimationFrame(requestID); 
    requestID = requestAnimationFrame(drawDot);
    if(radius >= c.width / 2){
        growing = false;
    }
    if(radius <= 0){
        growing = true;
    }
    if(growing){
        radius += 2;
    } else{
        radius -= 2;
    }
}

var stopIt = () => {
    console.log("stopIt invoked ..");
    console.log(requestID);

    window.cancelAnimationFrame(requestID);
}
dotButton.addEventListener("click", drawDot)
dvdButton.addEventListener("click", dvdLogoSetup)
stopButton.addEventListener("click", stopIt)