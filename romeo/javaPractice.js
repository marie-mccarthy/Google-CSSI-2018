let poem = ["Shall I compare thee to a summers day",
"That are more temprate", "Do you hear the people sing",
"Sing the songs of angry men"];

function plus(line){console.log("+"+line+"+");}
plus(poem[0]);
function together(x, b) {
  console.log(x+" and "+ b)
}
  function makeReturnValue()
  {
    return "Android";
  }

function messageBars(message){
  console.log("+".repeat(40))
  console.log(message);
  console.log("+".repeat(40));
}

let story= ["Grim visaged war hath smooth'd his wrinkled brow",
            "And now, instead of mouthing barded steeds",
            "To fright the soulds of fearful adversaries",
            "He capers nimbly in a lady's chamber",
            "To the lascivious pleasing of a lute"]
            let longestLine = 0;

            for(let w = 0 ; w < story.length ; w++)
            {
            //  console.log(poem[w].length);
              if(story[w].length>longestLine)
              {
                longestLine = story[w].length;

              }
            }
            console.log(longestLine);
            console.log("+".repeat(longestLine));
let spaces = "";
            for(let k = 0 ;k <story.length; k++)
            {
              spaces = longestLine- story[k].length;
              console.log("+"+story[k]+(" ".repeat(spaces))+"+");

            }
  console.log("+".repeat(longestLine));
