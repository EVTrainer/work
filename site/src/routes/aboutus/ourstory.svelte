<script>
  import Slidegallery from '$lib/components/reusable/slidegallery.svelte'
  import Timeline from '$lib/components/static/timeline.svelte'
  import Vidmenugallery from '$lib/components/reusable/vidmenugallery.svelte'
  import Profile from '$lib/components/reusable/profile.svelte';
</script>

<svelte:head>
  <title>our story</title>
  <meta name="description" content="Follow us on our journey to make CNC technology accessible to everyone!">
</svelte:head>

<!-- makes wrapper for most of the content -->
<div class="main">
  <div class="mainPadding">
    <Vidmenugallery gallerydata='rocketgallery'/>
  </div>

  <br><br><br>

  <section class="mainPadding">
    <Slidegallery gallerydata='rocketgallery' size='80%' position='center' display='whatever' />

    <br>

    <p>
      Before CNCs came rockets. Alex and Zack founded RRPL in 2017 as sophomores with a singular goal: get to space. In their first year, they clawed their way into the Spaceport America Cup, winning a team spirit award. 2 years into RRPL, Alex and Zack were contacted
      by Chianli, looking to collaborate for his own high school rocketry team. Eventually Chianli also joined RRPL. Through the founders' careers at Rutgers, RRPL achieved great heights, becoming one of the largest and most exciting student
      organizations, developing new technologies, launching higher and higher each time, incrementally approaching space. RRPL's next launch in California will hit 30K feet.
    </p>
  </section>

  <br>
  <br>

  <section class="mainPadding">
    <Slidegallery gallerydata='makerspacegallery' size='80%' position='center' display='whatever'/>

    <br>

    <p>
      Even though RRPL was prospering, internally it faced an annoying problem. In order to manufacture rocket components the team needed to frequent the university makerspace. While it was lucky for there to be a machine shop at all, the
      nature of the makerspace created a variety of problems.
    </p>
  </section>

  <br>
  <br>
  <br>

  <section>
    <img id="pano278" src="/img/pano278.jpg" alt="their first garage">

    <br><br><br>

    <div class="mainPadding">
      <p>
        The three met under the name of business for the first time on March 1st of 2021. Bundled in the freezer that was Chianli's garage, somehow they'd produced a rudimentary design of the MVP [minimum viable product] version of Carpenter. On
        April 1st THE CNC COMPANY recieved its Certificate of Formation. By June 8th, Carpenter made its first cut. THE CNC COMPANY had established it was capable of its goal. The team was born.
      </p>
    </div>

    <br>

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

    <div class="mainPadding">
      <p>
        At this point, the roles of each of the founders had relatively settled, job descriptions above. Chianli's lease was ending and Alex was graduating soon with a master's in aerospace engineering. The decision was made to pursue THE CNC
        COMPANY full-time. Come August, thecncco had a new HQ.
      </p>
    </div>
  </section>

  <br>

  <div class="mainPadding">
    <video id="carpVideo" autoplay loop muted>
      <source src="/vid/carpAssembly.mp4" type="video/mp4">
    </video>

    <p class="caption">
      //assembly for the MVP started in March.
    </p>
  </div>

  <section class="mainPadding">
    <div>
      <p>
        <br>
        To sustain themselves in the early months, whenever money ran dry, the founders would go out, build some fences, and put that money back in the company. This was also the era of refining Carpenter. The machine was tested on whatever it
        could handle. The founders observed as it crashed or failed and dissected every issue. Finally they had a product they were confident in.
      </p>
    </div>
  </section>

  <br>
  <br>

  <section class="mainPadding">
    <p>
      Requests started coming in for signs and prototypes to be made on their machine and THE CNC COMPANY happily accepted its first customers. With revenue coming into the company, momentum was built. So where are we now?
    </p>
  </section>

  <br>
  <br>

  <section class="mainPadding">
    <Slidegallery gallerydata='nowgallery' size='80%' position='center' display='whatever'/>

    <br>
    
    <p>
      We're ready to spread our machines to the world. We've made a customer-ready version of Carpenter that's stronger, more precise, and sexier <a href="/carpenter">[take a look!]</a>. We've begun development of Machinist. We've partnered with manufacturers to deliver you the best components at an affordable price. We're trying to get our first customers for our CNCs. Maybe it could be you!
    </p>
  </section>
</div>

<style>
  #pano278{
    width: 100%;
  }

  .row{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    width: 100%;
    margin-left: 5vw;
    padding-right: 5vw;
  }

  .col{
    flex: 1;
    align-self: flex-end;
  }

  @media screen and (max-width:35.5625em){
    .row{
      display:flex;
      flex-direction:column;
      row-gap:20vw;
      margin-left: 0vw;
      padding-right: 0;
    }

    .col{
      align-self:center;
    }
  }

  #carpVideo{
    width: 80%;
    border-radius: var(--r4);
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
</style>