
let achillesMood = "wrathful";
let achillesNumberOfShips = 0 ;
let achillesAlive = true;

let achilles = {
mood :"wrathful",
achillesNumberOfShips: 50,
isAlive:true,
buddies:["doggo", "petronus"],
attack: function(){
  console.log("yarg");
}
};
achilles.isALive = false;
achilles.killedBy ="paris";
achilles.mood =  "dead";

let aristotle = {
philospher : true,
career : "thinker",
works: ["physics", "philosphy"],

placeOfResidence:"athens"
};

function changeResidence(person)
{
  person.works.push = "biology";
  person.placeOfResidence = "Macedon";
  person.student = "alexander";
  return person ;
};
