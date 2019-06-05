function startTime() {
  //Function to receive current time
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('txt').innerHTML =
        h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
}

function mins_into_left(sched) {
  //Function used to determine which period we are currently in and
  //make that period appear red
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var a; //minutes into
    var b; // minutes left
    console.log(sched);
}

function all(sched) {
  //runs other functions
    console.log(sched);
    startTime();

    mins_into_left(sched);
}

function checkTime(i) {
  //for consistency of time format
    if (i < 10) {
        i = "0" + i
    }
    ;  // add zero in front of numbers < 10
    return i;
}

document.addEventListener("DOMContentLoaded", function (e) {
  //adds to the DOM
    startTime();
    mins_into_left();
});
