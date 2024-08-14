<script>

</script>

<a href="/machinist"> <!-- needs to be changed to whatever link> -->
  <!-- div for banner -->
  <div id="banner">
    <div class="scrollText">
      <!-- <p id ="bannerText">
        &nbsp //PRE-ORDER CARPENTER - 9/10 AVAILABLE &nbsp //PRE-ORDER CARPENTER - 9/10 AVAILABLE &nbsp //PRE-ORDER CARPENTER - 9/10 AVAILABLE &nbsp //PRE-ORDER CARPENTER - 9/10 AVAILABLE &nbsp //PRE-ORDER CARPENTER - 9/10 AVAILABLE &nbsp //PRE-ORDER CARPENTER - 9/10 AVAILABLE &nbsp //PRE-ORDER CARPENTER - 9/10 AVAILABLE &nbsp //PRE-ORDER CARPENTER - 9/10 AVAILABLE &nbsp //PRE-ORDER CARPENTER - 9/10 AVAILABLE &nbsp //PRE-ORDER CARPENTER - 9/10 AVAILABLE &nbsp //PRE-ORDER CARPENTER - 9/10 AVAILABLE &nbsp //PRE-ORDER CARPENTER - 9/10 AVAILABLE &nbsp //PRE-ORDER CARPENTER - 9/10 AVAILABLE &nbsp //PRE-ORDER CARPENTER - 9/10 AVAILABLE
      </p> -->
      <!-- -27.4% -->
      <p id ="bannerText">
        &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW &nbsp //MACHINIST BETA OUT NOW 
      </p>
    </div>
  </div>
</a>

<style>

/* bottom banner/box */
#banner{
   /* margin: auto; */
   bottom: 0px;
   height: 50px;
   width: 200%;
   background-color: var(--grack_dark);
   z-index: 99;
   position:fixed;
}

/* bottom banner text */
#bannerText{
  text-align: middle;
  vertical-align: middle;
  line-height: 50px;
  color: var(--offwhite_gentle);
  z-index: 3;
  position: absolute;
  white-space: nowrap;
}

@media screen and (max-width:1080px){
  #bannerText{margin-top:-5vw;}
}

/* horizontal scroll animation */
.scrollText{
  /* .moz for mozilla, .o for opera, .webkit for chrome/safari and the like,
  below skeleton code */
  -webkit-animation: animate 8s linear infinite;
  -moz-animation: animate 8s linear infinite;
  -o-animation: animate 8s linear infinite;
  animation: animate 8s linear infinite;
  animation-delay: 0s;
  
}

/* each individual keyframe for the separate browsers that state the horizontal
distance that the words travel before resetting */
@-webkit-keyframes animate{
  from
  {
      transform: translateX(0%);
  }
  to
  {
      transform: translateX(-45%);
  }
}

@-o-keyframes animate{
  from
  {
      transform: translateX(0%);
  }
  to
  {
      transform: translateX(-45%);
  }
}

@-moz-keyframes animate{
  from
  {
      transform: translateX(0%);
  }
  to
  {
      transform: translateX(-45%);
  }
}

@keyframes animate{
  from
  {
      transform: translateX(0%);
  }
  to
  {
      transform: translateX(-45%);
  }
}

@media screen and (max-width:64em){
  #banner{
    height:30px;
  }
  #bannerText{
    margin:auto;
    line-height:30px;
  }

  @keyframes animate{
    from{
      transform:translateX(0%);
    }
    to{
      transform:translateX(-61%);
    }
  }
}

@media screen and (max-width:35.5625em){
  #banner{
    height:30px;
  }
  #bannerText{
    margin:auto;
    line-height:35px;
  }

  @keyframes animate{
    from{
      transform: translateX(0%);
    }
    to{
      transform: translateX(-49%);
    }
  }
}
</style>