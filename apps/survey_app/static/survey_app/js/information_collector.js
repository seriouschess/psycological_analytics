var time = 0; //seconds
var clicks = 0;
var keys_pressed = 0;
var backspaces = 0;

function increment_time(){
    time += 1;
}

function increment_clicks(){
    clicks += 1;
}

function increment_keypress(){
    keys_pressed += 1;
}

function keyDown(/** @type {KeyboardEvent} */ ev){
    switch(ev.keyCode){
      case 8: //backspace
        backspaces += 1;
    }
}

setInterval(increment_time, 1000)
document.body.addEventListener("click", increment_clicks, true);
document.body.addEventListener("keyup", increment_keypress, true);
document.body.addEventListener("keyup", increment_keypress, true);
document.body.addEventListener("keydown", keyDown);

function sendItAway(){
    document.forms['survey_part_a'].elements['time'].value = time;
    document.forms['survey_part_a'].elements['clicks'].value = clicks;
    document.forms['survey_part_a'].elements['keys_pressed'].value = keys_pressed;
    //document.getElemenetById("time").value = time
    //document.getElemenetById("clicks").value = clicks
    //document.getElemenetById("keys_pressed").value = keys_pressed
    document.getElementById("survey_part_a").submit();
}

function sendItAgain(){
    document.forms['survey_part_b'].elements['time'].value = time;
    document.forms['survey_part_b'].elements['clicks'].value = clicks;
    document.forms['survey_part_b'].elements['keys_pressed'].value = keys_pressed;
    document.forms['survey_part_b'].elements['backspaces'].value = backspaces; //only exists in form b
    //document.getElemenetById("time").value = time
    //document.getElemenetById("clicks").value = clicks
    //document.getElemenetById("keys_pressed").value = keys_pressed
    document.getElementById("survey_part_b").submit();
}


//well that was a fun waste of 2 hours
// $(document).ready(function(){ //wait for DOM
//     $("select,input").change(function ()
//     {
//       jQuery(function($) {  //track mouse movement
//           var currentMousePos = { x: -1, y: -1 };
//           $(document).mousemove(function(e) {
//               currentMousePos.x = e.pageX;
//               currentMousePos.y = e.pageY;
//           });
//
//           mouse_distance += currentMousePos.x
//           // ELSEWHERE, your code that needs to know the mouse position without an event
//           //if (currentMousePos.x < 10) {
//               // ....
//           //}
//       });
//     })
// });

// function add_mouse_distance(event){
//     Math.sqrt(Math.pow(Math.abs(event.clientX-last_mouse_pos[0]),2) + Math.pow(Math.abs(event.clienty-last_mouse_pos[1]),2))
// }
