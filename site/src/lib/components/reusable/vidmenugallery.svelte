<script>
    //ex: rocketgallery
    export let gallerydata;

    const loadGallery = (name) =>
        fetch(`/menugalleries/${gallerydata}.json`)
            .then((res) => {
                if (!res.ok) throw new Error('Fetch error');
                return res;
            })
            .then((res) => res.json());

    $: videosPromise = gallerydata && loadGallery(gallerydata);

    // shows selected video
    let videoShowingIndex = 0;
    let changeVideoIndex = (id) => {
        videoShowingIndex = id;
    }

    let hoverIndex = 0;
    let hoverEnter = (id) => {
        hoverIndex = id;
    }

    let hoverExit = (id) => {
        hoverIndex = null;
    }
</script>

{#if videosPromise}
    {#await videosPromise then videos}
        <div class="grid">
            <div class="listGrid" style="width: {videos.length*3}vw;"> 
                <div class="itemList">
                    {#each videos as item (item.id)}
                        <div class="items" on:click={() => changeVideoIndex(item.id)}  on:mouseenter={() => hoverEnter(item.id)} on:mouseleave={() => hoverExit()}>
                            {#if (item.id == videoShowingIndex)}
                            <p class="item">&gt;</p><p class="item"> &nbsp; {videos[videoShowingIndex].title} </p>
                            {:else}
                            <p class="item">&nbsp;</p><p class="item"> &nbsp; {videos[item.id].title}</p>
                            {/if}
                        </div>
                    {/each}
                </div>
            </div>
            <div id="videoGrid"><video id="video" src={videos[videoShowingIndex].src} alt={videos[videoShowingIndex].alt} autoplay controls muted>
            </div>
            <div id="stats" class="grackPop">
                <p class="par">{videos[videoShowingIndex].stats}</p>
            </div>
            <div id="caption">
                <p class="par"> {videos[videoShowingIndex].caption}</p>
            </div>
        </div>
    {:catch err}
        <pre>{err}</pre>
    {/await}
{/if}
<style>
    .grid{
        display: grid;
        margin-right:6vw;
    }

    #video{
        border-radius: 2vw;
        margin-left:6.5vw;
        width:100%;
    }

    #videoGrid{
        grid-column-start: 2;
        grid-column-end: 4;
    }
    .listGrid{
        display: flex;
        grid-column-start: 1;
        grid-column-end: 2;
        grid-row-start: 1;
        grid-row-end: 2;
        align-items: center;
    }

    #stats{
        grid-column-start: 2;
        grid-column-end: 4;
        text-align:center;
        margin-left:12.5vw;
        font-weight:bold;
    }

    #caption{
        text-align:left;
        width:95%;
        margin-left:7.5vw;
        grid-column-start: 2;
        grid-column-end: 4;
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

    .item:hover{
        font-weight:bold;
    }

    @media screen and (max-width:35.5625em){
        #videoGrid{
            grid-row-start:1;
            grid-row-end:2;
            grid-column-start:1;
            grid-column-end:3;
        }
        .listGrid{
            grid-row-start:2;
            grid-row-end:3;
            grid-column-start:1;
            grid-column-end:2;
        }
        #stats{
            grid-row-start:2;
            grid-row-end:3;
            grid-column-start:2;
            grid-column-end:3;
        }
        #caption{
            grid-row-start:3;
            grid-row-end:4;
            grid-column-start:1;
            grid-column-end:3;
            margin:auto;
        }
        #video{
            margin:auto;
        }
    }
</style>