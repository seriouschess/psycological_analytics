function drawGraph(element_id, x_label, y_label){
    /** @type {HTMLCanvasElement} */
    var canv = document.getElementById(element_id);
    var ctx = canv.getContext("2d");

    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canv.width, canv.height);

    ctx.strokeStyle = "white";
    ctx.lineWidth = 8;
    ctx.beginPath();
    ctx.moveTo(50, 50);
    ctx.lineTo(50, 350);
    ctx.lineTo(350, 350);
    ctx.stroke();
    var data = canv.innerHTML;
    var data_array = [];
    var stuff = "";

    for(var x=0; x<data.length ;x++){ //gets data and makes a single dimensional array of numbers
          if (isNaN(data.charAt(x))){
            if(stuff.length > 0){
              data_array.push(Number(stuff));
              stuff = "";
           }
        }else{
            stuff += data.charAt(x);
        }
    }
    var y;
    ctx.fillStyle = "pink";
    for(var i=0; i<=data_array.length; i+=2){ //plots points from data_array
      x = 30*data_array[i] + 50
      y = 350-30*data_array[i + 1]
      ctx.beginPath();
      ctx.arc(x, y, 5, 0, 2*Math.PI, true);
      ctx.fill();
    }

    ctx.font = "30px Arial";
    ctx.fillText(x_label, 100, 380); //x,y
    ctx.fillText(y_label, 20, 30); //x,y
}


function analyzeGraph(element_id, x_label, y_label){
    /** @type {HTMLCanvasElement} */
    var canv = document.getElementById(element_id);
    var ctx = canv.getContext("2d");

    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canv.width, canv.height);

    ctx.strokeStyle = "white";
    ctx.lineWidth = 8;
    ctx.beginPath();
    ctx.moveTo(50, 50);
    ctx.lineTo(50, 350);
    ctx.lineTo(350, 350);
    ctx.stroke();
    var data = canv.innerHTML;
    var data_array = [];
    var stuff = "";

    for(var x=0; x<data.length ;x++){ //gets data and makes a single dimensional array of numbers
          if (isNaN(data.charAt(x))){
            if(stuff.length > 0){
              data_array.push(Number(stuff));
              stuff = "";
           }
        }else{
            stuff += data.charAt(x);
        }
    }

    var max_x = data_array[0];
    for(var i=0; i<=data_array.length; i+=2){ //find maximum x
      if(max_x < data_array[i]){
        max_x = data_array[i]
      }
    }

    var y;
    ctx.fillStyle = "pink";
    for(var i=0; i<=data_array.length; i+=2){ //plots points from data_array
      x = (300/max_x)*data_array[i] + 50; //this is different from drawGraph!
      y = 350-30*data_array[i + 1];
      ctx.beginPath();
      ctx.arc(x, y, 5, 0, 2*Math.PI, true);
      ctx.fill();
    }

    ctx.font = "30px Arial";
    ctx.fillText(x_label, 100, 380); //x,y
    ctx.fillText(y_label, 20, 30); //x,y
}

drawGraph("anxiety_happiness", "anxiety level", "happiness level");
drawGraph("fitness_happiness", "fitness level", "happiness level");
drawGraph("confidence_happiness", "confidence level", "happiness level");
drawGraph("confidence_anxiety", "confidence level", "anxiety level");
drawGraph("confidence_fitness", "confidence level", "fitness level");
drawGraph("anxiety_fitness", "fitness level", "anxiety level");
analyzeGraph("backspaces_anxiety", "Num Backspaces", "anxiety_level");
analyzeGraph("time_fitness", "time(s) on survey", "fitness level");
analyzeGraph("clicks_confidence", "number of clicks", "confidence level")
