<script lang="ts">
    import { modalStatus } from '../../../stores/modalStore';

    // modal store
    let showModal:boolean;

    modalStatus.subscribe(value => {
        showModal = value;
    })

	const toggleModal = () => {
		modalStatus.update(showModal => !showModal);
	}
</script>

{#if showModal}
    <div id="modal">
        <p>Hi, we're sorry to say that THE CNC COMPANY has been dissolved as of August 2022. In accordance with this, we've removed features of this site such as authentication and purchasing while directing contact forms elsewhere. We'd like to thank everyone who's supported us along this journey.</p>
        <br>
        <p>Best,</p>
        <p>THE CNC COMPANY team.</p>
    </div>

    <div id="backdrop" on:click={toggleModal}></div>
{/if}

<style>
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
        padding: 5%;
        width: 60vw;
        height: 70vh;
        background-color: var(--grack_dark);
        color: var(--offwhite_gentle);
        position: fixed;
        top: 15vh;
        left: 20vw;
        border-radius: var(--r4);
        z-index: 99;
        animation: slideUp .2s ease-in-out;
    }

    /* tablet modal */
    @media screen and (max-width:64em){
        #backdrop{
            z-index:99;
        }

        #modal{
            margin:auto;
            z-index:100;
            flex-direction:column;
        }
    }

    /* deals with mobile modal */
    @media screen and (max-width:35.5625em){
        #backdrop{
            z-index:49;
        }

        #modal{
            width:100%;
            margin:auto;
            left:0;
            height:100%;
            z-index:50;
        }
    }
</style>