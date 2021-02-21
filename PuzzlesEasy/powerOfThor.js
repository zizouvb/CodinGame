var inputs = readline().split(' ');
const lightX = parseInt(inputs[0]); // the X position of the light of power
const lightY = parseInt(inputs[1]); // the Y position of the light of power
const initialTx = parseInt(inputs[2]); // Thor's starting X position
const initialTy = parseInt(inputs[3]); // Thor's starting Y position

let currentX = initialTx
let currentY = initialTy
// game loop
while (true) {
    const remainingTurns = parseInt(readline()); // The remaining amount of turns Thor can move. Do not remove this line.
    let ans = ""
    if (currentY < lightY) {
        ans += "S";
        currentY += 1
    }
    if (currentY > lightY) {
        ans += "N";
        currentY -= 1
    }
    if (currentX < lightX) {
        ans += "E";
        currentX += 1
    }
    if (currentX > lightX) {
        ans += "W";
        currentX -= 1
    }
    console.log(ans)
}
