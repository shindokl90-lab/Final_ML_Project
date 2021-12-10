var userInput = [];

function loadGrade(parameter) {
    
    console.log(parameter);
    var result = d3.select(".result").text(parameter);
    /*d3.json("/calculate").then(response => {
        userInput = response;
        //writeGrade();
        console.log("Hello");
    });*/
    
}



function postGrade() {
    var inputAmount = d3.select("#loanAmount").property("value");
    var inputHome = d3.select("#home").property("value");
    var inputEmployement = d3.select("#yearsOfEmployment").property("value");
    var inputFico = d3.select("#FICO").property("value");
    var inputAppType = d3.select("#appType").property("value");
    var inputIncome = d3.select("#income").property("value");
    console.log(inputAmount);
    console.log(inputHome);
    console.log(inputEmployement);
    console.log(inputFico);
    console.log(inputAppType);
    console.log(inputIncome);

    d3.json("/assessment", {
        method: "POST",
        body: JSON.stringify({
            "loanAmount": inputAmount,
            "home": inputHome,
            "yearsOfEmployement": inputEmployement,
            "FICO": inputFico,
            "appType": inputAppType,
            "income": inputIncome
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then(loadGrade);

}

d3.select("#Submit").on("click", postGrade)
