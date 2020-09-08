/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

var inputs: string[] = readline().split(' ');
const W: number = parseInt(inputs[0]); // width of the building.
const H: number = parseInt(inputs[1]); // height of the building.
const N: number = parseInt(readline()); // maximum number of turns before game over.
var inputs: string[] = readline().split(' ');
const X0: number = parseInt(inputs[0]);
const Y0: number = parseInt(inputs[1]);

let x=X0;
let y=Y0;
let x_max=W;
let y_max=H;
let x_min=0;
let y_min=0;

// game loop
while (true) {
    const bombDir: string = readline(); // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    // Write an action using console.log()
    // To debug: console.error('Debug messages...');


    // the location of the next window Batman should jump to.}
    if (bombDir=='U'){
        y_max = y
        y=y_min+Math.floor((y-y_min)/2)
    }
    if (bombDir=='UR'){
        y_max = y
        y=y_min+Math.floor((y-y_min)/2)
        x_min=x
        x=x+Math.floor((x_max-x)/2)
    }
    if (bombDir=='R'){
        x_min=x
        x=x+Math.floor((x_max-x)/2)
    }
    if (bombDir=='DR'){
        y_min=y
        y=y+Math.floor((y_max-y)/2)
        x_min=x
        x=x+Math.floor((x_max-x)/2)
    }
    if (bombDir=='D'){
        y_min=y
        y=y+Math.floor((y_max-y)/2)
    }
    if (bombDir=='DL'){
        y_min=y
        y=y+Math.floor((y_max-y)/2)
        x_max=x
        x=x_min+Math.floor((x-x_min)/2)
    }
    if (bombDir=='L'){
        x_max=x
        x=x_min+Math.floor((x-x_min)/2)
    }
    if (bombDir=='UL'){
        y_max = y
        y=y_min+Math.floor((y-y_min)/2)
        x_max=x
        x=x_min+Math.floor((x-x_min)/2)
    }
    console.log(x,y)
}



