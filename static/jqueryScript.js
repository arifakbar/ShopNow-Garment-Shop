AOS.init();

var swiper = new Swiper('.s1',{
    init:true,
    direction:'horizontal',
    touchEventsTarget:'container',
    initialSlide: 0,
    speed: 300,
    loop:true,
    autoplay:true,
    effect: 'slide', //slide,fade,cube,coverflow,flip
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
})

var swiper = new Swiper('.s2',{
    init:true,
    direction:'horizontal',
    touchEventsTarget:'container',
    initialSlide: 0,
    speed: 300,
    loop:true,
    effect: 'slide', //slide,fade,cube,coverflow,flip
    slidesPerView: 4,
    spaceBetween: 30,
    pagination: {
        el: '.p1',
        clickable: true,
        renderBullet: function (index, className) {
            return `<span class="dot swiper-pagination-bullet"  style="margin:0px 5px"></span>`;
          }
      },
    autoHeight:false,
    setWrapperSize:false,
    autoplay:true
})
var swiper = new Swiper('.s3',{
    init:true,
    direction:'horizontal',
    touchEventsTarget:'container',
    initialSlide: 2,
    speed: 300,
    loop:true,
    effect: 'coverflow', //slide,fade,cube,coverflow,flip
    slidesPerView: 4,
    spaceBetween: 30,
    pagination: {
        el: '.p2',
        clickable: true,
        renderBullet: function (index, className) {
            return `<span class="dot swiper-pagination-bullet"  style="margin:0px 5px"></span>`;
          }
      },
    autoHeight:false,
    setWrapperSize:false,
    autoplay:true
})
var swiper = new Swiper('.s4',{
    init:true,
    direction:'horizontal',
    touchEventsTarget:'container',
    initialSlide: 1,
    speed: 300,
    loop:true,
    effect: 'slide', //slide,fade,cube,coverflow,flip
    slidesPerView: 4,
    spaceBetween: 30,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    autoHeight:false,
    setWrapperSize:false,
    autoplay:true
})
var swiper = new Swiper('.s5',{
    init:true,
    direction:'horizontal',
    slidesPerView: 3,
    slidesPerColumn: 2,
    touchEventsTarget:'container',
    initialSlide: 0,
    speed: 300,
    // loop:true,
    effect: 'slide', //slide,fade,cube,coverflow,flip
    spaceBetween: 30,
    pagination: {
        el: '.p5',
        clickable: true,
        renderBullet: function (index, className) {
          return '<span class="' + className + '">' + (index + 1) + '</span>';
        },
    },
    autoHeight:false,
    setWrapperSize:false,
    // autoplay:true
})

// .from('#bcimg1',{
//     opacity:0,
//     x:20,
//     duration:1,
//     ease: 'expo.easeInOut',
// })

$('document').ready(function(){
    $('.shliSide').click(function(){
        $('.shliMain').attr('src',this.src)
    })
})
