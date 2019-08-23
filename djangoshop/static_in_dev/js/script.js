var domain = "http://127.0.0.1:8000";
$(document).ready(function(){
      var scrValue = $('#gallery a').attr('href');

    $('img.bigimg').attr('src', scrValue)

    $('#gallery a').on('click',function(e){
        e.preventDefault();

        scrValue = $(this).attr('href');
        $('img.bigimg').attr('src', scrValue)
    })
    $('#category a').on('click',function(e){
        e.preventDefault();
        path = domain + $(this).attr('href');
        $('#product_list').empty();
        var settings = {
		    async: true,
		    crossDomain: true,
		    url: path,
		    method: "GET",
		    headers: {'X-Requested-With': 'XMLHttpRequest'},


		    dataType: "json",
		    contentType: "application/json",

		    data: { }
	    }
	    $.ajax(settings).done(function (response){

	        console.log(response.data );
	        history.pushState(null, null, path);
	        items = response.data
	        $.each(items, function(index, value){

                var html = '<div class="col-lg-4 col-md-6 mb-4"><div class="card h-100"><a href="#"><img class="card-img-top" src="'+value.image_path +'" alt="" "alt=""></a><div class="card-body"><h4 class="card-title"><a href="'+'#'+'">'+value.title+'</a></h4></div></div></div>';

                $('#product_list').append(html);
	        })

	    })
    })


})



