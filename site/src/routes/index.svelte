<script lang="ts">
  import Marquee from '$lib/components/static/marquee.svelte'
  import Contactform from '$lib/components/static/contactform.svelte'
  import Imgmenugallery from '$lib/components/reusable/imgmenugallery.svelte'
  import Typewriter from '$lib/components/reusable/typewriter.svelte'
  import Button from '$lib/components/reusable/button.svelte'
  import Profile from '$lib/components/reusable/profile.svelte'
  import Modal from '$lib/components/reusable/modal.svelte'

  import { lightdark } from '/src/stores/lightdark';
  let darkOn:boolean;
  lightdark.subscribe(value => {
      darkOn=value;
  })

  let submitStatus;
  const submitForm = async (data) => {
    submitStatus = "submitting";
    const formData = new FormData(data.currentTarget);
    const res = await fetch("contact.json", {
      method: "POST",
      body: formData,
    });
    const { message } = await res.json();
    submitStatus = message;
  };
</script>

<svelte:head>
  <title>THE CNC COMPANY</title>
  <meta name="description" content= "THE CNC COMPANY is an exciting CNC tech startup lowering the barrier of entry for hardware.">
</svelte:head>

<Marquee/>
<Modal/>

<!-- makes wrapper for most of the content -->
<div class="main mainPadding">
  <!-- title and top of page -->
  <div id="landing">
    <div id="typetext">
      <Typewriter words='["Welcome, Maker."]'/>
    </div>

    <div id="machineButtons">
      <Button text='carpenter' link='/carpenter'/>
      <br>
      <br>
      <Button text='machinist' link='/machinist'/>
    </div>
  </div>

  <!-- THE CNC COMPANY synopsis -->
  <div class="content">
    <p>
      CNC tech should be for everyone. Check out our machines right up there! &#9757
    </p>
  </div>

  <br>

<!-- Machinist front render -->
<div class="mediaBoxFull">
  {#if darkOn}
    <img src="img/machinist/lightFront_grack.png" alt="Machinist, a metal-cutting CNC mill">
  {:else}
    <img src="img/machinist/darkFront_offwhite.png" alt="Machinist, a metal-cutting CNC mill">
  {/if}
</div>

  <div class="caption">
    <p>//we couldn't find a capable machine for makers - </p>
    <p>so we made one ourselves.</p>
  </div>

  <br>
  <br>
  <br>

  <!-- "our story" content starting. To add a lil' personal touch! -->
  <section>
    <p>
      THE CNC COMPANY is an ad-hoc business spawned from 3 Rutgers rocket scientists, Alex, Chianli, and Zack. But our machines are for far more than rocketry.
    </p>

    <!-- splits into 3 columns for founder profiles -->
    <div class="row">
      <div class="col">
        <Profile
          profilePic='/img/profiles/alexanderSanducu.png'
          picWidth='35'
          marginLeft='-15'
          marginBottom='-3'
          name='Alexander Sanducu'
          jobDesc='tech'
          likes='Miatas'
          dislikes='Rockets gone AWOL'
          modalLeft='-10'
          intro="Buna Ziua, my name is Alexander, and I graduated from Rutgers with a Masters of Engineering in Aerospace. My job in the company is to design and manufacture our CNC machines. In college I built rockets using CNCs, now I build CNCs to one day build rockets again. CNCs aren't so different from rocket science right?"
          mobileWidth = '140'
          mobilemarginLeft = '-150'
          mobilemarginBottom = '-10'
          />
      </div>

      <div class="col">
        <Profile
          profilePic='/img/profiles/chianliHang.png'
          picWidth='17.5'
          marginLeft='0'
          name='Chianli Hang'
          jobDesc='web dev, biz dev, design'
          likes='Mischief'
          dislikes='Salads'
          modalLeft='-3.5'
          intro="Yowza! I'm Chianli, pronounced 'chen-lee'. My main job is to build this website and make our company look good. I dropped out of university as a freshman to pursue this company full-time. Dear god... WHAT HAVE I DONE???"
          mobileWidth = '70'
          mobilemarginLeft = '-60'
          mobilemarginBottom = '3'
          />
      </div>

      <div class="col">
        <Profile
          profilePic='/img/profiles/zachariahClark.png'
          picWidth='15'
          marginLeft='1'
          name='Zachariah Clark'
          jobDesc='tech'
          likes="Wendy's 4 for 4"
          dislikes='Nice weather'
          modalLeft='-3.5'
          intro="Hello, I’m Zachariah, a chemical engineer from Rutgers. My job is to design machines that fill gaps in the market of current amateur CNCs. Now, it may sound far from chemical engineering but material properties goes back to chemistry and comes up a lot... right? Truth is I enjoy all types of engineering and building these machines is what excites and motivates me."
          mobileWidth = '60'
          mobilemarginLeft = '-44'
          mobilemarginBottom = '3'
          />
      </div>
    </div>

    <br>

    <p>Our technology is for independent inventors, contractors, artists, and more. We want to lower the barrier of entry for hardware so anyone can create.</p>
  </section>

  <br>
  <br>
  <br>

  <h1 id="endless">Endless Possibilities</h1>

  <section>
    <Imgmenugallery gallerydata='endlesspossibilities'/>
  </section>

  <br>

  <!-- "chat with us" content starting. This is where customers can start a conversation with us, investors can contact us, and so forth. -->
  <section id="talkToUs">
    <h1 id="talk">Talk To Us</h1>

    <br>
    <br>

    <div class="subContent">
      <p>
        Hey, you! Wanna chat with us? You can call/text 732-762-2854 or email chianli@thecncco.com.  Or just fill out the form below! Thanks :D
      </p>

      <br>

      <Contactform/>
    </div>
  </section>
</div>

<style>
  /* centers title of page */
  #landing{
    position: relative;
    height: 25vw;
  }

  #machineButtons{
    position: absolute;
    bottom: 12.5vh;
    right: 5vw;
  }

  @media screen and (max-width:35.5625em){
    #landing{
      height: 40vh;
    }

    #machineButtons{
      display: flex;
      width: 100%;
      justify-content: space-evenly;
      right: 0;
      padding-left: 5vw;
      padding-right: 5vw;
    }
  }

  /* formats look of picture of Carpenter as well as caption*/
  .mediaBoxFull{
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 85%;
  }

  .mediaBoxFull img{
    width: 100%;
    border-radius: 3em;
  }

  .row{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    width: 100%;
  }

  .col{
    flex: 1;
    align-self: flex-end;
  }

  #endless{
    font-family: c10p;
    font-size: 5vw;
    font-weight: 100;
    padding-right: 3vw;
    text-align: right;
    line-height: normal;
    animation: fadeIn 0.5s;
  }

  @media screen and (max-width:35.5625em){
    #endless{
      font-size:10vw;
    }
    .row{
      display:flex;
      flex-direction:column;
      row-gap:25vw;
  
    }
    .col{
      align-self:center;
    }
  }

  #talk{
    font-family: c10p;
    font-size: 5vw;
    font-weight: 100;
    padding-right: 3vw;
    text-align: left;
    line-height: normal;
    animation: fadeIn 0.5s;
  }

  @media screen and (max-width:35.5625em){
    #talk{
      font-size:10vw;
    }
  }
</style>