function timeString(time){
    let hours = Math.floor(time / 3600);
    let minutes = Math.floor((time - hours * 3600) / 60);
    let seconds = time % 60;
    return hours % 12 + ":" + ("0" + minutes).slice(-2) + ":" + ("0" + seconds).slice(-2);
}

function timeLoop(time, schedule){
    // Update the clock
    timeText = document.getElementById("time");
    let hours = Math.floor(time / 3600);
    let minutes = Math.floor((time - hours * 3600) / 60);
    let seconds = time % 60;
    timeText.innerHTML = timeString(time);
    // Highlight period
    let period = 0;
    while(period < schedule.length && schedule[period].start < time){
        period += 1;
    }
    // Show minutes into/left
    setTimeout(timeLoop, 1000, time + 1, schedule);
}

function initialize(schedule){
    let t = new Date()
    timeLoop(t.getHours() * 3600 + t.getMinutes() * 60 + t.getSeconds(), schedule);
}
