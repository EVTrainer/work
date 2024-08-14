<script>
  
</script>

<svelte:head>
  <title>carpenter</title>
  <meta name="description" content="The reliable and no-fuss large bed CNC router for woodworking and more!">
</svelte:head>

<!-- fixed tech specs dropdown menu -->
<a href="/img/carpenter/carpenterSpecSheet.pdf" target="_blank">
  <button id="techButton">
    <p>tech specs</p>
  </button>
</a>

<!-- makes wrapper for most of the content -->
<div class="main">
  <div id="landing">
    <img id="landingPic" src="/img/carpenter/carpLight_open.png" alt="Carpenter, our large woodworking CNC router.">
    <h6 id="landingMeet" class="h5">meet <br> carpenter.</h6>
  </div>

  <div id="infoBox">
    <div class="split">
      <div>
        <img id="radarGraph" src="/img/carpenter/radarGraph_light.png" alt="Radar graph for Carpenter's specs.">
      </div>

      <div id="info">
        <h6>precision: 0.002"</h6>
        <h6>min. work area: 2x2'</h6>
        <h6>max. work area: 5x10'</h6>
        <h6>driving force: 112 N</h6>
        <h6>starting 5000</h6>
        <br>
        <div class="button">
          <a href="/preorder"><p>get now</p></a>
        </div>      
      </div>
    </div>

    <div id="line"></div>

    <div id="intro" class="mainPadding">
      <p>inspired by woodworking cncs but adjusted to 5 different form factors, carpenter is a versatile cnc router. we designed her considering affordability first without sacrificing capability. if you're looking for a multi-purpose cnc router without breaking the bank, carpenter is for you.</p>
    </div>
  </div>

  <div id="container" class="mainPadding">
    <h4>all <br> inclusive</h4>
    <br>
    <div class="split">
      <p id="leftBox" class="order1">
        our philosophy is to deliver customers complete products. don't worry about add-ons or important components you need to buy separately - everything you need to get routing comes in one package.
      </p>

      <img id="threepics" class="order2" src="/img/carpenter/carpLight_corner.png" alt="Machinist's driving components.">
    </div>
  </div>

  <div id="container" class="mainPadding">
    <h4 class="rightAlign">robust <br> architecture</h4>

    <div class="split">
      <img id="threepics" class="order1" src="/img/carpenter/carpLight_diagonal.png" alt="Machinist's spindle.">

      <p id="rightBox" class="order2">
        we've battle-tested carpenter in both simulation and real life. we've targeted weak points and reinforced them for a sturdy, reliable, and square frame.      </p>
    </div>
  </div>

  <div id="container" class="mainPadding">
    <h4>dependable <br> performance</h4>

    <div class="split">
      <p id="leftBox" class="order1">
        we've over-engineered carpenter to provide consistent accuracy of 0.002". with HGH rails on all axes, expect a smooth, exact routing experience.
      </p>

      <img id="threepics" class="order2" src="/img/carpenter/carpLight_front.png" alt="Entering the CNC.">
    </div>
  </div>

  <img id="power" src="/img/carpenter/carpLight_spindle.png" alt="Carpenter's spindle from below.">

  <div id="includes" class="centerText">
    <h4>includes</h4>

    <p>
      modular plug-and-play electrical box <br> air-cooled 2.2kW VFD spindle or custom router adapter <br> inductive limit switches and hard stops for safety <br> NEMA 23 closed-loop steppers <br> HGH 20 linear rails with linear roller guideways <br> aerospace grade 6061 aluminum frame <br> rack and pinion drive <br> ethernet-driven controller
    </p>
  </div>

  <h4 class="centerText">made by carpenter</h4>

  <br>

  <p class="centerText mainPadding">
    in its alpha, carpenter was put to use by us and select customers. here's carpenter in action, outfitted with a custom router attachment:
  </p>

  <br>

  <video id="cncSign" controls>
    <source src="/vid/cncSign.mp4" type="video/mp4">
    <track src="captions_en.vtt" kind="captions" srclang="en" label="english_captions">
  </video>

  <br><br><br>

  <div id="faqs" class="centerText mainPadding">
    <h2>FAQs</h2>

    <h6>Can I run the machine off 120v?</h6>
    <p>Yes, using a step-up transformer the machine can run off 120V.</p>

    <br>

    <h6>What new features are you working on?</h6>
    <p>We're working on implementing an automatic tool changer and rotary axis. You'll recieve first access to new upgrades and add-ons!</p>

    <br>

    <h6>What if I'm unsatisfied with my purchase?</h6>
    <p>We offer a money-back guarantee for 1 year if you don't like your machine :&#40;</p>

    <br>

    <h6>How will my machine be delivered?</h6>
    <p>During this beta period, it will be delivered by our engineers who will aid in assembly.</p>

    <br>
    
    <h6>What if my machine is damaged while working?</h6>
    <p>We offer warranty for parts damaged during proper use for 1 year!</p>
  </div>

  <div class="mainPadding centerText">
    <p>unsure if carpenter is right for you? email, text, or hop on the phone with alex at <span class="grackPop">alex@thecncco.com</span> or <span class="grackPop">732-640-3933</span> to learn more and decide what's right for you.</p>
  </div>

  <br><br>

