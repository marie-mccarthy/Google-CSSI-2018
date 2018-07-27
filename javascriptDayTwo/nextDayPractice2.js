window.onload = function ()
    {
    let button = document.querySelector("button");
    button.onclick = onButtonClick;

    //button.onmouseenter = onHover;
    let myTitle = document.querySelector("h1");

    myTitle.onclick = onElementClick;
    let myDivs = document.querySelectorAll("div");
    for(let i = 0 ; i < myDivs.length; i ++)
    {
      myDivs[i].onclick = onElementClick;
    }

    }
//myButton.onclick = function
function onButtonClick()
{
  let myInput = document.querySelector("input");
  console.log(myInput.value);

}
function onHover(){
  console.log("hover");
  let myTitle =  document.querySelector("h1");
  myTitle.style.cursor = "my Title";
  myTitle.innerText = "New Title";
  }
function changeDiv ()
  {
  console.log("changing the div");
  div.innerText = "New Title";
  }
function onElementClick(evt)
  {
  let clicked = evt.target;
  console.log(clicked);
  let clickedParent = evt.target.parentElement;
  console.log(clickedParent);
  let siblings = clickedParent.querySelectorAll("p");
  console.log(siblings);
  }

  function changeLines(){

    let lines = document.querySelectorAll(".lines");

    for(let i = 0 ; i < lines.length; i ++){

      lines[i].textContent = "changed line";
      lines[i].style.backgroundColor = "lime";
      lines[i].style.left = 100;
      lines[i].style.paddingLeft = "50px";

      if(i == 0 ){
        lines [i].style.display = "none";
      }
    }
  }

//Notes
