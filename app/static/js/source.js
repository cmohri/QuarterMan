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

function mins_into_left() {
  //Function used to determine which period we are currently in and
  //make that period appear red
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var a; //minutes into
    var b; // minutes left
    if (h == 8) {
        if (m <= 41) {
            a = m;
            b = 41 - m;
            document.getElementById("period1").style.color = "red";
        } else if (m <= 45) {
            a = m - 41;
            b = 45 - m;
            document.getElementById("period1").style.color = "red";
            document.getElementById("period2").style.color = "red";
        } else {
            a = m - 45;
            b = 26 + 60 - m;
            document.getElementById("period2").style.color = "red";
        }
    } else if (h == 9) {
        if (m <= 26) {
            document.getElementById("period2").style.color = "red";
            a = 15 + m;
            b = 26 - m;
        } else if (m <= 31) {
            a = m - 26;
            b = 31 - m;
            document.getElementById("period2").style.color = "red";
            document.getElementById("period3").style.color = "red";
        } else {
            a = m - 31;
            b = 15 + 60 - m;
            document.getElementById("period3").style.color = "red";
        }
    } else if (h == 10) {
        if (m <= 15) {
            a = 29 + m;
            b = 15 - m;
            document.getElementById("period3").style.color = "red";
        } else if (m <= 20) {
            a = m - 15;
            b = 20 - m;
            document.getElementById("period3").style.color = "red";
            document.getElementById("period4").style.color = "red";
        } else {
            a = m - 20;
            b = 1 + 60 - m;
            document.getElementById("period4").style.color = "red";
        }
    } else if (h == 11) {
        if (m <= 1) {
            a = 40 + m;
            b = 1 - m;
            document.getElementById("period4").style.color = "red";
        } else if (m <= 6) {
            a = m - 1;
            b = 6 - m;
            document.getElementById("period4").style.color = "red";
            document.getElementById("period5").style.color = "red";
        } else if (m <= 47) {
            a = m - 6;
            b = 47 - m;
            document.getElementById("period5").style.color = "red";
        } else if (m <= 52) {
            a = m - 47;
            b = 52 - m;
            document.getElementById("period5").style.color = "red";
            document.getElementById("period6").style.color = "red";
        } else {
            a = m - 52;
            b = 33 + 60 - m;
            document.getElementById("period6").style.color = "red";
        }
    } else if (h == 12) {
        if (m < 33) {
            a = 8 + m;
            b = 33 - m;
            document.getElementById("period6").style.color = "red";
        } else if (m < 38) {
            a = m - 31;
            document.getElementById("period6").style.color = "red";
            b = 38 - m;
            document.getElementById("period7").style.color = "red";
        } else {
            a = m - 38;
            b = 19 + 60 - m;
            document.getElementById("period7").style.color = "red";
        }
    } else if (h == 13) {
        if (m <= 19) {
            a = 22 + m;
            b = 19 - m;
            document.getElementById("period7").style.color = "red";
        } else if (m <= 24) {
            a = m - 19;
            b = 24 - m;
            document.getElementById("period7").style.color = "red";
            document.getElementById("period8").style.color = "red";
        } else {
            a = m - 24;
            b = 5 + 60 - m;
            document.getElementById("period8").style.color = "red";
        }
    } else if (h == 14) {
        if (m <= 5) {
            a = 36 + m;
            b = 5 - m;
            document.getElementById("period8").style.color = "red";
        } else if (m <= 9) {
            a = m - 5;
            b = 9 - m;
            document.getElementById("period8").style.color = "red";
            document.getElementById("period9").style.color = "red";
        } else if (m <= 50) {
            a = m - 9;
            b = 50 - m;
            document.getElementById("period9").style.color = "red";
        } else if (m <= 54) {
            a = m - 50;
            b = 54 - m;
            document.getElementById("period9").style.color = "red";
            document.getElementById("period10").style.color = "red";
        } else {
            a = m - 54;
            b = 35 + 60 - m;
            document.getElementById("period10").style.color = "red";
        }
    } else if (h == 13) {
        if (m <= 35) {
            a = 6 + m;
            b = 35 - m;
            document.getElementById("period10").style.color = "red";
        } else {
            a = 30000;
            b = 30000;
        }
    }
    if (a != 0) {
        a -= 1;
    }
    if (b != 0) {
        b -= 1;
    }

    document.getElementById('minutes_into').innerHTML = checkTime(a);
    document.getElementById('minutes_left').innerHTML = checkTime(b);
    var t = setTimeout(mins_into_left, 500);
    //return (a, b);
}

function all() {
  //runs other functions
    startTime();
    mins_into_left();
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
