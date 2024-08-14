<script lang="ts">
    export let profilePic: string;
    export let picWidth: string;
    export let marginLeft: string = '0';
    export let marginBottom: string = '0';
    export let name: string;
    export let jobDesc: string;
    export let likes: string;
    export let dislikes: string;
    export let modalLeft: string = '0';
    export let modalBottom: string = '0';
    export let intro: string;
    // mobile props
    export let mobileWidth: string;
    export let mobilemarginLeft: string;
    export let mobilemarginBottom: string;


    let modalOpen = false;
    const toggle = () => {
        modalOpen = !modalOpen;
    }

    if (window.matchMedia('(max-width:35.5625em)').matches){
        picWidth = mobileWidth;
        marginLeft = mobilemarginLeft;
        marginBottom = mobilemarginBottom;
    }

    let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<div id="container" on:click={toggle}>
    <img
        id="profilePic"
        src={profilePic}
        style="width: {picWidth}vw; margin-left: {marginLeft}vw; margin-bottom:{marginBottom}vw;"
        alt="{name}'s profile pic."
    >

    <div class="centerText">
        <p id="name">{name}</p>

        <div id="jobDescWrapper">
            <p id="jobDesc">//{jobDesc}</p>
        </div>

        <div id="likesDislikesWrapper">
            <p id="likesDislikes">Likes: {likes}</p>
        </div>

        <div id="likesDislikesWrapper">
            <p id="likesDislikes">Dislikes: {dislikes}</p>
        </div>
    </div>
</div>

{#if modalOpen}
    {#if innerWidth>1023}
        <div id="modal">
            <div class="col1">
                <img
                    id="profilePic"
                    src={profilePic}
                    style="margin-left: {modalLeft}vw; margin-bottom:{modalBottom}vw;"
                    alt="{name}'s profile pic."
                >
            </div>

            <div class="col2">
                <div id="info" class="centerText verticalCenter">
                    <p id="name">{name}</p>

                    <div id="jobDescWrapper">
                        <p id="jobDesc">//{jobDesc}</p>
                    </div>

                    <div id="likesDislikesWrapper">
                        <p id="likesDislikes">Likes: {likes}</p>
                    </div>

                    <div id="likesDislikesWrapper">
                        <p id="likesDislikes">Dislikes: {dislikes}</p>
                    </div>
                </div>
            </div>

            <div class="col3">
                <p id="intro" class="verticalCenter">{intro}</p>
            </div>
        </div>
    {:else}
        <div id="modal">
            <!-- for mobile modal, everything besides name is hidden -->
            <div class="mobilecol">
                <p id="titlename">{name}</p>
            </div>
    
            <div class="col3">
                <p id="intro" class="verticalCenter">{intro}</p>
            </div>
        </div>    
    {/if}
    <div id="backdrop" on:click={toggle}></div>
{/if}

<style>
    #container{
        width: 17.5vw;
        bottom: 0;
    }

    #container:hover{
        opacity: .5;
        cursor: pointer;
    }

    #name{
        font-size: 1.5vw;
        margin-bottom: -0.5vw;
    }

    #jobDescWrapper{
        height: 2.5vw;
    }

    #jobDesc{
        font-size: 0.9vw;
        line-height: 115%;
    }

    #likesDislikesWrapper{
        height: 3vw;
    }

    #likesDislikes{
        line-height: 115%;
    }

    /* modal styling */
    #backdrop{
        height: 100vh;
        width: 100vw;
        background-color: hsla(0,0%,17.6%,0.4);
        position: fixed;
        top: 0;
        left: 0;
        backdrop-filter: blur(3px);
        z-index: 98;
        animation: fadeIn .5s ease-in-out;
        cursor: pointer;
    }

    #modal{
        width: 60vw;
        height: 70vh;
        background-color: var(--grack_dark);
        color: var(--offwhite_gentle);
        position: fixed;
        top: 15vh;
        left: 20vw;
        border-radius: var(--r4);
        display: flex;
        z-index: 99;
        animation: slideUp .2s ease-in-out;
    }

    .col1{
        flex: 2;
        position: relative;
    }

    .col2{
        flex: 1.05;
        position: relative;
    }

    .col3{
        flex: 2;
        padding-right: 1vw;
    }

    #modal > .col1 > #profilePic {
        height: 60vh;
        position: absolute;
        bottom: 0;
    }

    .verticalCenter{
        position: absolute;
        top: 50%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
    }

    #info{
        left: -3.5vw;
    }

    #intro{
        padding: 1.5vw;
    }



    /* styling profile before modal shows up */
    @media screen and (max-width:35.5625em){
        #container{
            width:100%;
        }

        #name{
            font-size:5vw;
            margin:auto;
            line-height:100%;
        }

        #jobDesc{
            font-size:2.5vw;
            margin:auto;
        }

        #likesDislikesWrapper{
            height:5vw;
            margin:auto;
        }

        #jobDescWrapper{
            margin:auto;
        }

        .centerText{
            display:flex;
            flex-direction:column;
            row-gap:3vw;
        }

        #profilePic{
            transform:translateX(60%);
        }
    }

    /* tablet modal */
    @media screen and (max-width:64em){
        #intro{
            text-align:center;
            margin-left:3vw;
            margin-right:3vw;
        }

        .mobilecol{
            display:block;
        }

        #titlename{
            font-size:4vw;
            text-align:center;
            line-height:100%;
            margin-top:10%;
        }

        #backdrop{
            z-index:99;
        }

        #modal{
            margin:auto;
            z-index:100;
            flex-direction:column;
        }

        .col1{
            display:none;
        }

        .col2{
            display:none;
        } 
    }

    /* deals with mobile modal */
    @media screen and (max-width:35.5625em){
        #intro{
            font-size:4vw;
            text-align:center;
            margin-left:3vw;
            margin-right:3vw;
        }

        .mobilecol{
            display:block;
        }

        #titlename{
            font-size:10vw;
            text-align:center;
            line-height:100%;
            margin-top:10vw;
        }
        
        #backdrop{
            z-index:49;
        }

        #modal{
            width:100%;
            margin:auto;
            left:0;
            height:100%;
            z-index:50;
            flex-direction:column;
        }

        .col1{
            display:none;
        }

        .col2{
            display:none;
        }
    }
</style>