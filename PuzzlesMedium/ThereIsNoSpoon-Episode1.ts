const width = parseInt(readline()); // the number of cells on the X axis
const height = parseInt(readline()); // the number of cells on the Y axis
const grid = []
for (let i = 0; i < height; i++) {
    grid.push(readline()); // width characters, each either 0 or .
}

const findRight = (x,y) => {
    for (let i=x+1; i<width;i++) {
        if (grid[y][i]==="0") return [i,y]
    }
    return [-1,-1]
}

const findBottom = (x,y) => {
    for (let i=y+1; i<height;i++) {
        if (grid[i][x]==="0") return [x,i]
    }
    return [-1,-1]
}

for (let y=0;y<height;y++) {
    for(let x=0; x<width;x++){
        if (grid[y][x]==="0"){
            const [rightX,rightY] = findRight(x,y)
            const [bottomX, bottomY] = findBottom(x,y)
            console.log(x,y,rightX,rightY,bottomX,bottomY)
        }
    }
}
