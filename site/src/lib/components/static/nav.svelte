<script lang="ts">
  import {page} from "$app/stores";
  
  let hover1 = false
  let togglehover1 = () => {
    hover1 = !hover1;
  }

  let hover2 = false
  let togglehover2 = () => {
    hover2 = !hover2;
  }

  // scrolls nav up with banner gone
  let lastScrollY = window.scrollY;
  let scrollDir:boolean;
  window.addEventListener("scroll", () => {   
      if (lastScrollY < window.scrollY) {
          scrollDir = true
      } else {
          scrollDir = false
      }
      lastScrollY = window.scrollY;
  });
</script>

<!-- menu -->
<nav class="nav" class:hideNav={scrollDir}>
  <ul class="navLi">
    <!-- home -->
    <li>
        <a href="/">
        <p class:inactive={$page.url.pathname !== "/"}>&gt;</p>
        <p class:inactive={$page.url.pathname == "/"}>&nbsp;</p>
        <p>&nbsp;home</p>
      </a>
    </li>

    <br>

    <!-- our tech -->
    <li
      on:mouseenter={togglehover1} on:mouseleave={togglehover1}>
      <a href="/ourtech">
        <p class:inactive={$page.url.pathname !== "/ourtech"}>&gt;</p>
        <p class:inactive={$page.url.pathname == "/ourtech"}>&nbsp;</p>
        <p>&nbsp;our tech
          {#if (hover1 == true || $page.url.pathname == "/carpenter" || $page.url.pathname == "/machinist")}
            <sup>-</sup>
          {:else}
            <sup>+</sup>
          {/if}
        </p>
      </a>
      <!-- our tech submenu -->
      {#if (hover1 == true || $page.url.pathname == "/carpenter" || $page.url.pathname == "/machinist")}
        <ul class="subMenu" style="display: block;">
          <li><a href="/carpenter"><p class:inactive={$page.url.pathname !== "/carpenter"}>&gt;</p> <p class:inactive={$page.url.pathname == "/carpenter"}>&nbsp;</p> <p>&nbsp;carpenter</p></a></li>
          <li><a href="/machinist"><p class:inactive={$page.url.pathname !== "/machinist"}>&gt;</p> <p class:inactive={$page.url.pathname == "/machinist"}>&nbsp;</p> <p>&nbsp;machinist</p></a></li>
        </ul>
      {/if}
    </li>

    <br>

    <!-- about us -->
    <li on:mouseenter={togglehover2} on:mouseleave={togglehover2}>
      <a href="/aboutus">
        <p class:inactive={$page.url.pathname !== "/aboutus"}>&gt;</p>
        <p class:inactive={$page.url.pathname == "/aboutus"}>&nbsp;</p>
        <p>&nbsp;about us
          {#if (hover2 == true || $page.url.pathname.startsWith("/aboutus/blog") || $page.url.pathname == "/aboutus/ourstory" || $page.url.pathname == ("/aboutus/ourteam"))}
            <sup>-</sup>
          {:else}
            <sup>+</sup>
          {/if}
        </p>
      </a>
      <!-- about us submenu -->
      {#if (hover2 == true || $page.url.pathname.startsWith("/aboutus/blog") || $page.url.pathname == "/aboutus/ourstory" || $page.url.pathname == "/aboutus/ourteam")}
        <ul class="subMenu" style="display: block;">
          <li><a href="/aboutus/blog"><p class:inactive={!$page.url.pathname.startsWith("/aboutus/blog")}>&gt;</p> <p class:inactive={$page.url.pathname.startsWith("/aboutus/blog")}>&nbsp;</p> <p>&nbsp;our blog</p></a></li>
          <li><a href="/aboutus/ourstory"><p class:inactive={$page.url.pathname !== "/aboutus/ourstory"}>&gt;</p> <p class:inactive={$page.url.pathname == "/aboutus/ourstory"}>&nbsp;</p> <p>&nbsp;our story</p></a></li>
          <li><a href="/aboutus/ourteam"><p class:inactive={$page.url.pathname !== "/aboutus/ourteam"}>&gt;</p> <p class:inactive={$page.url.pathname == "/aboutus/ourteam"}>&nbsp;</p> <p>&nbsp;our team</p></a></li>
        </ul>
      {/if}
    </li>

    <br>

    <!-- talk to us -->
    <li><a href="/#talkToUs"><p class:inactive={$page.url.pathname !== "/#talkToUs"}>&gt;</p> <p class:inactive={$page.url.pathname == "/#talktous"}>&nbsp;</p> <p>&nbsp;talk to us</p></a></li>
  </ul>
</nav>
  
<style>
  /* removes the nav display for mobile */
  @media screen and (max-width: 35.5625em){
    .nav{
      display: none;
    }
  }

  .nav{
    animation: slideRight 0.5s;
  }

  /* styles naviagtion bar */
  .nav{
    position: fixed;
    background-color:	var(--offwhite_grack);
    color: var(--grack_gentle);
    top: 2.5vh;
    left: 1.5vw;
    width: 12vw;
    padding: 3% 1% 3% 1%;
    border-radius: 2.5vw;
    z-index: 97;
    margin-top: var(--bannerHeight);
    transition: transform 0.3s;
  }

  .hideNav{
    transform: translateY(calc(-1 * var(--bannerHeight)));
  }

  .navLi{

  }

  .navLi li{
    list-style: none;
    text-align: left;
  }

  .navLi li a{
    text-decoration: none;
    color: var(--grack_gentle);
  }

  .navLi li a:hover{
    text-decoration: none;
    font-weight: bold;
  }

  .subMenu{
    margin-left: 1vw;
    animation: slideDown .5s;
    animation-delay: -.2s;
  }

  p{
    display: inline;
  }

  .inactive{
    display: none;
  }

  @media screen and (max-width:64em){
    p{
      font-size:1.15vw;
    }
    .navLi li{
      margin-top:-.5vw;
      margin-bottom:-.5vw;
    }
  }
</style>