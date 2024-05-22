/**Run when someone clicks on a tab item (include comments for clarity)*/
function openTab(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}
/** where this fucntion is called (this is the function for when you click on _____) */

function updateCollege() {
  
  dropdown1 = document.getElementById("college1");
  first =  document.getElementById("college1Show")
  first.innerHTML = dropdown1.value;

  dropdown2 = document.getElementById("college2");
  second =  document.getElementById("college2Show")
  second.innerHTML = dropdown2.value;

}

function go(){
	location.href="/comparingStats";
}

function getIncomeValue() {
    var selectElement = document.getElementById("income");
    var selectedValue = selectElement.value;
    text =  document.getElementById("incomeText")
    text.innerHTML = selectedValue;
    console.log("Selected income value: " + selectedValue);
}

function getCollegeValue() {
    var selectElement = document.getElementById("colleges");
    var selectedValue = selectElement.value;
    text =  document.getElementById("collegeText")
    text.innerHTML = selectedValue;
    console.log("Selected college value: " + selectedValue);
}
