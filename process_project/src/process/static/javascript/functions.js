
function sum(){

    var number1 = document.getElementById("number1").value
    var number2 = document.getElementById("number2").value

    var params = "number1="+number1+"&number2="+number2
    var req = new XMLHttpRequest()
    req.open("POST", "/process", true)
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")

    req.onreadystatechange = function(){
        console.log("function called")
        console.log("readystate " + req.readystate)
        if (req.readyState === 4){
            if (req.status === 200){
                console.log("Returned 200")
                text = "<p>" + number1 + " + " + number2 + " = " + req.responseText + "</p>"
                document.getElementById("results").innerHTML += text

                document.getElementById("number1").value = ""
                document.getElementById("number2").value = ""
                document.getElementById("number1").focus()
                document.getElementById("number1").select()
            }else{
                showDialog(req.responseText, 10000)

            }
        }

    };

    req.send(params)
    console.log("parameters sent " + params)
}

var dialogTimeout;

function showDialog(msg, time){
    var dialog = document.getElementById("dialog")
    var dialogText = document.getElementById("dialog-text")
    dialogText.innerHTML = msg
    dialog.style.display = "block"
    dialogTimeout = setTimeout(closeDialog, time);

}

function closeDialog(){
    clearTimeout(dialogTimeout)
    var elem = document.getElementById("dialog")
    elem.style.display = "none"
}