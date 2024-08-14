<script>  
  import '../styles/reset.css'
  import '../styles/global.css'
  import '../styles/reusableclasses.css'
  import '../styles/variables.css'
  import '../styles/animations.css'

  import Nav from '$lib/components/static/nav.svelte'
  import Footer from '$lib/components/static/footer.svelte'
  import Banner from '$lib/components/static/banner.svelte'
  import Cookies from '$lib/components/static/cookies.svelte'
  // import Login from '$lib/components/static/auth/login.svelte'
  // import Register from '$lib/components/static/auth/register.svelte'
  import { goto } from '$app/navigation';

  // loading animation
  let isPageLoaded = false;
  const pageLoaded = () => {
    isPageLoaded = true;
  };
  
  // dont remember why this needs to be here but error if not 
  $: innerWidth = 0

  let disappear = () => {

  }

  // Redirection to /profile
  function redirectToProfile() {
    goto('/profile');
  }
</script>

<svelte:window bind:innerWidth/>

{#if isPageLoaded}
  {#if innerWidth>568}
    <Banner/>
    <Nav/>

    <div id="rightWing">
      <!-- <Login on:success={redirectToProfile}/>
      <Register/> -->
      <Cookies/>
    </div>

    <main>
      <slot></slot>
      <Footer/>
    </main>
  {:else}
    <Banner/>
    <Nav/>

    <main>
      <slot></slot>
      <Footer/>
    </main>
  {/if}
{:else}
    <div id="loadingBackground" use:pageLoaded>
      <img id="loading" src="/img/loading.gif" alt="Loading animation.">
    </div>
{/if}

<style>
  #rightWing{
    position: fixed;
    width: 12.5vw;
    right: 1.25vw;
    top: 2.5vh;
    bottom: 10vh;
    margin-top: var(--bannerHeight);
    z-index: 97;
  }

  /* loading animation */
  #loadingBackground{
    width: 100vw;
    height: 100vh;
    background-color: black;
    position: relative;
  }

  #loading{
    max-height: 99vh;
    max-width: 99vw;
    position: absolute;
    top: 50%;
    left: 50%;
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
  }
</style>