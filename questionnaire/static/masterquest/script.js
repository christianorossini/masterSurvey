var taskStartTime;
var taskEndTime;
    
$(document).ready(function() {
    
    $('#instructionsModal').modal({
        keyboard: false,
        backdrop: 'static',
    });
    $('#instructionsModal').modal('show'); 

    $('#btnStartTask').click(function() {
        $('.tab-content').css('visibility','visible');                
        $('#instructionsModal').modal('hide')
        startTime();
    });
    
    //resolve o problema dos compoenentes do form quando estão 'disbaled'
    $('form').submit(function(e) {
        endTime();            
        //computar o tempo em segundos        
        timeDiff = (taskEndTime - taskStartTime)/1000;
        timeDiff = timeDiff.toFixed(2); //segundos com 2 casas decimais
        //atribui o tempo a uma variável hidden
        $('#id_secondsToAnswer').val(timeDiff);
    });
    
});



function startTime(){
    taskStartTime =  new Date().getTime();    
}

function endTime(){
    taskEndTime = new Date().getTime();    
}

