$(document).ready(function(){
    var scrValue = $('img.bigimg').attr('src');
    $('#gallery a').on('click',function(e){
        e.preventDefault();
        scrValue = $(this).attr('href');
        $('img.bigimg').attr('src', scrValue)
    })


    $('#category a').on('click',function(e){
        e.preventDefault();
        alert('fdf');
        SendGet();


    }

})

function SendGet() {
    //отправляю GET запрос и получаю ответ
    $$a({
        type:'get',//тип запроса: get,post либо head
        url:'127.0.0.1:8000/shop/categoryjson/korobki-kryshka-dno/',//url адрес файла обработчика
        data:{'q':'1'},//параметры запроса
        response:'text',//тип возвращаемого ответа text либо xml
        success:function (data) {//возвращаемый результат от сервера
            $$('result',$$('result').innerHTML+'<br />'+data);
        }
    });
}
