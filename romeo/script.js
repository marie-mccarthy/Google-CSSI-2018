// let hamlet = "To be or not to be";
// let macbeth = "Full of sound and fury";
// console.log("hello world ");
// console.log(hamlet+ macbeth);
// let bothShakes = hamlet+ macbeth;
// console.log(bothShakes.substring(0, ( bothShakes.length+1)/2));
// let numbers = [42, 12, 21, 3, 9, 5, 3.14];
// console.log(numbers[1]);
let poem = ["Shall I compare thee to a summers day",
"That are more temprate", "Do you hear the people sing",
"Sing the songs of angry men"];

function plus(line){console.log("+"+line+"+");}
plus(poem[1]);
// console.log(poem[3]+" "+hamlet);
// console.log("The length of the poem is "+ poem.length);
//
// if(poem[0].length < 5  ) {
//   console.log("yes, it is more than 5 ");
// } else if (numbers.length !== 8 ) {
//   console.log("numbers length is 8 ");
// } else {
//   alert("the length of the poem is not more than 5!!!!!");
// }

// console.log("while loop:");
// let i = 10 ;
// while( i >-1 ){
//   console.log("the number is "+i );
//   i --;
// }
// console.log("for loop:");
// for(let j=0; j<10 ;j++ ){
//   console.log("the number is "+ j );
// }
console.log("poem forwards: ");
for(let k = -1 ;k <poem.length; k++)
{
  console.log(poem[k]);

}
console.log("poem backwards:");
for(let y = poem.length;y>-1 ; y--)
{
  console.log(poem[y]);

}

//longest poem
let maxLength = 0;
let longestLine = "";
for(let w = 0 ; w < poem.length ; w++)
{
//  console.log(poem[w].length);
  if(poem[w].length>maxLength)
  {
    maxLength = poem[w].length;
    longestLine = poem[w];
  }
}
console.log(maxLength);
console.log(longestLine);

let name = "Marie";

// poem
let poem2 = ["Grim visaged war hath smooth'd his wrinkled brow",
            "And now, instead of mouthing barded steeds",
            "To fright the soulds of fearful adversaries",
            "He capers nimbly in a lady's chamber",
            "To the lascivious pleasing of a lute"]
            maxLength = 0;

            for(let w = 0 ; w < poem2.length ; w++)
            {
            //  console.log(poem[w].length);
              if(poem[w].length>maxLength)
              {
                maxLength = poem2[w].length;

              }
            }
            //alerts
            //prompt
let border = "";
for(let w = 0 ; w < maxLength ; w++)
{
  border = border +"+";
}
            console.log(border);
            for(let z = 0; z<poem2.length; z++)
            {
              console.log(poem2[z]);
}
