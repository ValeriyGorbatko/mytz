$( document ).ready(function() {
    if (window.location.hash == '#_=_') {
        window.location.hash = '';
        history.pushState('', document.title, window.location.pathname);
    }
     $('.answer').click(function(){
            $('.answer').next().hide();
            $('.answer').show();
            $(this).next().toggle();
            $(this).hide();
             $('textarea').val('');
        });

        $('.cancel').click(function(){
            $(this).closest('.hidden-block').prev().toggle();
            $(this) .closest('.hidden-block').toggle();
            $('textarea').val('');
        });

        $('.parent-block').click(function(){
            var className;
            $(this).siblings('.children').toggle();

            className = $(this).children().attr('class');
            if (className === 'glyphicon glyphicon-triangle-right') {
                $(this).children().removeClass(className);
                $(this).children().addClass('glyphicon glyphicon-triangle-bottom');
            } else if(className === 'glyphicon glyphicon-triangle-bottom') {
                $(this).children().removeClass(className);
                $(this).children().addClass('glyphicon glyphicon-triangle-right');
            }
    });
});



