let today = new Date();

let days = [
  "Sunday",
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday"
];

let months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December"
];

let currentDay = days[today.getDay()];
let currentDate = today.getDate();
let currentMonth = months[today.getMonth()];
let currentYear = today.getFullYear();

document.getElementById("day").innerHTML =
  "Day: " + currentDay;

document.getElementById("date").innerHTML =
  "Date: " + currentDate;

document.getElementById("month").innerHTML =
  "Month: " + currentMonth;

document.getElementById("year").innerHTML =
  "Year: " + currentYear;