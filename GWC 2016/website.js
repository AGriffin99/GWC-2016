
  function changeImage() {
    var words = document.getElementById("pic1");

    if(words.src.match("keep-calm-and-coding--18.jpg")) {
      words.src = "coding-super-power.jpg";


    }else{words.src="keep-calm-and-coding--18.jpg" ;}


  }


  function changeCircle(){
    var soleil = document.getElementById("cirquedusoleil");
    if(soleil.fill== "blue"){soleil.fill= "yellow";}
    else{soleil.fill="blue";}
  }

  function OhmPun(){
    var ohms = document.getElementById("ohm");
    console.log(ohms.innerHTML);
    console.log(ohms.src);
    if(ohms.src.match("brunsell-cat.jpg")){ohms.src="sherlockohms.jpg";}
    else if(ohms.src.match("sherlockohms.jpg")){ohms.src="Ohm-Sweet-Ohm.jpg";}
    else if(ohms.src.match("Ohm-Sweet-Ohm.jpg")){ohms.src="dyinguncleohm.jpg";}
    else if(ohms.src.match("dyinguncleohm.jpg")){ohms.src="watt.jpg";}
    else if(ohms.src.match("watt.jpg")){ohms.src="ohmmy.jpe";}
    else if(ohms.src.match("ohmmy.jpe")){ohms.src="fetchdog.jpe";}
    else if(ohms.src.match("fetchdog.jpe")){ohms.src="wattislove.jpg";}
    else if(ohms.src.match("wattislove.jpg")){ohms.src="stop.jpg";}
    else if(ohms.src.match("stop.jpg")){ohms.src="joinus.jpg";}
    else if(ohms.src.match("joinus.jpg")){ohms.src="shocking.jpg";}
    else if(ohms.src.match("shocking.jpg")){ohms.src="ohmwithme.jpg";}
    else if(ohms.src.match("ohmwithme.jpg")){ohms.src="ohmslaw.jpg";}
    else if(ohms.src.match("ohmslaw.jpg")){ohms.src="badpun.jpg";}
    else if(ohms.src.match("badpun.jpg")){ohms.src="marriageohm.jpg";}
    else if(ohms.src.match("marriageohm.jpg")){ohms.src="electricians.jpg";}
    else if(ohms.src.match("electricians.jpg")){ohms.src="Math-Puns-are-the-First-Sine-of-Madness.jpg";}
    else if(ohms.src.match("Math-Puns-are-the-First-Sine-of-Madness.jpg")){ohms.src="thatsallfolks.gif";}
    else if(ohms.src.match("thatsallfolks.gif")){ohms.src="brunsell-cat.jpg";}
    else{ohms.src="brunsell-cat.jpg";}
  }
