function timeString(time){
    let hours = Math.floor(time / 3600);
    let minutes = Math.floor((time - hours * 3600) / 60);
    let seconds = time % 60;
    if (hours >= 12){
	post = "PM";
    }
    else {
	post = "AM";
    }
    if (hours == 12 || hours == 0) {
	//console.log(hours);
	tstr = 12;
    }
    else {
        //console.log(hours);
	tstr = hours % 12;
    }
    return tstr + ":" + ("0" + minutes).slice(-2) + ":" + ("0" + seconds).slice(-2) + " " + post;
}

function timeLoop(time, schedule){
    // Update the clock

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

    if (schedule[period].start >= time){

	document.getElementById("into_txt").innerHTML = "minutes after end";
        document.getElementById("left_txt").innerHTML = "minutes until start";
	

	var left = Math.floor ((schedule[period].start - time)/60 ); // until start
	var into =  Math.floor ((time + 86400 - schedule[schedule.length - 1].end )/60); // after end
	console.log (schedule[period].start - time);
	
	if (schedule[period].start - time < 1){

	    document.getElementById("into_txt").innerHTML = "minutes into";
            document.getElementById("left_txt").innerHTML = "minutes left";
	}
	

    } else if (schedule[period].end > time ){

	// Show minutes into/left
	var into = ( Math.floor((time - schedule[period].start) / 60));
	var left = ( Math.floor((schedule[period].end - time) / 60));
	// Highlight period
	document.getElementById("slot-" + period.toString()).style.color = "red";

    } else { // if end time is also less than time

	if (period + 1 < schedule.length){ // if not at end of schedule
	    // to handle transitions:
	    
	    var into = ( Math.floor ( (time - schedule[period].end)  / 60));
	    var left = ( Math.floor( ((schedule[period + 1].start - time) / 60)));
	    var n = period + 1;
	    document.getElementById("slot-" + period.toString()).style.color = "red";
	    document.getElementById("slot-" + n.toString()).style.color = "red";
	    
	    document.getElementById("into_txt").innerHTML = "minutes after";
	    document.getElementById("left_txt").innerHTML = "minutes before";
	    
	   // console.log( schedule[period + 1].start - time);
	    if ( (schedule[period + 1].start - time) < 1){
		document.getElementById("slot-" + period.toString()).style.color = "black";
		document.getElementById("into_txt").innerHTML = "minutes into";
		document.getElementById("left_txt").innerHTML = "minutes left";
	    }
	}
	else { // past end of schedule
	    var n = schedule.length - 1;
	    document.getElementById("slot-" + n.toString()).style.color = "black";
	    
	    var into = Math.floor ( (time - schedule[n].end )/60);
            var left = Math.floor ((schedule[0].start + (86400 - time)/60));

	    document.getElementById("into_txt").innerHTML = "minutes after end";
            document.getElementById("left_txt").innerHTML = "minutes until start";
	    
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
