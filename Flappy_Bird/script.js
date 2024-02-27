var canvas= document.getElementById('gamezone');
var context= canvas.getContext('2d');
var scoreshow=document.getElementById('score');
var high_score = document.getElementById('high-score');

var birdimg= new Image();
var hinhnenchinh=new Image();
var upper= new Image();
var lower=new Image();
birdimg.src="images/bird.png";
hinhnenchinh.src="images/main.png";
upper.src="images/upperpipe.png";
lower.src="images/lowerpipe.png";

var highest = 0;
var score=0;
var range = [140];
var lowerpipe; 

var bird={
    x: hinhnenchinh.width/5,
    y: hinhnenchinh.height/2
}
var pipes=[]; 
pipes[0]={
    x:canvas.width,
    y:0 
}

function run(){
    context.drawImage(hinhnenchinh,0,0);
    context.drawImage(birdimg,bird.x,bird.y);
    for(var i=0;i<pipes.length;i++){
        var r = range[i];
        lowerpipe=upper.height+r;
        context.drawImage(upper,pipes[i].x,pipes[i].y);

        context.drawImage(lower,pipes[i].x,pipes[i].y+lowerpipe);

        pipes[i].x-=5; 

        if(pipes[i].x ==canvas.width/2){
            range.push( Math.floor(Math.random()*140) + 85) ;
            pipes.push({
                x:canvas.width,
                y:Math.floor(Math.random()*upper.height)-upper.height
            })
        }
        if(pipes[i].x == 0){
            pipes.splice(0,1);
            range.splice(0,1);
        }
     
        if(pipes[i].x==bird.x)score++;  

        if(bird.y+birdimg.height>=canvas.height|| bird.y - birdimg.height <= 0 ||
        bird.x+birdimg.width>= pipes[i].x && bird.x <= pipes[i].x +upper.width
        && (bird.y<=pipes[i].y+upper.height||
        bird.y +birdimg.height>= pipes[i].y+ lowerpipe)    
        ){
            return;
        }                   
    }

    scoreshow.innerHTML="Score: "+score;
    if( score > highest){
        highest = score;
    }
    high_score.innerHTML="High score: " + highest;

    bird.y+=3;
    requestAnimationFrame(run);
}

function fly(){
    bird.y-=50; 
}

function restart(){
    bird.x = hinhnenchinh.width/5;
    bird.y= hinhnenchinh.height/2;
    pipes.splice(0,pipes.length);
    range.splice(0,range.length);
    pipes[0] = {
        x:canvas.width,
        y:0 
    }
    range = [140];
    score=0;
    run();
}

document.addEventListener("keydown",(e)=>{
if(e.keyCode == 38 || e.keyCode == 87  || e.keyCode == 32)
    fly();
if(e.keyCode == 13){
    restart();
}
    
})
document.addEventListener("click",fly)


run();


