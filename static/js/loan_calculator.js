// button variables
var calculateBtn = document.getElementById('calculate-btn');
var resetBtn = document.getElementById('reset-btn');

// input fields variables
var downPercentage = document.getElementById('downPercentage');
var sellingPrice = document.getElementById('sellingPrice');
var downAmount = document.getElementById('downAmount');

// error message variable
var errorMsg = document.getElementById('errorMsg');

var paymentTerms;
var amountFinanced,basicAmortization, monthlyInterest, monthlyAmortization, interestRate;

// validation functions
function isSellingPriceValid(sellingPrice){
	if (sellingPrice <= 0){
		errorMsg.innerHTML = "Invalid selling price. Please try again.";
		return Boolean(false);
	}
	errorMsg.innerHTML = "";
	return Boolean(true);
}

function isPercentageValid(percentage){
	if (percentage < 20){
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
function calculateStandardAmortization(){
	// getting input from user
	sellingPrice = document.getElementById('sellingPrice').value;
	downPercentage = document.getElementById('downPercentage').value;
	paymentTerms = document.getElementById('paymentTerms').value;

	// computing intermediate values
	downAmount = sellingPrice * (downPercentage / 100);
	amountFinanced = sellingPrice - downAmount;

	// setting interest based on payment terms
	interestRate = 0.055805; // sample only

	// calculating amortization
	basicAmortization = amountFinanced / paymentTerms;
	monthlyInterest = (amountFinanced * interestRate) / paymentTerms;
	monthlyAmortization = basicAmortization + monthlyInterest;

	console.log(interestRate + " " + amountFinanced + " " + downAmount + " " + paymentTerms + " "
		+ basicAmortization + " " + monthlyInterest + " " + monthlyAmortization);
}

// validating downPercentage and auto-updating downAmount
downPercentage.addEventListener('change', function(){
	sellingPrice = document.getElementById('sellingPrice').value;
	percentage = document.getElementById('downPercentage').value;
	errorMsg = document.getElementById('errorMsg');
	percentCheck = isPercentageValid(percentage);

	if (sellingPrice && percentCheck){ // if input for percentage is valid and there is input for selling price
		document.getElementById('downAmount').value = sellingPrice * (percentage / 100);
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
		document.getElementById('downAmount').value = sellingPrice * (percentage / 100);
		return;
	}
	document.getElementById('downAmount').value = "";
});

downAmount.addEventListener('change', function(){
	sellingPrice = document.getElementById('sellingPrice').value;
	percentage = document.getElementById('downPercentage').value;
	downAmount = document.getElementById('downAmount').value;

	if (sellingPrice){
		document.getElementById('downPercentage').value = (downAmount / sellingPrice) * 100;
	}
});

calculateBtn.addEventListener('click', function(){
	calculateStandardAmortization();
});

resetBtn.addEventListener('click', function(){
	// reset all fields to default
	document.getElementById('sellingPrice').value = "";
	document.getElementById('downPercentage').value = 20;
	document.getElementById('downAmount').value = "";
	document.getElementById('paymentTerms').value = 12;
});