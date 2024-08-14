<script lang="ts">
  import Button from '$lib/components/reusable/button.svelte';

  import { lightdark } from '/src/stores/lightdark';
  let darkOn:boolean;
  lightdark.subscribe(value => {
      darkOn=value;
  })
</script>

<svelte:head>
    <title>machinist</title>
    <meta name="description" content="Cutting edge (haha) and affordable, Machinist is the next generation of desktop CNC mills for precision machining metal.">
</svelte:head>

<!-- makes wrapper for most of the content -->
<div class="main">

  <a href="/img/machinist/specsheet.pdf" target="_blank">
    <button id="techButton">
      <p>tech specs</p>
    </button>
  </a>

  <header class="split">
    <div id="landingText">
      <h4>hey!</h4>
      <p id="h5">check it out. we made a compact CNC mill and named her "machinist".</p>
      <br>
      <p>7000 through program beta. <br> invitation only.</p>
      <br>
      <Button text="get it" link="/beta" />
    </div>
  
    <!-- SolidWorks rendering of Carpenter -->
    <div>
      {#if darkOn}
        <img id="landingImg" src="/img/machinist/lightFront_grack.png" alt="Machinist, our metal-cutting CNC mill">
      {:else}
        <img id="landingImg" src="/img/machinist/darkFront_offwhite.png" alt="Machinist, our metal-cutting CNC mill">
      {/if}
    </div>
  </header>

  <h6 class="centerText">introducing machinist</h6>

  <p id="intro" class="centerText mainPadding">
    we've been waiting for this. finally a quality CNC mill designed for power, designed for simplicity, designed for you. born from the concept of the machine that can replicate itself, we use machinist to manufacture all our cncs. 
  </p>

  <section id="container" class="mainPadding">
    <h4>pinpoint <br> accuracy</h4>
    <br>
    <div class="split">
      <p id="leftBox" class="order1">
        at a theoretical 3.125 x 10<sup>-5</sup> inch precision, the limiting factor is no longer the machine, but the person. we use machinist to make all our machines and even itself, a testament to its reliability.
      </p>

      <img id="threepics" class="order2" src="/img/machinist/precision.png" alt="Machinist's driving components.">
    </div>
  </section>

  <section id="container" class="mainPadding">
    <h4 class="rightAlign">power</h4>

    <div class="split">
      <img id="threepics" class="order1" src="/img/machinist/power.png" alt="Machinist's spindle.">

      <p id="rightBox" class="order2">
        equipped with a 2.2kW VFD spindle to churn through the toughest metals, machinist is as tough as the best of them. her rigid chassis is designed to reduce vibrations while a driving force of 1.2kN propels that spindle across the work area.
      </p>
    </div>
  </section>

  <section id="container" class="mainPadding">
    <h4>innovative <br> design</h4>

    <div class="split">
      <p id="leftBox" class="order1">
        machinist's novel form factor allows access and visibility from all 360 degrees. she's fully modular and clear wherever possible. with her integrated enclosure, this machine is the most compact enclosed mill on the market.
      </p>

      <img id="threepics" class="order2" src="/img/machinist/lightOpen_grack_4x3.png" alt="Entering the CNC.">
    </div>
  </section>

  <div id="line"></div>

  <section class="mainPadding">
    <div class="split">
      {#if darkOn}
        <img id="radarGraph" src="/img/machinist/radarGraph_light.png" alt="Machinist stats and specs radar graph.">
      {:else}
        <img id="radarGraph" src="/img/machinist/radarGraph_dark.png" alt="Machinist stats and specs radar graph.">
      {/if}
      <div id="quickSpecs">
        <h6>quick specs</h6>
        <p>
          theoretical max precision: 3.125 x 10 <sup>-5</sup> in
          <br>
          maximum backlash : 0.001 in
          <br>
          work area: 15” x 30” x 7”
          <br>
          footprint: 32” x 48” x55”
          <br>
          XY driving force: 1.2kN
          <br>
          Z downwards force: 2.4kN
          <br>
          XY lead speed: 120 in/min
          <br>
          Z lead speed: 60 in/min
        </p>
      </div>
    </div>

    <div id="includes">
      <h6>includes</h6>
      <p>
        modular plug-and-play electrical box + air-cooled 2.2kW VFD spindle + integrated full enclosure + flood coolant with recycling system and chip tray + inductive limit switches and hard stops for safety + NEMA 23 closed-loop steppers + HGH 20 linear rails with linear roller guideways + 1610 linear ballscrews all axes + aerospace grade 6061 aluminum frame + ethernet-driven controller
      </p>
    </div>
  </section>

  <div id="line"></div>

  <!-- FAQs -->
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

  <section class="mainPadding">
    <h4>development <br> ongoing</h4>

    <br>

    <p>
      as of now, machinist has launched for beta testing, but you'll have to wait a lil' before we launch it to the wider world. every day we're coming up with new ideas and it's a super exciting process. if you're impatient we invite you to enquire about program beta - but for now, enjoy this nice picture of zack sipping some coffee during early development.
    </p>

    <br><br><br>

    <img id="machDesignProcess" src="img/machDesignProcess.jpg" alt="Zack working on Machinist">
  </section>

  <br><br><br>

  <div class="consult mainPadding centerText">
    <p>
      contact chianli at <span class="grackPop">chianli@thecncco.com</span> or <span class="grackPop">732-762-2854</span> to enquire about program beta.
    </p>
  </div>
</div>  

<style>
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

  #landingImg{
    width: 90%;
    display: block;
    margin-left: auto;
    margin-right: auto;
  }

  #landingText{
    text-align: center;
    margin-left: 10%;
    margin-right: 10%;
  }

  @media (min-width: 40em){
    #landingImg{
      width: 40vw;
      order: 2;
      margin-left: 5vw;
    }

    #landingText{
      text-align: left;
      order: 1;
      margin: 10vh 5vw 0 0;
    }
  }

  #h5{
    font-size: 1.75vw;
    font-weight: 100;
    line-height: 1.2;
  }

  @media (max-width: 40em){
    #h5{
      font-size: 4.25vw;
    }
  }

  #intro{
    margin-left: 7.5vw;
    margin-right: 7.5vw;
  }

  /* 3 marketing sections */
  #container{
    margin-top: 20vh;
  }

  #threepics{
    border-radius: var(--r5);
    border: 1px solid var(--grack_gentle);
    background-color: var(--grack);
    margin-top: 2.5vh;
    margin-bottom: 2.5vh;
  }

  @media (min-width: 40em){
    #threepics{
      width: 35vw;
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

  #quickSpecs{
    text-align: center;
  }

  #includes{
    margin-top: 7.5vh;
    text-align: center;
  }

  @media (min-width: 40em){
    #radarGraph{
      width: 30vw;
      flex: auto;
      margin-right: 5vw;
    }

    #quickSpecs{
      flex: auto;
      display: block;
      margin-top: auto;
      margin-bottom: auto;
      text-align: left;
    }

    #includes{
      text-align: left;
    }
  }

  #line{
    width: 80%;
    height: 2.5px;
    background-color: var(--grack_gentle);
    border-radius: 1.25px;
    display: block;
    margin: 12.5vh auto 12.5vh auto;
  }

  /* FAQ div */
  #faqs{
    margin-bottom: 12.5vh;
  }

  /* image of Zack working on Machinist */
  #machDesignProcess{
    width: 85%;
    border-radius: var(--r4);
    display: block;
    margin-left: auto;
    margin-right: auto;
  }

  .consult{
    margin-bottom: 5vh;
  }
</style>