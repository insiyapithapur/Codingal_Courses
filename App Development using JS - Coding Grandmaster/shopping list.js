function addItem() {
  let itemInput = document.getElementById("itemInput");
  let itemName = itemInput.value;

  if (itemName === "") {
    alert("Please enter an item.");
    return;
  }

  let newItem = document.createElement("li");
  newItem.innerHTML = itemName;

  document.getElementById("shoppingList").appendChild(newItem);

  itemInput.value = "";
}