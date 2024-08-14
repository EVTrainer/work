<script>
    export let gallerydata;

    const loadGallery = (name) =>
        fetch(`/menugalleries/${gallerydata}.json`)
            .then((res) => {
                if (!res.ok) throw new Error('Fetch error');
                return res;
            })
            .then((res) => res.json());

    $: imagesPromise = gallerydata && loadGallery(gallerydata);

    //ex: 10vw

    //position and display

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
</script>

{#if imagesPromise}
    {#await imagesPromise then images}
        <div class="grid">
            <div class="listGrid"> 
                <div class="itemList">
                    {#each images as item (item.id)}
                        <div class="items" on:click={() => changeImageIndex(item.id)}  on:mouseenter={() => hoverEnter(item.id)} on:mouseleave={() => hoverExit()}>
                            {#if (item.id == imageShowingIndex)}
                                <p class="item">&gt;</p><p class="item"> &nbsp; {images[imageShowingIndex].title} </p>
                            {:else}
                                <p class="item">&nbsp;</p><p class="item"> &nbsp; {images[item.id].title}</p>
                            {/if}

                        </div>
                    {/each}
                </div>
            </div>
            <div id="imageGrid"><img id="image" src={images[imageShowingIndex].src} alt={images[imageShowingIndex].alt}>
            </div>
        </div>
    {:catch err}
        <pre>{err}</pre>
    {/await}
{/if} 

<style>
    .grid{
        display:grid;
        grid-auto-columns: minmax(20vw, auto);
        align-items:center;
        grid-template-rows: 75vh;

    }

    @media screen and (max-width:35.5625em){
        .grid{
            grid-template-rows:50vh;
        }
    }

    .listGrid{
        grid-column-start:1;
        grid-column-end:2;
        grid-row-start:1;
        grid-row-end:2;

    }

    #imageGrid{
        grid-column-start:2;
        grid-column-end:4;
        grid-row-start:1;
        grid-row-end:2;
    }

    #image{
        border-radius: 2vw;
        width:100%;

    }

    .itemList{
        display: flex;
        flex-direction:column;
    }

    .itemList:after{
        content: "";
        display: table;
        clear: both;
    }

    .items{
        display: block;
        width: 3vw;
        padding-bottom: 2vw;
        border-radius: 1.5vw;
    }

    .item{
        width:1vw;
        border-radius: .5vw;
        white-space:nowrap;
        display:inline-block;
        cursor:pointer;
    }

    @media screen and (max-width:35.5625em){
        .item{
            position:relative;
            z-index:5;
        }
    }

    .item:hover{
        font-weight:bold;
    }
</style>