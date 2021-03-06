var taskStartTime;
var taskEndTime;
    
$(document).ready(function() {
    
    $('#instructionsModal').modal({
        keyboard: false,
        backdrop: 'static',
    });
    $('#instructionsModal').modal('show'); 

    $('#btnStartTask').click(function() {
        //$('.tab-content').css('visibility','visible');                
        $('#instructionsModal').modal('hide')
        try {
            // a biblioteca de tutorial (introjs) será ativada pela próxima linha, mas caso ela não seja necessária na tarefa em avaliação, o catch contorna o erro de chamar uma função que não existe.
            startIntro();
            startTime();
        }
        catch(err) {
            startTime();
        }
    });
        
    $('form').submit(function(e) {
        endTime();            
        //computar o tempo em segundos        
        timeDiff = (taskEndTime - taskStartTime)/1000;
        timeDiff = timeDiff.toFixed(2); //segundos com 2 casas decimais
        //atribui o tempo a uma variável hidden
        $('#id_secondsToAnswer').val(timeDiff);
    });

    $('#warmupModal').modal({
        keyboard: false,
        backdrop: 'static',
    });
    $('#warmupModal').modal('show'); 

    $('#btnStartWarmupTask').click(function() {                
        $('#warmupModal').modal('hide');                
        startIntro();
    });   
    
});

function startTime(){
    taskStartTime =  new Date().getTime();    
}

function endTime(){
    taskEndTime = new Date().getTime();    
}