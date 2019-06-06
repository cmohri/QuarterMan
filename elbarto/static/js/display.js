function timeString(time){
    let hours = Math.floor(time / 3600);
    let minutes = Math.floor((time - hours * 3600) / 60);
    let seconds = time % 60;
    return hours % 12 + ":" + ("0" + minutes).slice(-2) + ":" + ("0" + seconds).slice(-2);
}

function timeLoop(time, schedule){
    // Update the clock
    console.log(time);
    timeText = document.getElementById("time");
    let hours = Math.floor(time / 3600);
    let minutes = Math.floor((time - hours * 3600) / 60);
    let seconds = time % 60;
    timeText.innerHTML = timeString(time);
    let period = 0;
    while (period < schedule.length && schedule[period].start < time){
	period += 1;
    }
    //console.log(period - 1);
    if (period != 0){
	period -= 1;
    }

    if (schedule[period].start > time){
	var into ="none";
	var left = "none";

    } else if (schedule[period].end > time ){

	// Show minutes into/left
	var into = ( Math.floor((time - schedule[period].start) / 60));
	var left = ( Math.floor((schedule[period].end - time) / 60));
	// Highlight period
	document.getElementById("slot-" + period.toString()).style.color = "red";
	
    } else { // if end time is also less than time

	if (period + 1 < schedule.length){ // if not at end of schedule
	    
	    var into = ( Math.floor ( (time - schedule[period].end)  / 60));
	    var left = ( Math.floor( ((schedule[period + 1].start - time) / 60)));
	    var n = period + 1;
	    document.getElementById("slot-" + period.toString()).style.color = "red";
	    document.getElementById("slot-" + n.toString()).style.color = "red";
	}
	else { // past end of schedule
	    var into ="none";
            var left = "none";
	}
	    
    }

    document.getElementById('minutes_into').innerHTML  = into;     
    document.getElementById("minutes_left").innerHTML = left;      


	
    
    setTimeout(timeLoop, 1000, time + 1, schedule);
}

function initialize(schedule){
    console.log(schedule);
    let t = new Date();
    timeLoop(t.getHours() * 3600 + t.getMinutes() * 60 + t.getSeconds(), schedule);
}
