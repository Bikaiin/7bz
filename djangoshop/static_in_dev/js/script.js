$(document).ready(function(){
    var scrValue = $('img.bigimg').attr('src');
    $('#gallery a').on('click',function(e){
    e.preventDefault();
    scrValue = $(this).attr('href');
    $('img.bigimg').attr('src', scrValue)
    })

})