</div>

<style>
  .h5{
    font-size: 3vw;
    font-weight: 100;
    line-height: 1.2;
  }

  @media (max-width: 40em){
    .h5{
      font-size: 4vw;
    }
  }

  /* tech specs button */
  #techButton{
      background-color: var(--grack_gentle);
      color: var(--offwhite_grack);
      cursor: pointer;
      padding-left: 30px;
      padding-right: 30px;
      border: 0;
      border-radius: var(--r5);
      position: fixed;
      text-align: center;
      bottom: 2.5vh;
      z-index: 98;
      left: 50%;
      transform: translate(-50%);
  }

  #techButton:hover{
    opacity: 0.75;
  }

  /* landing styling */
  #landing{
    position: relative;
  }

  #landingPic{
    width: 85%;
    display: block;
    margin-left: auto;
    margin-right: auto;
  }

  #landingMeet{
    position: absolute;
    top: 5%;
    left: 16%;
    color: var(--grack_gentle);
  }

  /* box for carpenter price, info, etc. */
  #infoBox{
    width: 85%;
    background-color: var(--grack_dark);
    display: block;
    margin-left: auto;
    margin-right: auto;
    margin-top: 5vh;
    border-radius: var(--r4);
    padding: 5% 0% 5% 0%;
    color: var(--offwhite_gentle);
  }

  #radarGraph{
    width: 110%;
  }

  @media (max-width: 40em){
    #radarGraph{
      width: 100%;
    }
  }

  #info{
    width: 100%;
    text-align: center;
  }

  #line{
    width: 80%;
    height: 2.5px;
    background-color: var(--offwhite_gentle);
    border-radius: 1.25px;
    display: block;
    margin: 7.5vh auto 7.5vh auto;
  }

  #intro{
    text-align: center;
  }

  /* 3 marketing sections */
  #container{
    margin-top: 20vh;
  }

  #threepics{
    margin-top: 2.5vh;
    margin-bottom: 2.5vh;
  }

  @media (min-width: 40em){
    #threepics{
      width: 40vw;
    }
  }

  #leftBox{
    display: block;
    margin-top: auto;
    margin-bottom: auto;
    margin-right: 5%;
  }

  #rightBox{
    text-align: right;
    display: block;
    margin-top: auto;
    margin-bottom: auto;
    margin-left: 5%;
  }

  @media (max-width: 40em){
    #leftBox{
      text-align: center;
      order: 1;
    }

    #rightBox{
      text-align: center;
      order: 2;
    }
  }

  .rightAlign{
    text-align: right;
  }

  /* carpenter spindle pic */
  #power{
    width: 100%;
    border-bottom: 7.5px solid var(--grack_gentle);
    margin-top: 15vh;
    margin-bottom: 15vh;
  }

  /* includes section */
  #includes{
    margin-bottom: 15vh;
  }

  /* video of Carpenter in action */
  #cncSign{
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 85%;
    border-radius: var(--r4)
  }

  /* FAQ div */
  #faqs{
    margin-bottom: 12.5vh;
  }

  /* button styling */
  .button{
    text-align: center;
    border: 2px solid var(--offwhite_pop);
    border-radius: var(--r5);
    display: inline-block;
    width: 9vw;
  }

  @media screen and (max-width:35.5625em){
    .button{
      width: 27.5vw;
    }
  }

  .button:hover{
      background-color: var(--offwhite_pop);
  }

  .button a{
      text-decoration: none;
  }

  .button a p{
      color: var(--offwhite_pop);
  }

  .button a p:hover{
      color: var(--grack);
  }
</style>