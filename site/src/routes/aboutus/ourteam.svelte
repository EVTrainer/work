<script lang="ts">
    import Profile from '$lib/components/reusable/profile.svelte'
    import IntersectionObserver from "svelte-intersection-observer";

    let elementOnce: boolean;
    let intersectOnce: boolean;
</script>

<svelte:head>
  <title>our team</title>
  <meta name="description" content= "The people who make THE CNC COMPANY.">
</svelte:head>

<div class="main mainPadding">
  <h5 class="centerText">Founders</h5>

  <p class="centerText">The guys who brought the company from zero to now.</p>

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
    <br>
    <br>

    <IntersectionObserver
        once
        element={elementOnce}
        bind:intersecting={intersectOnce}
    >
        {#if intersectOnce}
            <div id="line" bind:this={elementOnce}></div>
        {:else}
            <div id="line" class="hide" bind:this={elementOnce}></div>
        {/if}
    </IntersectionObserver>

    <br>
    <br>
    <br>

    <h5 class="centerText">Interns</h5>

    <p class="centerText">Our talented engineers developing experience at thecncco.</p>

    <Profile
        profilePic='/img/profiles/kerryLi.png'
        picWidth='20'
        marginLeft='-2'
        name='Kerry Li'
        jobDesc='web dev'
        likes="Osu!"
        dislikes='mushrooms'
        modalLeft='-3.5'
        intro='Hello, I’m Kerry, an intern working on web development for the company. I joined the team near the end of 2021 and have been with the group ever since. I’m a Computer Engineering student at Rutgers going into my third year who’s questioning their career choice.'
        mobileWidth = '80'
        mobilemarginLeft = '-42'
    />
</div>

<style>
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

  #line{
        width: 80%;
        height: 2.5px;
        background-color: var(--grack);
        border-radius: 1.25px;
        display: block;
        margin-left: auto;
        margin-right: auto;
        animation: slideRight 1.25s;
    }

    @media screen and (max-width:35.5625em){
      .row{
        display:flex;
        flex-direction:column;
        row-gap:20vw;
      }

      .col{
        align-self:center;
      }
    }
</style>