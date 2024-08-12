$(document).ready(function() {
    $(".nav-link").removeClass("active");

    $(".nav-link").each(function() {
        if (this.href == window.location.href) {
            $(this).addClass("active");
        }else{
            $(this).removeClass("active");
        }
    });
    
    $(".vertical-center-4").slick({
      dots: true,
      vertical: true,
      centerMode: true,
      slidesToShow: 4,
      slidesToScroll: 2
    });
    $(".vertical-center-3").slick({
      dots: true,
      vertical: true,
      centerMode: true,
      slidesToShow: 3,
      slidesToScroll: 3
    });
    $(".vertical-center-2").slick({
      dots: true,
      vertical: true,
      centerMode: true,
      slidesToShow: 2,
      slidesToScroll: 2
    });
    $(".vertical-center").slick({
      dots: true,
      vertical: true,
      centerMode: true,
    });
    $(".vertical").slick({
      dots: true,
      vertical: true,
      slidesToShow: 3,
      slidesToScroll: 3
    });
    $(".regular").slick({
      dots: true,
      infinite: true,
      slidesToShow: 3,
      slidesToScroll: 3
    });
    $(".center").slick({
      dots: true,
      infinite: true,
      centerMode: true,
      slidesToShow: 5,
      slidesToScroll: 3
    });
    $(".variable").slick({
      dots: true,
      infinite: true,
      variableWidth: true
    });
    $(".lazy").slick({
      lazyLoad: 'ondemand', // ondemand progressive anticipated
      infinite: true
    });



    setTimeout(function(){
      $(".pic1").hide();
      $(".pic2").show();
    },2000);

    $("#adrssubmit").click(function(){
      
      var order_address=$("#inputAddress").val();
      var order_landmark=$("#landmark").val();
      var order_pincode=$("#pincode").val();
      var order_phone=$("#phone").val();
      

      if (order_address=="" || order_landmark=="" || order_phone=="" || order_pincode==""){
        alert("required fields should not br blank")

      }else{

        $("#adrsform").submit();
      }
    })


  });