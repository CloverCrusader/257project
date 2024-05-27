function updateCollege() {
  
  dropdown1 = document.getElementById("college1");
  first =  document.getElementById("college1Show")
  first.innerHTML = dropdown1.value;

  dropdown2 = document.getElementById("college2");
  second =  document.getElementById("college2Show")
  second.innerHTML = dropdown2.value;

}

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

	if ((rate !== "null") && (lowhigh !== "null")) {
		url ="/rankings/" + rate + "/" + lowhigh;
		console.log(url);
		location.href = url;
    	} else {
        	alert("Please select both options.");
    	}
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

function fetchjson(college1, college2){
	URL = "/graphdata/" + college1;

    	fetch(URL).then( response => response.json());

	// assign above to first dictionary

	URL = "/graphdata/" + college2;

    	fetch(URL).then( response => response.json());

	// assign above to second dictionary

	anychart.onDocumentReady(function () {
	  
	  var data = [
	    
	    ["0-30k", 4, 0],
	    ["30-48k", 4, 0],
	    ["48-75k", 6, 0],
	    ["75-110k", 9, 1],
	    ["110k+", 12, 2]
	  ];
	  
	  // create a data set
	  var dataSet = anychart.data.set(data);
	
	  var college1Data = dataSet.mapAs({x: 0, value: 1});
	  var college2Data = dataSet.mapAs({x: 0, value: 2});
	
	  var chart = anychart.line();
	
	  var college1 = chart.line(college1Data);
	  college1.name("College1");
	  var college2 = chart.line(college2Data);
	  college2.name("College2");
	
	  chart.legend().enabled(true);
	  
	  chart.title("College Finaval Aid vs Income Data");
	  
	  chart.yAxis().title("Money");
	  chart.xAxis().title("Income Range");
	  
	  // customize the series markers
	  college1.hovered().markers().enabled(true).type("circle").size(4);
	  college2.hovered().markers().enabled(true).type("circle").size(4);
	  
	  // turn on crosshairs and remove the y hair
	  chart.crosshair().enabled(true).yStroke(null).yLabel(false);
	  
	  // change the tooltip position
	  chart.tooltip().positionMode("point");
	  chart.tooltip().position("right").anchor("left-center").offsetX(5).offsetY(5);
	  
	  // specify where to display the chart
	  chart.container("container");
	  
	  chart.draw();
	  
	});

}

function newSearch(url){
	location.href = url;
}
