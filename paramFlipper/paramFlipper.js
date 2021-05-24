
var global = {
  dashboard: undefined,
  stepsize: undefined,
  max: undefined,
  min: undefined,
  parameter: undefined,
  currentlyPlaying: undefined,
  interval: undefined,
  timeUnits: undefined,
  dateTimeUnits: undefined,
  currentVal: undefined,
  selParam: undefined,
  loopInfinitely: undefined

}

$('.collapse').collapse({toggle: false})

// initialized variables that will be used throughout the program
tableau.extensions.initializeAsync().then(()=>{
    global.timeUnits = ['days', 'weeks', 'months', 'quarters', 'years'] // list of time units for looping through parameters
    global.dateTimeUnits = ['seconds', 'minutes', 'hours','days', 'weeks', 'months', 'quarters', 'years']
    global.currentlyPlaying = false  
    $('#timeU').collapse('hide')
    $('#play').hide()
    setParameterList();
    getParameterMinMax();// creates list of parameters in UI
    console.log("InitializeAsync()");  
    global.dashboard = tableau.extensions.dashboardContent.dashboard; // initializes dashboard so that parameters can be accesssed
    console.log(global.dashboard); 
  })


function findParameter() { // finds user inputed parameter, shows play pause button, and runs loop
    getInputValues();
    tableau.extensions.dashboardContent.dashboard.getParametersAsync().then(params => {
        global.parameter = params.find(param => param.name === global.selParam);
    paraLoop();
    });
} 

function paraLoop() { // checks for user input error and runs each loop
    $('#play').show()
  
    var hasErrors = checkInputErrors()
    if (hasErrors == true) {
      return;
    }
    
     clearInterval(global.interval)
     global.currentVal = global.min;
     $('.results').html(global.currentVal)
     global.currentlyPlaying = true;
    
    if (global.parameter.allowableValues.type == 'range' && global.parameter.dataType != 'date' && global.parameter.dataType != 'date-time')  { // range + number case
      global.interval = rangeLoop();
      $('#play')[0].onclick = (function() {playPause()});
    }
    else if (global.parameter.allowableValues.type == 'list') {  // list case
      global.currentVal = 0 
      global.interval = listLoop()
      $('#play')[0].onclick = (function() {playPause()} );
    }
    else if (global.parameter.dataType == 'date' && global.parameter.allowableValues.type == 'range') { // range + date case
      global.parameter.changeValueAsync(global.min)
      global.interval = rangeDateLoop();
      $('#play')[0].onclick = (function() {playPause()} );
    }
    else if (global.parameter.dataType == 'date-time' && global.parameter.allowableValues.type == 'range') { // range + date-time case
      global.parameter.changeValueAsync(global.min)
      global.interval = rangeDateTimeLoop();
      $('#play')[0].onclick = (function() {playPause()} );
    }
}

function getInputValues () { // gets User inputed values
    global.time = parseFloat($('#time').val())*1000
    global.stepsize = parseFloat($('#stepsize').val())
    global.selParam = $('#parameter').val()
    tableau.extensions.dashboardContent.dashboard.getParametersAsync().then(params => {
        global.parameter = params.find(param => param.name === global.selParam)
        if (global.parameter.dataType != ('date')  && global.parameter.dataType != 'date-time') {
          $('#min')[0].type = 'text'
          $('#max')[0].type = 'text'
          global.min = parseFloat($('#min').val())
          global.max = parseFloat($('#max').val())
        }
        else if (global.parameter.dataType == 'date-time' && global.parameter.allowableValues.type != 'list') {
          $('#min')[0].type = 'datetime-local'
          $('#max')[0].type = 'datetime-local'
          global.min = $('#min').val().replace(/T/g," ") // adjusts tableau date-time format to javascript format
          global.max = $('#max').val().replace(/T/g," ")
          $('#timeU').collapse('show')
        }
        else if (global.parameter.dataType == 'date' && global.parameter.allowableValues.type != 'list') {
          $('#min')[0].type = 'date' // makes min/max input into date
          $('#max')[0].type = 'date'
          global.min = $('#min').val()
          global.max = $('#max').val()
          $('#timeU').collapse('show')
        }
      })
}

function setParameterList () { // sets list of parameters in UI
  var paramList = []
  tableau.extensions.dashboardContent.dashboard.getParametersAsync().then(para => {for (var j in para) {
    paramList.push(para[j].name)
    // issue here, breaks when parameter has multiple words in title 
    $('#parameter').append("<option value='" + paramList[j] + "'>" + paramList[j] + "</option>");
    console.log(paramList);
    console.log($('#parameter'));
    global.selParam = $('#parameter').val()
   } 
 }) 
}

