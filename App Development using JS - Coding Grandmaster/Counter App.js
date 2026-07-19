let counter = 0;

function updateCounter() {
  document.getElementById("counterValue").innerHTML = counter;
}

function incrementCounter() {
  counter = counter + 1;
  updateCounter();
}

function decrementCounter() {
  counter = counter - 1;
  updateCounter();
}

function resetCounter() {
  counter = 0;
  updateCounter();
}