const BEGIN:any = readline().split(".");
const BEGIN_DATE:any = new Date(BEGIN.reverse())
const END:any = readline().split('.');
const END_DATE:any = new Date(END.reverse())
const diff = new Date(END_DATE - BEGIN_DATE);

const day = diff.valueOf() / (1000 * 3600 * 24)
const month = diff.getUTCMonth()
const year = diff.getUTCFullYear() - 1970

let answer = "";

if (year > 0) {
    answer += `${year} year${(year>1)?"s":""}, `;
}
if (month > 0) {
    answer += `${month} month${(month>1)?"s":""}, `;
}    

console.log(answer + `total ${day} days`);
