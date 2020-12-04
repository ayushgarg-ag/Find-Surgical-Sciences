var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
    // This function will display the specified tab of the form...
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    //... and fix the Previous/Next buttons:
    if (n == 0) {
        document.getElementById("prevBtn").style.display = "none";
    } else {
        document.getElementById("prevBtn").style.display = "inline";
    }
    if (n == (x.length - 1)) {
        document.getElementById("nextBtn").innerHTML = "Submit";
    }
    else {
        document.getElementById("nextBtn").innerHTML = "Next";
    }
    //... and run a function that will display the correct step indicator:
    fixStepIndicator(n)
}

function nextPrev(n) {
    recheckValidation(currentTab);

    // This function will figure out which tab to display
    var x = document.getElementsByClassName("tab");
    // Exit the function if any field in the current tab is invalid:
    if (n == 1 && !validateForm()) return false;
    // Hide the current tab:
    x[currentTab].style.display = "none";
    // Increase or decrease the current tab by 1:
    currentTab = currentTab + n;
    // if you have reached the end of the form...
    if (currentTab >= x.length) {
        // ... the form gets submitted:
        // document.getElementById("my-form").submit();
        createFile();
        return false;
    }
    // Otherwise, display the correct tab:
    showTab(currentTab);
}

function recheckValidation(n) {
    // This function deals with validation of the form fields
    var x, y, i, valid = true;
    x = document.getElementsByClassName("tab");
    y = x[n].getElementsByTagName("input");
    // A loop that checks every input field in the current tab:
    for (i = 0; i < y.length; i++) {
        // If a field is empty...
        if (y[i].value == "") {
            // add an "invalid" class to the field:
            y[i].className += " invalid";
        }
        else {
            y[i].className -= " invalid";
        }
    }
}

function validateForm() {
    // This function deals with validation of the form fields
    var x, y, i, valid = true;
    x = document.getElementsByClassName("tab");
    y = x[currentTab].getElementsByTagName("input");
    // A loop that checks every input field in the current tab:
    for (i = 0; i < y.length; i++) {
        // If a field is empty...
        if (y[i].value == "") {
            // add an "invalid" class to the field:
            y[i].className += " invalid";
            // and set the current valid status to false
            valid = false;
        }
    }
    // If the valid status is true, mark the step as finished and valid:
    if (valid) {
        document.getElementsByClassName("step")[currentTab].className += " finish";
    }
    return valid; // return the valid status
}

function fixStepIndicator(n) {
    // This function removes the "active" class of all steps...
    var i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(" active", "");
    }
    //... and adds the "active" class on the current step:
    x[n].className += " active";
}

function createFile() {
    var result = "";
    var all = document.getElementsByTagName("*");
    var range = -1;

    for (var i = 0; i < all.length; i++) {
        var element = all[i];
        console.log(element.checked);
        // Deals with range values
        if (element.className.includes("range")) {
            range++;
        }
        else if (range == 0) {
            result += `${element.name}=[${element.value},`;
            range++;
        }
        else if (range == 1) {
            result += `${element.value}]\n`;
            range -= 2;
        }

        // Deals with section names
        else if (element.tagName == 'DIV' && element.className.includes("header")) {
            result += `\n[${element.id}]\n`;
        }

        // Deals with input values
        else if (element.tagName == 'INPUT' || element.tagName == 'SELECT') {
            if (element.type == "radio") {
                if (! element.checked) {
                    continue;
                }
            }

            var val = element.value;
            console.log(val);
            // Deals with toggles
            if (val == "on") {
                val = 1;
            }
            else if (val == "off") {
                val = 0;
            }
            result += `${element.name}=${val}\n`;
        }
        
    }

    result = result.trim();
    document.getElementById('container').style.display = "none";
    document.getElementById('results').innerHTML = result;
    // download(result, "config.ini", "text/plain");
}

// Function to download data to a file
function download(data, filename, type) {
    var file = new Blob([data], { type: type });
    if (window.navigator.msSaveOrOpenBlob) // IE10+
        window.navigator.msSaveOrOpenBlob(file, filename);
    else { // Others
        var a = document.createElement("a"),
            url = URL.createObjectURL(file);
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        setTimeout(function () {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
        }, 0);
    }
}