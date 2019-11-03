var taskStartTime;
var taskEndTime;
    
$(document).ready(function() {
    $('.btnStartTask').click(function() {
        $('.btnStartTask').attr("disabled","disabled");
        $('#gridModelSnippets').css('visibility','visible');
        $('.quest1Content').css('visibility','visible');
        startTime();
    });

    $('.btnStartQuest1').click(function() {             
        $('.btnStartQuest1').attr("disabled","disabled");
        $('.slcQuest1').attr("disabled",true);
        $('.quest2Content').css('visibility','visible');  
        endTime();            
        //computar o tempo em segundos
        //atribuir o tempo a uma variável hidden
        timeDiff = (taskEndTime - taskStartTime)/1000;
        timeDiff = timeDiff.toFixed(2);
        $('#id_secondsToAnswer').val(timeDiff);
    });      

    $('.slcQuest1').change(function() {
        if($('.slcQuest1').val()==''){
            $('.btnStartQuest1').attr("disabled",true);
        }else{             
            $('.btnStartQuest1').attr("disabled",false);
            $('.quest2Content').css('visibility','hidden'); 
        }
    });  

    //resolve o problema dos compoenentes do form quando estão 'disbaled'
    $('form').submit(function(e) {
        $(':disabled').each(function(e) {
            $(this).removeAttr('disabled');
        })
    });
    
});



function startTime(){
    taskStartTime =  new Date().getTime();    
}

function endTime(){
    taskEndTime = new Date().getTime();    
}