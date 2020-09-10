/**
 * Save humans, destroy zombies!
 **/

let nextX = 0
let nextY = 0

// game loop
while (true) {
    let closestDistance = 100000000
    var inputs: string[] = readline().split(' ');
    const x: number = parseInt(inputs[0]);
    const y: number = parseInt(inputs[1]);
    const humanCount: number = parseInt(readline());
    for (let i = 0; i < humanCount; i++) {
        var inputs: string[] = readline().split(' ');
        const humanId: number = parseInt(inputs[0]);
        const humanX: number = parseInt(inputs[1]);
        const humanY: number = parseInt(inputs[2]);
        const currentDistance = (x-humanX)**2 + (y- humanY)**2
        if (currentDistance<closestDistance && humanCount!==2)
        {
            nextX = humanX
            nextY = humanY
            closestDistance=currentDistance 
        } else if (humanCount==2) {
            nextX = humanX
            nextY = humanY
        }
    }
    const zombieCount: number = parseInt(readline());
    for (let i = 0; i < zombieCount; i++) {
        var inputs: string[] = readline().split(' ');
        const zombieId: number = parseInt(inputs[0]);
        const zombieX: number = parseInt(inputs[1]);
        const zombieY: number = parseInt(inputs[2]);
        const zombieXNext: number = parseInt(inputs[3]);
        const zombieYNext: number = parseInt(inputs[4]);
    }

    // Write an action using console.log()
    // To debug: console.error('Debug messages...');

    console.log(nextX + " " + nextY);     // Your destination coordinates

}
