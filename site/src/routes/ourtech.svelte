<script lang="ts">
  import Marquee from '$lib/components/static/marquee.svelte'
  import Typewriter from '$lib/components/reusable/typewriter.svelte'
  import Button from '$lib/components/reusable/button.svelte'

  import { lightdark } from '/src/stores/lightdark';
    let darkOn:boolean;
    lightdark.subscribe(value => {
        darkOn=value;
  })
</script>
  
  <svelte:head>
      <title>our tech</title>
      <meta name="description" content="Check out the innovative products we make using CNC technology!">
  </svelte:head>
  
  <Marquee/>
  
  <div class="main mainPadding">
      <!-- div to make typewriter effect full page -->
      <div id="landing">
        <!-- text of typewriter effect -->
        <h1 id="typetext">
          <Typewriter words='["computer numerical control", "for makers", "for creators", "for you"]'/>
        </h1>
  
        <ul id="jumpTo">
          <li><p>jump to:</p></li>
          <div id="machineButtons">
            <Button text='carpenter' link='/carpenter'/>
            <br>
            <br>
            <Button text='machinist' link='/machinist'/>
          </div>
        </ul>
      </div>
  
      <br>
  
      <div class="content">
        <h6>
          CNC [noun]
        </h6>
  
        <p class="figcaption">
          //see-en-see
        </p>
      </div>
  
      <div class="subContent">
        <p>
          : Abbreviation for "Computer Numerical Control". Automated control of machines by computer program. Colloquially refers to machines that use CNC technology primarily for manufacturing purposes such as milling, routing, cutting, printing, etc.
        </p>
      </div>
  
      <br>
      <br>
  
      <div>
        <img id="carpDev" src="img/carpDev.jpg" alt="Zack + Alex working on Carpenter">
        <p class="centerText">//Zack + Alex developing Carpenter in the first few months of our company</p>
      </div>
  
      <br><br><br><br><br><br>

  
      <section>
        <h4 class="centerText">how it works</h4>
  
        <p class="centerText">
          Computer numerical control [CNC] is at the core of all our machines. Using CNC tech, our instruments achieve both precision and automation.
        </p>

        <br><br><br>
  
        <div class="row">
          <div class="cncCol">
            <img class="howItWorks" src="img/hardware.jpg" alt="hardware">
            <h6 class="centerText">Hardware</h6>
  
            <div class="longText">
              <p>
                The physical components that move or support our machine. Ball screw, gantry, spindle, etc.
              </p>
            </div>
          </div>
  
          <!-- Chianli's profile -->
          <div class="cncCol">
            <img class="howItWorks" src="img/electrical.jpg" alt="electrical">
            <h6 class="centerText">Electrical</h6>
  
            <div class="longText">
              <p>
                The intermediary allowing the computer to communicate with and move our hardware.
              </p>
            </div>
          </div>
  
          <!-- Zack's profile -->
          <div class="cncCol">
            <img class="howItWorks" src="img/software.PNG" alt="software">
            <h6 class="centerText">Software</h6>
  
            <div class="longText">
              <p>
                The control tower of CNCs. Signals are generated and communicated through G-code, telling the machine how to move.
              </p>
            </div>
          </div>
        </div>
      </section>
  
      <br><br><br>
  
      <section>
        <h4>for makers, <br> by makers</h4>
  
        <br>
  
        <div class="subContent">
          <p>
            Our technology is developed with makers in mind. See below to discover our machines:
          </p>
        </div>
  
        <br>
        <br>
  
        <div class="row1col2">
          <div class="column">
            <a href="carpenter">
              <img class="machineGallery" src="img/carpenter/carpLight_open.png" alt="Carpenter, our large-bed woorkworking CNC.">
              <h6>carpenter</h6>
            </a>
  
            <div class="longText">
              <p>
                Our first CNC, armed with a 4x6 ft. bed, 0.002" accuracy, and a 3 horsepower spindle. Battle-tested through simulation and real life, Carpenter is exactly what you want in a large-bed machine.
              </p>
            </div>
          </div>
  
          <div class="column">
            <a href="machinist">
              {#if darkOn}
                <img class="machineGallery" src="img/machinist/lightFront_grack.png" alt="Machinist, our desktop precision CNC mill.">
              {:else}
                <img class="machineGallery" src="img/machinist/darkFront_offwhite.png" alt="Machinist, our desktop precision CNC mill.">
              {/if}
              <h6>machinist</h6>
            </a>
  
            <div class="longText">
              <p>
                Still in development, Machinist is for metal-cutting with absolute precision. It's desktop sized and machines up to steel. In fact, we use Machinist for manufacturing our own machines. Beta testing now.
              </p>
            </div>
          </div>
        </div>
    </section>
  
    <br><br><br><br><br><br>
  
    <section>
      <h4 class="rightAlign">made by cnc</h4>
  
      <div class="subContent">
        <p>
          We also provide machining services to manufacture your projects. Whether you have a design or want us to make something - whether you want a mechanical component, sign, sculpture, or anything else CNC-made, we can create it for you. Email, text, or hop on the phone with Chianli at chianli@thecncco.com or 732-762-2854 to get a quote and your project delivered fast.
        </p>
      </div>
  
      <br><br><br>
  
      <div class="vid">
        <video id="harley" controls>
          <source src="/vid/harley.mp4" type="video/mp4">
          <track src="captions_en.vtt" kind="captions" srclang="en" label="english_captions">
        </video>
      </div>
  
      <div class="caption">
        <p>//our first commissioned sign for our customer's dog, Harley.</p>
      </div>
    </section>
  
    <br>
    <br>
  
  </div>
  
<style>
  /* makes typewriter animation full screen */
  #landing{
    position: relative;
    height: 81vh;
  }

  @media screen and (max-width:35.5625em){
    #landing{
      height: 50vh;
    }
  }
  
  /* formats "jump to" section */
  #jumpTo{
    position: absolute;
    bottom: 5vh;
    right: 7.5vw;
  }
  
  #jumpTo li{
    list-style: none;
    text-align: left;
  }

  /* pic of Zack and Alex working on Carpenter */
  #carpDev{
    width: 90%;
    border-radius: var(--r3);
    display: block;
    margin-left: auto;
    margin-right: auto;
  }

  /* makes 3 columns for "how it works" */
  .cncCol{
    float: left;
    width: 33.33%;
    display: block;
  }
  
  /* clear floats after the columns */
  .row:after{
    content: "";
    display: table;
    clear: both;
  }
  
  .howItWorks{
    width: 15vw;
    display: block;
    margin-left: auto;
    margin-right: auto;
    border-radius: var(--r5);
  }
  
  /* makes font smaller for hardware, electrical, software section so it looks better */
  .longText{
    font-size: 0.75em;
    padding: 0% 7% 0% 7%;
  }
  
  /* formats machine gallery */
  .row1col2{
    display: flex;
    text-align: center;
  }
  
  .column{
    flex: 50%;
  }
  
  .column a{
    text-decoration: none;
    color: var(--grack_gentle);
  }
  
  .column a :hover{
    opacity: 0.5;
  }
  
  .machineGallery{
    height: 15vw;
  }
  
  #harley{
    width: 85%;
    border-radius: var(--r4);
    margin-left: 5vw;
  }

  @media screen and (max-width:35.5625em){
    #harley{
      width:100%;
      margin:auto;
    }

    .cncCol{
      width: 100%;
    }

    .howItWorks{
      width:75%;
    }

    .longText{
      margin-bottom:10vw;
    }
    
    .row1col2{
      display:flex;
      flex-direction:column;
      row-gap:10vw;
    }
    .machineGallery{
      width:75%;
      height:auto;
    }
    .subContent{
      margin-left:3vw;
    }
  }
</style>