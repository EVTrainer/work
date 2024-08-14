<script>
  import Emaillist from '$lib/components/static/emaillist.svelte'

  //updates + displays year for copyright in footer
  const getCurrentYear = () => {
    return new Date().getFullYear();
  }
</script>

<!-- footer -->
<div id="footer">
  <p>
    This site for THE CNC COMPANY is still in development. Check back in a week or 2 and we'll have something better - we promise.
  </p>

  <br>
  <br>

  <a href="https://www.facebook.com/profile.php?id=100074416744974"><img class="socialPictures" src="/img/assets/icons/social/facebook_offwhite.png">&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp</a>
  <a href="https://www.instagram.com/thecncco?fbclid=IwAR0eeq1v4pGUnivdQQVr0MrbxoyaL5Khp69MWluTgGG1ozRxgyDA1GFVff4"><img class="socialPictures" src="/img/assets/icons/social/instagram_offwhite.png">&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp</a>
  <a href="https://twitter.com/thecncco?fbclid=IwAR3KpGOT2t1gxJkXz1R0FdOZtKcNLCean-GgNmxbWdFnjwBMQGGjST5ysUk"><img class="socialPictures" src="/img/assets/icons/social/twitter_offwhite.png"></a>

  <br>
  <br>
  <br>

  <Emaillist/>

  <br>
  <br>

  <div id="linksBox">  
    <a id="links" href="/termsofuse"><p>Terms of Use</p></a>
    <p id="links">&nbsp;/&nbsp;</p>
    <a id="links" href="/privacy"><p>Privacy Policy</p></a>
    <p id="links">&nbsp;/&nbsp;</p>
    <a id="links" href="/presskit"><p>Press Kit</p></a>
    <p id="links">&nbsp;/&nbsp;</p>
    <a id="links" href="/sitemap"><p>Site Map</p></a>
  </div>

  <br>
  <br>
  <br>

  <p>
    Copyright &copy; {getCurrentYear()}, THE CNC COMPANY
  </p>
</div>

<style>
  /* formats look of footer*/
  #footer{
    position: relative;
    bottom: 0;
    text-align: center;
    margin: 0vh 4.5vw 0vh 4.5vw;
    padding: 9vh 10% 9vh 10%;
    background-color:	var(--grack_dark);
    color: var(--offwhite_gentle);
    border-radius: 7.5vw 7.5vw 0vw 0vw;
    z-index: 98;
  }

  /* mobile screen fix black box formatting */
  @media screen and (max-width: 1080px){
    #footer{
      margin: 0;
    }
  }

  /*social media pictures */
  .socialPictures{
    width: 2vw;
    min-width: 1.25em;
  }

  /* links section */
  #linksBox{
    margin-left: auto;
    margin-right: auto;
    width: 50%;
  }

  @media screen and (max-width:64em){
    #linksBox p{
      font-size:1.2vw;
    }
  }

  @media screen and (max-width:35.5625em){
    #linksBox{
      display:flex;
      flex-direction:column;
    }
  }

  #links{
    float: left;
  }

  a{
    text-decoration: none;
    color: var(--offwhite_gentle);
  }

  a:hover{
    opacity: 0.5;
  }
</style>