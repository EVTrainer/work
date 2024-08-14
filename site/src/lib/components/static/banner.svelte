<script lang="ts">
    import Darkmode from '$lib/components/static/darkmode.svelte'
    import Mobilenav from '$lib/components/static/mobilenav.svelte'

    import { lightdark } from '/src/stores/lightdark';
    let darkOn:boolean;
    lightdark.subscribe(value => {
        darkOn=value;
    })

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

    // dont remember why this needs to be here but error if not 
    $: innerWidth = 0

    let hover:boolean = false
    const toggle = () => {
        hover = !hover
    }
</script>

<svelte:window bind:innerWidth/>

<div id="banner" class:hideBanner={scrollDir}>
    {#if innerWidth<569}
        <Mobilenav/>
    {/if}

    <a href="/profile">
        {#if darkOn}
            {#if hover}
                <img
                    id="profilePic"
                    src="/img/profile_gentle_fill.png"
                    on:mouseleave={toggle}
                    alt="Profile pic."
                >
            {:else}
                <img
                    id="profilePic"
                    src="/img/profile_gentle.png"
                    on:mouseenter={toggle}
                    alt="Profile pic."
                >
            {/if}
        {:else}
            {#if hover}
                <img
                    id="profilePic"
                    src="/img/profile_offwhite_fill.png"
                    on:mouseleave={toggle}
                    alt="Profile pic."
                >
            {:else}
                <img
                    id="profilePic"
                    src="/img/profile_offwhite.png"
                    on:mouseenter={toggle}
                    alt="Profile pic."
                >
            {/if}
        {/if}
    </a>

    <Darkmode/>

    <a href="/">
        {#if darkOn}
            <img id="logo" src="/img/assets/logos/primaryMark_gentle.png" alt="Primary mark.">
        {:else}
            <img id="logo" src="/img/assets/logos/primaryMark_offwhite.png" alt="Primary mark.">
        {/if}
    </a>
</div>

<style>
    #banner{
        height: var(--bannerHeight);
        width: 100%;
        background-color: var(--grack_dark);
        position: fixed;
        margin-top: -10vh;
        transition: transform 0.2s;
        z-index: 99;
    }

    #profilePic{
        height: calc(var(--bannerHeight) - 3vh);
        margin-top: 1.5vh;
        position: absolute;
        left: 2vw;
    }

    #profilePic:hover{
        cursor: pointer;
    }

    #logo{
        height: 80%;
        display: block;
        margin-left: auto;
        margin-right: auto;
        position: relative;
        top: 50%;
        transform: translateY(-50%);
    }

    @media screen and (max-width:35.5625em){
        #banner{
            background-color:transparent;
        }

        #logo{
            display:none;
        }
    }

    @media screen and (min-width:35.5625em){
        .hideBanner{
            transform: translateY(calc(-1 * var(--bannerHeight)));
        }
    }
</style>