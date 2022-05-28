// for formatting of results
nf = new Intl.NumberFormat('en-US', {
	minimumFractionDigits: 2,
  	maximumFractionDigits: 2,
});

// button variables
var calculateBtn = document.getElementById('calculate-btn');
var resetBtn = document.getElementById('reset-btn');

// input fields variables
var downPercentage = document.getElementById('downPercentage');
var sellingPrice = document.getElementById('sellingPrice');
var downAmount = document.getElementById('downAmount');

// error message variable
var errorMsg = document.getElementById('errorMsg');

// results fields variables
var sellingPriceRes = document.getElementById('sellingPriceResults');
var downPaymentRes = document.getElementById('downPaymentResults');
var paymentTermsRes = document.getElementById('paymentTermsResults');
var amountFinancedRes = document.getElementById('amountFinancedResults');
var monthlyAmortRes = document.getElementById('monthlyAmortizationResults');

// other intermediate variables
var paymentTerms;
var amountFinanced,basicAmortization, monthlyInterest, monthlyAmortization, interestRate;

// hardcoded interest rates based on payment terms (e.g. 12 mos, 18 mos, ..., 60 mos)
var rate12 = 5.5800;
var rate18 = 8.1500;
var rate24 = 11.0200;
var rate36 = 16.9000;
var rate48 = 22.9600;
var rate60 = 28.7600;

function openTab(evt, tabName){
	var i, tabcontent, tablinks;

	// hiding all elements with class="tabcontent"
	tabcontent = document.getElementsByClassName("tabcontent");
	for (i = 0; i < tabcontent.length; i++){
		tabcontent[i].style.display = "none";
	}

	// get all elements with class="tablinks" and remove the class "active"
	tablinks = document.getElementsByClassName("tablinks");
  	for (i = 0; i < tablinks.length; i++) {
    	tablinks[i].className = tablinks[i].className.replace(" active", "");
  	}

  	// show current tab and add 'active' class to the button that opened the tab
  	document.getElementById(tabName).style.display = "flex";
  	evt.currentTarget.className += " active";
}

// formatting function 
function setTwoNumberDecimal(num){
	num.value = parseFloat(num.value).toFixed(2);
}

// validation functions
function isSellingPriceValid(sellingPrice){
	if (sellingPrice <= 0 || isNaN(sellingPrice)){
		errorMsg.innerHTML = "Invalid selling price. Please try again.";
		document.getElementById('sellingPrice').value = "";
		return Boolean(false);
	}
	errorMsg.innerHTML = "";
	return Boolean(true);
}

function isPercentageValid(percentage){
	if (isNaN(percentage)){
		errorMsg.innerHTML = "Invalid down payment percentage. Please try again.";
		document.getElementById('downPercentage').value = "";
		return Boolean(false);
	} else if (percentage < 20){
		errorMsg.innerHTML = "Percentage of down payment must at least 20% of the selling price. Please try again.";
		return Boolean(false);
	} else if (percentage > 100){
		errorMsg.innerHTML = "Percentage of down payment must be lower than 100% of the selling price. Please try again.";
		return Boolean(false);
	} 
	errorMsg.innerHTML = "";
	return Boolean(true);
}

// calculation functions
function getInterestRate(paymentTerms){
	if (paymentTerms == 12){
		return rate12;
	} else if (paymentTerms == 18){
		return rate18;
	} else if (paymentTerms == 24){
		return rate24;
	} else if (paymentTerms == 36){
		return rate36;
	} else if (paymentTerms == 48){
		return rate48;
	} else if (paymentTerms == 60){
		return rate60;
	}
	return 0;
}

function calculateStandardAmortization(){
	// getting input from user
	sellingPrice = document.getElementById('sellingPrice').value;
	downAmount = document.getElementById('downAmount').value;
	downPercentage = document.getElementById('downPercentage').value;
	paymentTerms = document.getElementById('paymentTerms').value;

	// validate input
	if (isSellingPriceValid(sellingPrice) && isPercentageValid(downPercentage)){
		// compute intermediate values
		amountFinanced = sellingPrice - downAmount;

		// setting interest based on payment terms
		interestRate = getInterestRate(paymentTerms) / 100;

		// calculating amortization
		basicAmortization = amountFinanced / paymentTerms;
		monthlyInterest = (amountFinanced * interestRate) / paymentTerms;
		monthlyAmortization = basicAmortization + monthlyInterest;

		// setting results variables
		sellingPriceRes.innerHTML = nf.format(sellingPrice);
		downPaymentRes.innerHTML = nf.format(downAmount);
		paymentTermsRes.innerHTML = paymentTerms;
		amountFinancedRes.innerHTML = nf.format(amountFinanced);
		monthlyAmortRes.innerHTML = nf.format(monthlyAmortization);

		// show calculation results 
		document.getElementById('calculator-results').style.display = "block";
		return;
	} 
	errorMsg.innerHTML = "One of the fields detected an invalid or missing input. Please recheck your figures.";
}

// validating downPercentage and auto-updating downAmount
downPercentage.addEventListener('change', function(){
	sellingPrice = document.getElementById('sellingPrice').value;
	percentage = document.getElementById('downPercentage').value;
	errorMsg = document.getElementById('errorMsg');
	percentCheck = isPercentageValid(percentage);

	if (sellingPrice && percentCheck){ // if input for percentage is valid and there is input for selling price
		downAmount = document.getElementById('downAmount');
		downAmount.value = sellingPrice * (percentage / 100);
		setTwoNumberDecimal(downAmount);
		return;
	} 
	document.getElementById('downAmount').value = "";
});

// validating sellingPrice and auto-updating downAmount 
sellingPrice.addEventListener('change', function(){
	sellingPrice = document.getElementById('sellingPrice').value;
	percentage = document.getElementById('downPercentage').value;
	errorMsg = document.getElementById('errorMsg');
	priceCheck = isSellingPriceValid(sellingPrice);

	if (percentage && priceCheck){
		downAmount = document.getElementById('downAmount');
		downAmount.value = sellingPrice * (percentage / 100);
		setTwoNumberDecimal(downAmount);
		return;
	}
	document.getElementById('downAmount').value = "";
});

downAmount.addEventListener('change', function(){
	sellingPrice = document.getElementById('sellingPrice').value;
	percentage = document.getElementById('downPercentage').value;
	downAmount = document.getElementById('downAmount').value;

	if (sellingPrice){
		downPercentage = document.getElementById('downPercentage');
		downPercentage.value = (downAmount / sellingPrice) * 100;
		setTwoNumberDecimal(downPercentage);
	}
	isPercentageValid(downPercentage.value);
});

calculateBtn.addEventListener('click', function(){
	calculateStandardAmortization();
});

resetBtn.addEventListener('click', function(){
	// reset all fields to default
	document.getElementById('sellingPrice').value = "";
	document.getElementById('downPercentage').value = 20.00;
	document.getElementById('downAmount').value = "";
	document.getElementById('paymentTerms').value = 12;

	// hide calculation results
	document.getElementById('calculator-results').style.display = "none";
});