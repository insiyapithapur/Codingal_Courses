function changeColour() {
  let red = Math.floor(Math.random() * 256);
  let green = Math.floor(Math.random() * 256);
  let blue = Math.floor(Math.random() * 256);

  let randomColour =
    "rgb(" + red + ", " + green + ", " + blue + ")";

  document.body.style.backgroundColor = randomColour;

  document.getElementById("colourName").innerHTML =
    "Current colour: " + randomColour;
}