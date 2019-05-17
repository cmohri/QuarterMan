function startTime() {
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


function mins_into_left(){
    var today = new Date();    
    var h = today.getHours();
    var m = today.getMinutes();                                                                                       
    var a; //minutes into
    var b; // minutes left
    if ( h == 8){
	if ( m <= 41){
            a= m;
	    b = 41 -m ;
	} else if (m <= 45) {
	    a = m - 41;
	    b = 45 -m;
	} else {
	    a = m - 45;
	    b = 26 + 60 - m;
	}
    } else if (h == 9) {
	if (m <= 26){
	    a = 15 + m;
	    b = 26 -m;
	} else if (m <= 31){
	    a = m - 26;
	    b = 31 -m;
	} else {
	    a = m - 31;
	    b = 15 + 60 - m;
	}
    } else if (h == 10){
	if (m <= 15){
	    a = 29 + m;
	    b = 15 -m;
	} else if (m <= 20){
	    a = m - 15;
	    b = 20 -m;
	} else {
	    a = m - 20;
	    b = 1 + 60 -m;
	}
    } else if (h == 11){
	if (m <= 1){
	    a = 40 + m;
	    b = 1 -m;
	} else if (m <= 6){
	    a = m - 1;
	    b = 6 -m;
	} else if (m <= 47){
	    a = m - 6;
	    b = 47 -m;
	} else if (m <= 52){
	    a = m - 47;
	    b = 52 -m;
	} else {
	    a = m - 52;
	    b = 33 + 60 -m;
	}
    } else if (h == 12){
	if (m <= 33){
	    a = 8 + m;
	    b = 33 -m;
	} else if (m <= 38){
	    a = m - 31;
	    b = 38 -m;
	} else {
	    a = m - 38;
	    b = 19 + 60 -m;
	}
    } else if (h == 13){
	if (m <= 19){
	    a = 22 + m;
	    b = 19 -m;
	} else if (m <= 24){
	    a = m - 19;
	    b = 24 -m;
	} else {
	    a = m - 24;
	    b = 5 + 60 -m;
	}
    } else if (h == 14){
	if (m <= 5){
	    a = 36 + m;
	    b = 5 -m;
	} else if (m <= 9){
	    a = m - 5;
	    b = 9-m;
	} else if (m <= 50){
	    a = m - 9;
	    b = 50 -m;
	} else {
	    a = m - 54;
	    b = 35 + 60 -m;
	}
    } else if (h == 13){
	if (m <= 35){
	    a = 6 + m;
	    b = 35 -m;
	} else {
	    a = 30000;
	    b = 30000;
	}
    }

    return (a, b);
}
	
                                 





function checkTime(i) {
  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
  return i;}
