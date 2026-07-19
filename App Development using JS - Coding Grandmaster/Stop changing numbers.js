let isChanging = true;
let clickCount = 0;

let numberTimer = setInterval(changeNumber, 500);

function changeNumber() {
  let randomNumber = Math.floor(Math.random() * 10) + 1;

  document.getElementById("randomNumber").innerHTML = randomNumber;
}

function toggleNumber() {
  clickCount = clickCount + 1;

  if (clickCount % 2 !== 0) {
    clearInterval(numberTimer);
    isChanging = false;

    document.getElementById("status").innerHTML =
      "Number stopped. Click again to start.";
  } else {
    numberTimer = setInterval(changeNumber, 500);
    isChanging = true;

    document.getElementById("status").innerHTML =
      "Number is changing. Click to stop.";
  }
}