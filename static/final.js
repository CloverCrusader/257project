/*The function 'updateCollege' takes the values from the two dropdowns on the compare 
tab and uses the stored variables to display the chosen schools below
*/
function updateCollege() {
  dropdown1 = document.getElementById("college1");
  first =  document.getElementById("college1Show")
  first.innerHTML = dropdown1.value;
  dropdown2 = document.getElementById("college2");
  second =  document.getElementById("college2Show")
  second.innerHTML = dropdown2.value;
}
/*'submitCompare' takes the values from the two dropdowns on the compare 
tab and passes the stored variables to the display page for the comparing tab, results in an alert if the same college is selected
*/
function submitCompare(){
	dropdown1 = document.getElementById("college1")
	college1 = dropdown1.value;
	
	dropdown2 = document.getElementById("college2")
	college2 = dropdown2.value;
	
	if (college1 !==college2) {
		url ="/compare/" + college1 + "/" + college2;
		console.log(url);
		location.href = url;
	} else {
		alert("Please select two different colleges.");
	}	
}
/*The function 'updateRankings' takes the values from the two dropdowns on the Ranking 
tab and uses the stored variables to display the schools based on the chosen filter and sort by
*/
function updateRankings() {
  
	rateDropdown = document.getElementById("rate");
	rateText =  document.getElementById("rateText")
	rateText.innerHTML = rateDropdown.value;
	
	lowhighDropdown = document.getElementById("lowhigh");
	lowhighText =  document.getElementById("lowhighText")
	lowhighText.innerHTML = lowhighDropdown.value;
}
/*'submitRankings' takes the values from the two dropdowns on the rankings 
tab and passes the stored variables to the display page for the rankings tab, results in an alert if only one is selected
*/
function submitRankings(){
	rateDropdown = document.getElementById("rate")
	rate = rateDropdown.value;
	lowhighDropdown = document.getElementById("lowhigh")
	lowhigh = lowhighDropdown.value;
	if ((rate !== "null") && (lowhigh !== "null")) {
		url ="/rankings/" + rate + "/" + lowhigh;
		console.log(url);
		location.href = url;
    	} else {
        	alert("Please select both options.");
    	}
}
/*The function 'updateFinancialAid' takes the values from the two dropdowns on the Estimate Your Financial Aid 
tab and uses the stored variables to display choices of income level and school below
*/
function updateFinancialAid() {
	
	incomeDropdown = document.getElementById("income");
	incomeText =  document.getElementById("incomeText")
	incomeText.innerHTML = incomeDropdown.value;
	
	collegeDropdown = document.getElementById("colleges");
	collegeText =  document.getElementById("collegeText")
	collegeText.innerHTML = collegeDropdown.value;
}
/*'submitFinancialAid' takes the values from the two dropdowns on the financial aid 
tab and passes the stored variables to the display page for the financial aid tab, results in an alert if income is not selected
*/
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
/*The function 'updateMajor' takes the values from the two dropdowns on the major 
tab and uses the stored variables to display the chosen schools below
*/
function updateMajor() {
  
	majorDropdown = document.getElementById("major");
	majorText =  document.getElementById("majorText")
	majorText.innerHTML = majorDropdown.value;
}
/*'submitMajor' takes the values from the two dropdowns on the popular major 
tab and passes the stored variables to the display page for the popular major tab, results in an alert if major is not selected
*/
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
/*The function 'newSearch' sends the user to a refreshed screen to search again for the specific tab's query.
*/
function newSearch(url){
	location.href = url;
}
