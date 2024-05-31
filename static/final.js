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

async function fetchjson(college1, college2){
	URL1 = "/graphdata/" + college1;


	URL2 = "/graphdata/" + college2;

    	json1 = await fetch(URL1).json().then(response => response.json());
	json2 = await fetch(URL2).json().then(response => response.json());

	makeChart(json1, json2, college1, college2)

}
	
function makeChart(json1, json2, c1, c2){

	f0C1 = json1[ 'f0to30grand' ]
	f30C1 = json1[ 'f30to48grand' ]
	f48C1 = json1[ 'f48to75grand' ]
	f75C1 = json1[ 'f75to110grand' ]
	f110C1 = json1[ 'f110grandup' ]

	f0C2 = json2[ 'f0to30grand' ]
	f30C2 = json2[ 'f30to48grand' ]
	f48C2 = json2[ 'f48to75grand' ]
	f75C2 = json2[ 'f75to110grand' ]
	f110C2 = json2[ 'f110grandup' ]
	
	anychart.onDocumentReady(function () {
	  
	  var data = [
	    
	    ["0-30k", f0C1, f0C2],
	    ["30-48k", f30C1, f30C2],
	    ["48-75k", f48C1, f48C2],
	    ["75-110k", f75C1, f75C2],
	    ["110k+", f110C1, f110C2]
	  ];
	  
	  var dataSet = anychart.data.set(data);
	
	  var college1Data = dataSet.mapAs({x: 0, value: 1});
	  var college2Data = dataSet.mapAs({x: 0, value: 2});
	
	  var chart = anychart.line();
	
	  var college1 = chart.line(college1Data);
	  college1.name(c1);
	  var college2 = chart.line(college2Data);
	  college2.name(c2);
	
	  chart.legend().enabled(true);
	  
	  chart.title("College Finacial Aid vs Income Data");
	  
	  chart.yAxis().title("Money");
	  chart.xAxis().title("Income Range");
	  
	  college1.hovered().markers().enabled(true).type("circle").size(4);
	  college2.hovered().markers().enabled(true).type("circle").size(4);
	  
	  chart.crosshair().enabled(true).yStroke(null).yLabel(false);
	  
	  chart.tooltip().positionMode("point");
	  chart.tooltip().position("right").anchor("left-center").offsetX(5).offsetY(5);
	  
	  chart.container("graph");
	  
	  chart.draw();
	  
	});

}

function newSearch(url){
	location.href = url;
}