function getParameterMinMax () { // extracts maximum and minimum values of a parameter (If they exist)
  getInputValues()
    var minval, maxval;

   global.selParam = $('#parameter').val()
   // $('#timeU').collapse('hide')
    
    tableau.extensions.dashboardContent.dashboard.getParametersAsync().then(para => {
      global.parameter = para.find(para => para.name === global.selParam)
      if (global.parameter.allowableValues.type != 'list') {
        minval = global.parameter.allowableValues.minValue.value
        maxval = global.parameter.allowableValues.maxValue.value
      }
        if (global.parameter.dataType == 'date-time' && minval != null) { // tableau outputs dates in non-standard format, converts to javascript format
            minval = minval.replace(/ /g, "T")
            $('#min').val(minval)
        }
        else if (minval != null) {
            $('#min').val(minval)
        }
        if (global.parameter.dataType == 'date-time' && maxval != null) {
            maxval = maxval.replace(/ /g, "T")
            $('#max').val(maxval)
  
        }
        else if (minval != null) {
            $('#max').val(maxval)
        }
      
      if (global.parameter.allowableValues.type != 'list' ) {
        if (minval != null)
        $('#max')[0].max = maxval
        $('#min')[0].max = maxval
        if (maxval != null)
        $('#max')[0].min = minval
        $('#min')[0].min = minval
      }
   // this place is where }) originally was

      // shows and hides relevant input boxes, executed on select
    if (global.parameter.allowableValues.type == 'list') {
      $('#ss').collapse('hide')
      $('#minimum').collapse('hide')
      $('#maximum').collapse('hide')
      $('#timeU').collapse('hide')
      console.log('hidden')
    }
    else if (global.parameter.allowableValues.type == 'range') {
      $('#ss').collapse('show')
      $('#minimum').collapse('show')
      $('#maximum').collapse('show')
        if (global.parameter.dataType == 'date-time' && global.parameter.allowableValues.type != 'list') {
          removeOptions($('#timeUnits'))
            for (var i = 0; i<(global.dateTimeUnits.length); i++) {
            $('#timeUnits').append("<option value='" + global.dateTimeUnits[i] + "'>" + global.dateTimeUnits[i] + "</option>")
            }
          $('#timeU').collapse('show')
          }
        else if (global.parameter.dataType == 'date' && global.parameter.allowableValues.type != 'list') {
          removeOptions($('#timeUnits'))
            for (var i = 0; i<(global.timeUnits.length); i++) {
            $('#timeUnits').append("<option value='" + global.timeUnits[i] + "'>" + global.timeUnits[i] + "</option>")
            }
          $('#timeU').collapse('show')
          }
      else {
        $('#timeU').collapse('hide')
      }
    }
  })
}

function playPause() { // allows play pause button to work
  if (global.currentlyPlaying) {
    clearInterval(global.interval)
    $('#play').html("play")
 }
  else if (global.parameter.dataType == 'date' && global.parameter.allowableValues.type == 'range') { // range + date case
   global.interval = rangeDateLoop();
      $('#play').html("pause")
  }
  else if (global.parameter.dataType == 'date-time' && global.parameter.allowableValues.type == 'range') { // range + date-time case
   global.interval = rangeDateTimeLoop();
      $('#play').html("pause")
  }
  else if (global.parameter.allowableValues.type == 'list') {
    global.interval = listLoop()
      $('#play').html("pause")
  }
  else if (global.parameter.allowableValues.type == 'range' && global.parameter.dataType != 'date' && global.parameter.dataType != 'date-time') {
    global.interval = rangeLoop()
      $('#play').html("pause")
  }
  global.currentlyPlaying = !global.currentlyPlaying;
}



function rangeLoop() {// creates interval that iterates parameter for user specified time
  if(global.time) {
    global.interval = setInterval(function(){
    //this runs continuously if global.time is NaN
      global.parameter.changeValueAsync(global.currentVal).then( val => {
        $('.results').html(val.value) })
        if ((global.currentVal + global.stepsize) >= global.max) {
            global.parameter.changeValueAsync(global.currentVal).then( val2 => {
            $('.results').html(val2.value)})
            if ($('#infinite').prop('checked')) {
              setTimeout(function() {paraLoop()}, global.time)
            } else {
              clearInterval(global.interval)
            }
        } else {
          global.currentVal += global.stepsize;
        }
      } , global.time);
      return global.interval;
  }
}

function listLoop() {  // loop for list parameters
  global.max = global.parameter.allowableValues.allowableValues.length - 1
    global.interval = setInterval(()=>{
    console.log(global.currentVal);
    global.parameter.changeValueAsync(global.parameter.allowableValues.allowableValues[global.currentVal].value).then( val => {  // inconsitency without the use of async function
    $('.results').html(val.value)})
    if(global.currentVal >= global.max){
      if ($('#infinite').prop('checked')) {
        setTimeout(function(){paraLoop()},global.time)
      }
      else {
      clearInterval(global.interval)
      }
    }global.currentVal += 1;
  }, global.time);
    return global.interval;
}

