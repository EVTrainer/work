<script>

</script>

<div id="timelineBlock">
    <img class="scrollArrow" src="img/gallery/triangle.png">
    <script>
      //formerly websiteScroll.js
      jQuery(window).scroll(function(){
      var h = document.documentElement,
          b = document.body,
          st = 'scrollTop',
          sh = 'scrollHeight';

      var percent = (h[st]||b[st]) / ((h[sh]||b[sh]) - h.clientHeight) * 100;

      if(percent <= 28.1){
        jQuery('.scrollArrow').css('margin-left',jQuery(this).scrollTop() / 46.7 + 'vh');
      }
      if(percent>28.1 && percent<=39.7){
        jQuery('.scrollArrow').css('margin-left',jQuery(this).scrollTop() / 32.9 + 'vh');
      }
      if(percent>39.7 && percent<=68.56){
        jQuery('.scrollArrow').css('margin-left',jQuery(this).scrollTop() / 37.53 + 'vh');
      }
    if(percent>68.56 && percent<=93.352){
        jQuery('.scrollArrow').css('margin-left',jQuery(this).scrollTop() / 38.8 + 'vh');
      }
      if(percent>93.352){
        document.getElementsByClassName("scrollArrow")[0].style.marginLeft = "108vh";
      }
    });
  </script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <img id="storyTimeline" src="img/icons/ourstory_timeline.png">
    <ul id="timeline">
      <li> <a href="">
          <p> &nbsp &nbsp &nbsp </p>
        </a> </li>
      <li> <a href="#makerspacePhoto">
          <p> &nbsp &nbsp &nbsp </p>
        </a> </li>
      <li> <a href="#pano278">
          <p> &nbsp &nbsp &nbsp </p>
        </a> </li>
      <li> <a href="#carpVideo">
          <p> &nbsp &nbsp &nbsp </p>
        </a> </li>
      <li> <a href="#nowPhoto">
          <p> &nbsp &nbsp &nbsp </p>
        </a> </li>
    </ul>
  </div>

<style>
  #timeline{
  display:flex;
  flex-direction: row;
  justify-content: space-between;
  width:100%;
  list-style:none;
  margin-left:-1vw;
  /* transform: translate(0, -150%); */
  }

  #timeline li:nth-child(5){
    margin-right:-.67vw;

  }
  #timeline p{

  }

  #timeline a{
    display:inline-block;
    position:relative;
    padding-top:1vh;
    margin-top:-1vh;
    color:var(--grack_gentle);
  }

  @media screen and (max-width:480px){
    #timeline li{
      font-size:2vw;
    }
  }

  #storyTimeline{
    width:100%;
    position:relative;
    bottom:-5vh;
  }

  #timelineBlock{
    position:fixed;
    bottom:7.5vh;
    width:50%;
    z-index:10;
    left: 50%;
    transform: translate(-50%, 0);
  }

  @media screen and (max-width:480px){
    #timelineBlock{
      width:80%;
    }
  }

  .scrollArrow{
    position:relative;
    right:-1.2vw;
    bottom:-5vh;
    width:3%;
  }
</style>