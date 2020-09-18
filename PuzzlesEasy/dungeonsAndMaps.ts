var inputs: string[] = readline().split(' ');
const w: number = parseInt(inputs[0]);
const h: number = parseInt(inputs[1]);
var inputs: string[] = readline().split(' ');
const startRow: number = parseInt(inputs[0]);
const startCol: number = parseInt(inputs[1]);
const nbMaps: number = parseInt(readline());
let selectedMap:any = {distance:Infinity, index:"TRAP"}

const computeDistance = (currentMap, startRow, startCol,distance=0) => {
    const symbol = currentMap[startRow][startCol]
    if (symbol==="T") return distance
    else if (symbol === "." || symbol ==="#" || distance > w*h) return Infinity
    else if (symbol==="^") return computeDistance(currentMap, startRow-1, startCol,distance+1)
    else if (symbol==="v") return computeDistance(currentMap, startRow+1, startCol,distance+1)
    else if (symbol===">") return computeDistance(currentMap, startRow, startCol+1,distance+1)
    else if (symbol==="<") return computeDistance(currentMap, startRow, startCol-1,distance+1)
}
for (let i = 0; i < nbMaps; i++) {
    const currentMap=[]
    for (let j = 0; j < h; j++) {
        const mapRow: string = readline();
        currentMap.push(mapRow)
    }
    const currentDistance = computeDistance(currentMap, startRow, startCol)
    if (currentDistance<selectedMap.distance) {
        selectedMap={distance:currentDistance, index:i}
    }
}

console.log(selectedMap.index);