function rangeDateLoop() { // loop for standard date parameters
  let x, y, deltime, delunit
  deltime = parseFloat($('#stepsize').val())
  delunit = $('#timeUnits').val()
  let d = new Date(global.max)
  global.interval = setInterval(() => {
    x = (global.parameter.currentValue.value)
    let y = moment(x).add(deltime,delunit).format('YYYY-MM-DD')
    global.parameter.changeValueAsync(y).then( dat => {
    $('.results').html(dat.value)})
    let cd = new Date(y)
      if (cd >= d) {
        global.parameter.changeValueAsync(global.max).then( dat2 => {
        $('.results').html(dat2.value)})
        if ($('#infinite').prop('checked')) {
        setTimeout(function() {paraLoop()}, global.time)    
        }
        else {
        clearInterval(global.interval)
        }
      }
    }
    ,global.time) ;
    return global.interval;
}

function rangeDateTimeLoop() { // date-time parameter
  let x, y, deltime, delunit
  deltime = parseFloat($('#stepsize').val())
  delunit = $('#timeUnits').val()
  let d = new Date(global.max)
  global.interval = setInterval(() => {
    x = (global.parameter.currentValue.value)
    let y = moment(x).add(deltime,delunit).format('YYYY-MM-DD hh:mm:ss a')
    global.parameter.changeValueAsync(y).then( dat => {
    $('.results').html(dat.value)})
    let cd = new Date(y)
      if (cd >= d) {
        global.parameter.changeValueAsync(global.max).then( dat2 => { 
        $('.results').html(dat2.value) })
        if ($('#infinite').prop('checked')) {
          setTimeout(function() {paraLoop()}, global.time) 
        }
        else {
        clearInterval(global.interval)
        }
      }
  },global.time);
    return global.interval;
}

function removeOptions(selectElement) { // removes options from relevant 
   var i, L = selectElement[0].options.length - 1;
   for(i = L; i >= 0; i--) {
      selectElement[0].remove(i);
   }
}

function checkInputErrors () { // checks for various user input errors and displays modal right afterwards (may need work as css doesnt like rapid opening and closing of modals)
  if (global.min > global.max ){
    window.alert('error: you have set min greater than max')
    $('#bigModal').modal('show')
    return true;
    }
  if (global.time <= 0 ) {
    window.alert('error: you must input a positive time')
   $('#bigModal').modal('show')
   return true;
   }
  if (global.stepsize <= 0) {
    window.alert('error: you must input a positive step size')
    $('#bigModal').modal('show')
    return true;
  }
 if (global.parameter.allowableValues.type == 'range' && global.parameter.dataType != 'date' && global.parameter.dataType != 'date-time') {
    if (global.min < parseFloat(global.parameter.allowableValues.minValue.value)) {
      window.alert('error: you have set your min less than the minimum value of your parameter in tableau')
      $('#bigModal').modal('show')
      return true;
    } 
    if (global.min > parseFloat(global.parameter.allowableValues.maxValue.value)) {
      window.alert('error: you have set your min greater than the maximum value of your parameter in tableau')
      $('#bigModal').modal('show')
      return true;
    }
    if (global.max > parseFloat(global.parameter.allowableValues.maxValue.value)) {
      window.alert('error: you have set your max greater than the maximum value of your parameter in tableau')
      $('#bigModal').modal('show')
      return true;
    }
    if (global.min > parseFloat(global.parameter.allowableValues.maxValue.value)) {
      window.alert('error: you have set your max less than the minimum value of your parameter in tableau')
      $('#bigModal').modal('show')
      return true;
    }
  }
  else if (global.parameter.allowableValues.type=='range') {
    let maxd = new Date(global.parameter.allowableValues.maxValue.value)
    let mind = new Date(global.parameter.allowableValues.minValue.value)
    let maxInputd = new Date(global.max)
    let minInputd = new Date(global.min)
    if (maxInputd > maxd) {
      window.alert('error: you have set your max date after the latest value of your parameter in tableau')
      $('#bigModal').modal('show')
      return true;
    }
    if (maxInputd < mind) {
      window.alert('error: you have set your max date before the earliest date of your parameter')
      $('#bigModal').modal('show')
      return true;
    }
    if (minInputd < mind) {
      window.alert('error: you have set your min date before the earliest date of your parameter')
      $('#bigModal').modal('show')
      return true;
    }
    if (minInputd > maxd) {
      window.alert('error: you have set your min date later than the latest date of your parameter')
      $('#bigModal').modal('show')
      return true;
    }
  }
  else {
    return false
  }
  
}
