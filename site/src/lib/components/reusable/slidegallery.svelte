<script lang="ts">
    //ex: rocketgallery
    export let gallerydata;
  
    const loadGallery = (name) =>
        fetch(`/slidegalleries/${gallerydata}.json`)
            .then((res) => {
                if (!res.ok) throw new Error('Fetch error');
                return res;
            })
            .then((res) => res.json());
  
    $: imagesPromise = gallerydata && loadGallery(gallerydata);
  
    //ex: 10vw
    export let size
    //left, center, right
    export let position
    //wrap, break
    export let display

    //position and display
    let posdis;
    let imgformat; //shifts dots to location of gallery

    if (position == "left" || position == "right"){
        let displayattribute;
        imgformat = null;

        if (display == "wrap"){ 
            displayattribute = "float"
        }else{
            displayattribute = "text-align"
        }
        posdis = displayattribute + ":" + position;
    }else{
        posdis = "display: block; margin-left: auto; margin-right: auto;"
        imgformat = "display: block; margin-left: auto; margin-right: auto;"
    }

    // shows selected image
    let imageShowingIndex = 0;
    let changeImageIndex = (id) => {
        imageShowingIndex = id;
    }

    let hoverIndex = 0;
    let hoverEnter = (id) => {
        hoverIndex = id;
    }

    let hoverExit = (id) => {
        hoverIndex = null;
    }

    let dotdis;

    if (window.matchMedia('(max-width:35.5625em)').matches){
        dotdis = 12;
    } else if (window.matchMedia('(max-width:64em)').matches){
        dotdis = 4.5;
    } else {
        dotdis = 3;
    }
</script>
  
{#if imagesPromise}
    {#await imagesPromise then images}
        <div class="gallery" style="{posdis};">

            <img id="image" src={images[imageShowingIndex].src} alt={images[imageShowingIndex].alt} style="width: {size}; {imgformat}">
      
            <!-- dots for gallery selection -->
            <div class="dotcontainer" style="width: {images.length*dotdis}vw;"> <!-- each dot takes 3vw of horizonatal space, multiplied by the number of dots there are -->
                <div class="dotrow">
                    {#each images as dot (dot.id)}
                        <div class="dots" on:click={() => changeImageIndex(dot.id)}  on:mouseenter={() => hoverEnter(dot.id)} on:mouseleave={() => hoverExit()}>
                            {#if (dot.id == imageShowingIndex || dot.id == hoverIndex)}
                                <img id="dot" src="/img/gallery/galleryOff.png" alt="gallery selection dot">
                            {:else}
                                <img id="dot" src="/img/gallery/galleryOn.png" alt="gallery selection dot">
                            {/if}
                        </div>
                    {/each}
                </div>
            </div>
        </div>
    {:catch err}
        <pre>{err}</pre>
    {/await}
{/if}
  
<style>
    .gallery{
        position: relative;
    }
  
    #image{
        border-radius: 2vw;
        margin-left: 1.5vw;
        margin-right: 1.5vw;
    }
  
    .dotcontainer{
        height: 1vw;
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-top: -3vw;
        margin-bottom: 2vw;
    }
  
    .dotrow{
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
    }
    
    .dotrow:after{
        content: "";
        display: table;
        clear: both;
    }
  
    .dots{
        float: left;
        display: block;
        width: 3vw;
        height: 3vw;
        padding-top: 1vw;
        border-radius: 1.5vw;
    }
  
    #dot{
        width: 1vw;
        position: absolute;
        margin-left: 1vw;
        border-radius: .5vw;
    }

    @media screen and (max-width:64em){
        .dotrow{
            flex-wrap: nowrap;
        }

        .dots{
            height: 12vw;
            width: 12vw;
            border-radius: 100vw;
            margin-top: -6vw;
            text-align: center;
        }

        #dot{
            width: 1.75vw; 
            position: relative;
            margin: auto;
            top: 50%;
            transform: translateY(-50%);
        }
    }

    @media screen and (max-width:35.5625em){
       #image{
            width: 100%;
       }

       .dotrow{
            flex-wrap: nowrap;
       }
       
       .dots{
            height: 12vw;
            width: 12vw;
        
            border-radius: 100vw;
            margin-top: -10vw;
            text-align: center;
       }

       #dot{
            width: 3.5vw; 
            position: relative;
            margin: auto;
            top: 50%;
            transform: translateY(-50%);
       }
    }
</style>