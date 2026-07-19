// Perimeter Calculator

let shape = prompt(
  "Choose a shape:\n1. Square\n2. Rectangle\n3. Triangle\n4. Circle"
);

let perimeter;

if (shape === "1") {
  let side = Number(prompt("Enter the side length of the square:"));

  perimeter = 4 * side;

  alert("The perimeter of the square is: " + perimeter);
} else if (shape === "2") {
  let length = Number(prompt("Enter the length of the rectangle:"));
  let width = Number(prompt("Enter the width of the rectangle:"));

  perimeter = 2 * (length + width);

  alert("The perimeter of the rectangle is: " + perimeter);
} else if (shape === "3") {
  let side1 = Number(prompt("Enter the first side of the triangle:"));
  let side2 = Number(prompt("Enter the second side of the triangle:"));
  let side3 = Number(prompt("Enter the third side of the triangle:"));

  perimeter = side1 + side2 + side3;

  alert("The perimeter of the triangle is: " + perimeter);
} else if (shape === "4") {
  let radius = Number(prompt("Enter the radius of the circle:"));

  perimeter = 2 * Math.PI * radius;

  alert("The circumference of the circle is: " + perimeter.toFixed(2));
} else {
  alert("Invalid choice! Please enter a number between 1 and 4.");
}