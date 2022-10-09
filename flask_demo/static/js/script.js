

var $window = $(window);
var windowsize = $(window).width();



// fixing bottom nav to top on scrolliing
var $fixednav = $(".bottom-nav");
$(window).on("scroll", function () {
    var $heightcalc = $(window).height() - $fixednav.height();
    if ($(this).scrollTop() > $heightcalc) {
        $fixednav.addClass("navbar-bottom-top");
    } else {
        $fixednav.removeClass("navbar-bottom-top");
    }
});

/* ------- Smooth scroll ------- */
$("a.pagescroll").on("click", function (event) {
    event.preventDefault();
    $("html,body").animate({
        scrollTop: $(this.hash).offset().top
    }, 1200);
});

/*----- Menu On click -----*/
if ($("#sidemenu_toggle").length) {
    $("body").addClass("pushwrap");
    $("#sidemenu_toggle").on("click", function () {
        $(".pushwrap").toggleClass("active");
        $(".side-menu").addClass("side-menu-active"), $("#close_side_menu").fadeIn(700)
    }), $("#close_side_menu").on("click", function () {
        $(".side-menu").removeClass("side-menu-active"), $(this).fadeOut(200), $(".pushwrap").removeClass("active")
    }), $("#btn_sideNavClose").on("click", function () {
        $(".side-menu").removeClass("side-menu-active"), $("#close_side_menu").fadeOut(200), $(".pushwrap").removeClass("active")
    });
}

/* ===================================
     Equal Heights
     ====================================== */
checheight();
$window.on("resize", function () {
    checheight();
});

function checheight() {
    var $smae_height = $(".equalheight");
    if ($smae_height.length) {
        if (windowsize > 767) {
            $smae_height.matchHeight({
                property: "height",
            });
        }
    }
}

/* ===================================
     Features Section Number Scroller
     ====================================== */

$(".stats").appear(function () {
    $('.numscroller').each(function () {
        $(this).prop('Counter',0).animate({
            Counter: $(this).text()
        }, {
            duration: 5000,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now));
            }
        });
    });
});
/* ===================================
       Parallax
   =================================== */
if (windowsize > 992) {
    $(".parallaxie").parallaxie({
        speed: 0.4,
        offset: 0,
    });
}

/* Brand Carousel */
$('.brand-carousel').owlCarousel({
    margin: 75,
    nav: false,
    navText: [
        '<i class="ti ti-angle-left"></i>',
        '<i class="ti ti-angle-right"></i>'
    ],
    dots: false,
    autoWidth: false,
    autoplay: 300,
    autoplayHoverPause: false,
    loop: true,
    responsive: {
        0: {
            items: 1
        },
        480: {
            items: 2
        },
        600: {
            items: 4
        },
        1000: {
            items: 5
        }
    }
});

/* ===================================
           Testimonial Two
   =================================== */

$('.testimonial-two').owlCarousel({
    loop: true,
    smartSpeed: 500,
    responsiveClass: true,
    nav:false,
    dots:false,
    autoplay: true,
    autoplayHoverPause: true,
    autoplayTimeout: 3000,
    responsive: {
        0: {
            items: 1,
            margin: 30,
        },
        480: {
            items: 1,
            margin: 30,
        },
        992: {
            items: 1,
            margin: 30,
        }
    }
})

/* ===================================
       Gallery 5
   ====================================== */

// isotope
var gallery5 = $('#gallery-5').isotope({
    // options
    itemSelector: '.items',
    // stamp elements
    stamp: '.stamp'
});

// filter items on button click
$('.gallery-filter-5').on('click', 'span', function () {

    var filterValue = $(this).attr('data-filter');
    gallery5.isotope({filter: filterValue});
    $(this).addClass('active').siblings().removeClass('active');
});

setTimeout(function () {
    $('.gallery-filter-2 .active,.gallery-filter-4 .active,.gallery-filter-5 .active').click();
}, 500);






$("#rev_slider_23_1").show().revolution({
    sliderType:"standard",
    jsFileLocation:"//revslider.ads:7080/revslider/public/assets/js/",
    sliderLayout:"fullscreen",
    dottedOverlay:"none",
    delay:9000,
    navigation: {
        keyboardNavigation:"off",
        keyboard_direction: "horizontal",
        mouseScrollNavigation:"off",
        mouseScrollReverse:"default",
        onHoverStop:"off",
        touch:{
            touchenabled:"on",
            touchOnDesktop:"off",
            swipe_threshold: 75,
            swipe_min_touches: 1,
            swipe_direction: "horizontal",
            drag_block_vertical: false
        }
    },
    responsiveLevels:[1240,1024,778,480],
    visibilityLevels:[1240,1024,778,480],
    gridwidth:[1240,1024,778,480],
    gridheight:[900,768,960,720],
    lazyType:"single",
    parallax: {
        type:"mouse",
        origo:"slidercenter",
        speed:300,
        speedbg:0,
        speedls:0,
        levels:[2,4,6,8,10,12,14,16,18,20,22,24,49,50,51,55],
    },
    shadow:0,
    spinner:"spinner2",
    stopLoop:"on",
    stopAfterLoops:0,
    stopAtSlide:1,
    shuffle:"off",
    autoHeight:"off",
    fullScreenAutoWidth:"off",
    fullScreenAlignForce:"off",
    fullScreenOffsetContainer: "",
    fullScreenOffset: "",
    disableProgressBar:"on",
    hideThumbsOnMobile:"off",
    hideSliderAtLimit:0,
    hideCaptionAtLimit:0,
    hideAllCaptionAtLilmit:0,
    debugMode:false,
    fallbacks: {
        simplifyAll:"off",
        nextSlideOnWindowFocus:"off",
        disableFocusListener:false,
    }
});

/* END OF revapi call */