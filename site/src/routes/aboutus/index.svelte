<script lang="ts">
    import IntersectionObserver from "svelte-intersection-observer";

    let elementOnce: boolean;
    let intersectOnce: boolean;

    let scroll: number;

    let landingHeight: number;
    let containerHeight: number;

    $: scroll1 = scroll-landingHeight;
    $: scroll2 = scroll-landingHeight-containerHeight;
    $: scroll3 = scroll-landingHeight-containerHeight-containerHeight;

    $: mainHeight = landingHeight + containerHeight + containerHeight + containerHeight + containerHeight/1.25;
</script>

<svelte:window bind:scrollY={scroll}/>

<div class="main" style="height: {mainHeight}px; overflow-y: hidden;">
    <div class="makerSlide" bind:clientHeight={landingHeight}>
        <h4 id="makerSlideRight" class="makerSlideText pad3 divwidth">EVERYONE IS A <span class="grackPop">MAKER</span></h4>
        <h4 id="makerSlideLeft" class="makerSlideText pad3 divwidth"><span class="grackPop">MAKING</span> IS FOR EVERYONE</h4>

        <br>
        <br>

        <div class="tworow pad3">
            <div class="twocol">
                <h6 class="pad3">
                    That's want we believe in. Whether you're an engineer, hobbyist, artist, or more, we want to help you create what you imagine.
                </h6>
            </div>

            <div class="twocol">
                <img id="landingPic" src="/img/mission1.jpg" alt="Zack and Alex in the old garage.">
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

    </div>

    <section class="container" bind:clientHeight={containerHeight}>
        <div style:transform={`translate3d(0, ${-scroll1/10}vh, 0)`}>
            <h2 class="centerText">
                🚀
            </h2>        
    
            <h2 class="centerText">
                Our Mission
            </h2>
        </div>

        <div style:transform={`translate3d(0, 0, 0)`} style="position: absolute; bottom: 0vh;">
            <h6 class="mainPadding centerText">
                To make making accessible to everyone, everywhere.
            </h6>
        </div>
    </section>
    
    <section class="container">
        <div style:transform={`translate3d(0, ${-scroll2/10}vh, 0)`}>
            <h2 class="centerText">
                👁️
            </h2>   
    
            <h2 class="centerText">
                Our Vision
            </h2>
        </div>

        <div style:transform={`translate3d(0, 0, 0)`} style="position: absolute; bottom: 0vh;">
            <h6 class="mainPadding centerText">
                To be THE place makers go to for content, community, and tools.
            </h6>
        </div>
    </section>

    <section class="container" style="margin-bottom: 200vh;">
        <div style:transform={`translate3d(0, ${-scroll3/10}vh, 0)`}>
            <h2 class="centerText">
                🙌
            </h2>
    
            <h2 class="bigText c10p centerText">
                Our Values
            </h2>
        </div>

        <div class="mainPadding centerText" style:transform={`translate3d(0, 0, 0)`} style="position: absolute; bottom: -50vh;">
            <h6>
                1. Functional, beautiful design.
            </h6>
    
            <p class="fontsize">
                Weaving together practical features with elegancy for a utilitarian product that happens to look sexy.
            </p>
    
            <h6>
                2. High caliber, low cost.
            </h6>
    
            <p class="fontsize">
                Quality shouldn't be unaffordable. We won't jeapordize our mission by overpricing our product.
            </p>
    
            <h6>
                3. Trust and transparency.
            </h6>
    
            <p class="fontsize">
                You get what you see. Never deceptive pricing, always what you need.
            </p>
    
            <h6>
                4. Community first.
            </h6>
    
            <p class="fontsize">
                We're committed to making our designs open-source and iterating upon feedback from you guys.
            </p>
        </div>
    </section>
</div>

<style>
    #makerSlideRight{
        animation: slideRight 1.25s;
    }

    #makerSlideLeft{
        animation: slideLeft 1.25s;
    }

    .makerSlide{
        width: 100%;
    }

    .makerSlideText{
        font-size: 4vw;
        text-align: center;
    }

    #landingPic{
        width: 87.5%;
        border-radius: 2vw;
        display: block;
        margin-top: auto;
        margin-bottom: auto;
    }

    .tworow{
        animation: fadeIn 2s ease-in-out;
    }

    #line{
        width: 80%;
        height: 2.5px;
        background-color: var(--grack_gentle);
        border-radius: 1.25px;
        display: block;
        margin-left: auto;
        margin-right: auto;
        animation: slideRight 1.25s;
    }

    .container{
        position: relative;
        height: 100vh;
        padding-top: 50vh;
    }

    @media screen and (max-width:35.5625em){
        h6{
            font-size:5vw;
        }
        .centerText{
            font-size:7.5vw;
        }
        .pad3{
            font-size:3vw
        }
        .makerSlideText{
            font-size:10vw;
        }
        .fontsize{
            font-size:3vw;
        }
    }
</style>