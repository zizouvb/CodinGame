const N: number = parseInt(readline());
const horses= []
let distanceMin = Infinity
for (let i = 0; i < N; i++) {
    const pi: number = parseInt(readline());
    horses.push(pi)
}
horses.sort((a,b)=>a-b)
for (let i=0; i<horses.length-1;i++) {
    const currentDistance = horses[i+1]-horses[i]
    if (currentDistance<distanceMin) {
        distanceMin=currentDistance
    }
}

console.log(distanceMin);
