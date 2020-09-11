var inputs: string[] = readline().split(' ');
const lightX: number = parseInt(inputs[0]); // the X position of the light of power
const lightY: number = parseInt(inputs[1]); // the Y position of the light of power
const initialTx: number = parseInt(inputs[2]); // Thor's starting X position
const initialTy: number = parseInt(inputs[3]); // Thor's starting Y position

let thorx=initialTx;
let thory=initialTy;
// game loop
while (true) {
    const remainingTurns: number = parseInt(readline()); // The remaining amount of turns Thor can move. Do not remove this line.
    let directionx="";
    let directiony="";
    if (thorx>lightX){
        directionx = "W";
        thorx=thorx-1;
    } else if (thorx<lightX){
        directionx = "E";
        thorx=thorx+1
    }
    if (thory>lightY){
        directiony = "N"
        thory=thory-1
    } else if (thory<lightY){
        directiony = "S"
        thory=thory+1
    }

    // A single line providing the move to be made: N NE E SE S SW W or NW
    console.log(directiony + directionx) 
}
