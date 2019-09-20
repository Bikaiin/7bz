var domain = "http://127.0.0.1:8000";
$(document).ready(function(){
      var scrValue = $('#gallery a').attr('href');

    $('img.bigimg').attr('src', scrValue)

    $('#gallery a').on('click',function(e){
        e.preventDefault();

        scrValue = $(this).attr('href');
        $('img.bigimg').fadeOut("fast")
        $('img.bigimg').attr('src', scrValue);
        $('img.bigimg').fadeIn("fast")
    })
    $('.carousel-item:first').addClass('active')
    /*
    $('#category a').on('click',function(e){
        e.preventDefault();
        my_ref = $(this).attr('href');
        path = domain + my_ref ;
        console.log(path );
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

	        items = response.data
	        $.each(items, function(index, value){
                var html = '<div class=" col-12 col-md-6 col-lg-4 dk-isotope-grid-item mockups"><div class="card h-100"><a class="dk-portfolio-item dk-portfolio-item-style-2 dk-portfolio-item-light" href="'+value.slug+'"><span class="dk-portfolio-item-image"><span class="dk-portfolio-item-image-size" data-portfolio-size="90%"></span><span class="dk-portfolio-item-overlay" style="background-color: rgba(255, 255, 255, .35)"></span><img src="'+value.image_path+'"  alt=""><span class="dk-portfolio-item-info"><a class="text-dark" href="'+value.slug+'"><h2 class="h3 dk-portfolio-item-title">'+value.title+'</h2></a></span></a></div></div>'
                $('#product_list').append(html);
	        })

	        $('#collapse1').removeClass('show');
	        try {

                history.pushState(null, null, path);
                return;
            } catch(e) {}
            ocation.hash =  path;

	    })
    })
    */
    var btn = $('#button');

    $(window).scroll(function() {
        if ($(window).scrollTop() > 300) {
        btn.addClass('show');
        } else {
        btn.removeClass('show');
        }
    });

    btn.on('click', function(e) {
        e.preventDefault();
        $('html, body').animate({scrollTop:0}, '300');
    });


})



