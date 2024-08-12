function ajaxCall( params, cb) {

    // Creating Our XMLHttpRequest object 
    let xhr = new XMLHttpRequest();

    // Making our connection  
    let url = 'https://jsonplaceholder.typicode.com/todos/1';
    xhr.open(params.method, params.url, true);
    xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8')


    // function execute after request is successful 
    xhr.onreadystatechange =  function () {
        if (this.readyState == 4 && this.status == 200) {
            cb(JSON.parse(this.responseText))
            }
        }
    // Sending our request 
    xhr.send(params.payload);
}


function updateIdentDropdown(data){
    sel = document.getElementById("ident")
    while (sel.options.length > 0){
        sel.remove(0)
    }
    for (animal of data){
        opt = document.createElement('option')
        opt.value = animal.ident
        opt.innerHTML = animal.ident
        sel.appendChild(opt)
    }

}

function init(){
    refreshAnimal();
    refreshLitter()

}


function refreshAnimal() {
    animalDomNode = document.getElementById("animalList")
    animalDomNode.innerHTML = ''
    ajaxCall({"method": "GET", "url": '/animal/v1_0/'}, 
        function (data){
            data.forEach (function (animal){
                text = "ident: "+animal.ident+
                " birthDate:"+animal.birthDate+
                " litterId:"+animal.litterId+
                " farmId:"+animal.farmId+
                " events: <br>"
                animal.events.forEach(function(animalEvent){
                    text += "<ol> "+animalEvent.eventName + animalEvent.eventData.testDate+"</ol>"
                })                
                thisLine = document.createElement("li")
                thisLine.innerHTML = text
                animalDomNode.appendChild(thisLine)

            })

            updateIdentDropdown(data)
        }
    )
}

function refreshLitter() {
    litterDomNode = document.getElementById("litterList")            
    litterDomNode.innerHTML = ''
    ajaxCall({"method": "GET", "url": '/litter/v1_0/'}, 
        function (data){
            data.forEach (function (litter){
                text = "id: "+litter.litterId+
                " sire:"+litter.sire+
                " dam:"+litter.dam
                thisLine = document.createElement("li")
                thisLine.innerText = text
                litterDomNode.appendChild(thisLine)

            })
        }
    )
}

function addEvent(){
    ident = document.getElementById('ident').value
    testDate = document.getElementById('testDate').value
    weight = document.getElementById('weight').value
    score = document.getElementById('score').value
    payload = {ident, testDate, weight, score};
    console.log(payload)

    ajaxCall({"method": "POST", "url": '/event/v1_0/onTest', "payload": JSON.stringify(payload)}, 
        refreshAnimal
    )
}