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
	dropdown1 = document.getElementById("college1")
	college1 = dropdown1.value;

	dropdown2 = document.getElementById("college2")
	college2 = dropdown2.value;
	
	url ="/comparingStats/" + college1 + "/" + college2;
	console.log(url);
	
	location.href = url;
}

function updateRankings() {
  
  rateDropdown = document.getElementById("rate");
  rateText =  document.getElementById("rateText")
  rateText.innerHTML = rateDropdown.value;

  lowhighDropdown = document.getElementById("lowhigh");
  lowhighText =  document.getElementById("lowhighText")
  lowhighText.innerHTML = lowhighDropdown.value;

}

function submitRankings(){
	rateDropdown = document.getElementById("rate")
	rate = rateDropdown.value;

	lowhighDropdown = document.getElementById("lowhigh")
	lowhigh = lowhighDropdown.value;
	
	url ="/rankings/" + rate + "/" + lowhigh;
	console.log(url);
	
	location.href = url;
}
function updateFinancialAid() {
  
  incomeDropdown = document.getElementById("income");
  incomeText =  document.getElementById("incomeText")
  incomeText.innerHTML = incomeDropdown.value;

  collegeDropdown = document.getElementById("colleges");
  collegeText =  document.getElementById("collegeText")
  collegeText.innerHTML = collegeDropdown.value;
	
}

function submitFinancialAid(){
	incomeDropdown = document.getElementById("income")
	income = incomeDropdown.value;

	collegeDropdown = document.getElementById("colleges")
	colleges = collegeDropdown.value;

	if (income !== "null") {
		url ="/financialaid/" + income + "/" + colleges;
		console.log(url);
		location.href = url;
	} else {
        	alert("Please select an income range.");
    	}
}

function updateMajor() {
  
  majorDropdown = document.getElementById("major");
  majorText =  document.getElementById("majorText")
  majorText.innerHTML = majorDropdown.value;
	
}

function submitMajor() {
	majorDropdown = document.getElementById("major");
	major = majorDropdown.value;
    
    if (major !== "null") {
	url = "/popularmajor/" + major;
        console.log(url);
        location.href = url;
    } else {
        alert("Please select a major.");
    }
}
function newSearch(url){
	location.href = url;
}
