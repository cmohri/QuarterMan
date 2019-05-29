let inputTemplateGenerator = (slot_id) =>
    `<div class = "row">
        <div class = "input-group col-lg-11 schedule-slot">
            <input class = "col-lg-8 col-md-6 form-control" placeholder="Schedule Slot Name"/>
            <span class = "input-group-append">Start Time: </span>
            <input class = "col-lg-2 col-md-3 form-control" placeholder="24 hour time"/>
            <span class = "input-group-append">End Time: </span>
            <input  class = "col-lg-2 col-md-3 form-control" placeholder="24 hour time"/>
        </div>
        <div class = "col-lg-1">
            <svg class = "remove-slot" width="20" height="20" xmlns="http://www.w3.org/2000/svg">
                <!-- Created with Method Draw - http://github.com/duopixel/Method-Draw/ -->
                <ellipse ry="10" rx="10" id="svg_1" cy="10" cx="10" stroke-width="0" stroke="#000" fill="#dc3545" fill-opacity="0.85"/>
                <rect id="svg_2" height="2.5" width="10" y="8.75" x="5" stroke-opacity="null" stroke-width="0" stroke="#000" fill="#ffffff"/>
            </svg>
        </div>
        <hr class = "input-divider">
    </div>`;

function addSlot(){
    let id = document.getElementsByClassName("schedule-slot").length;
    let new_slot = inputTemplateGenerator(id);
    let wrapper = document.createElement("div");
    wrapper.innerHTML = new_slot;
    document.getElementById("schedule-form").appendChild(wrapper.firstChild);
    new_slot = document.getElementById("schedule-form").lastChild;
    new_slot.getElementsByClassName("remove-slot")[0].addEventListener("click", function (e) {
        new_slot.parentNode.removeChild(new_slot);
    });
}

document.getElementById("add-slot").addEventListener("click", function () {
    addSlot();
});

document.addEventListener("DOMContentLoaded", function (e) {
    for(let i = 0; i < 5; i++){
        addSlot();
    }
});

function scheduleToJSON(){
    let schedule = [];
    for(let group of document.getElementsByClassName("schedule-slot")){
        let inputs = group.querySelectorAll("input");
        if(!validateSlot(inputs[0].value, inputs[1].value, inputs[2].value)){
            alert("Implement error message nicely");
            return;
        }
        schedule.push({
            "name": inputs[0].value,
            "start": inputs[1].value,
            "end": inputs[2].value
        });
    }
    document.getElementsByName("schedule")[0].value = JSON.stringify(schedule);
    document.getElementById("schedule-form").submit();
}

function validateSlot(name, start, end){
    return true;
}