<script lang="ts">
    import Close from "$lib/components/static/close.svelte";

    // x out button
    let hide = false;
    const close = () => {
        hide = true;
    }

    // animate in after delay
    let inserted:boolean = false;
    let insert = () => {
        inserted = true;
    }

    const myTimeout = setTimeout(insert, 3000);
</script>

{#if inserted}
    <div id="container" class:close={hide}>
        <div on:click={close}>
            <Close/>
        </div>
        <p id="text">We use cookies 🍪. Learn more in our <a href="/privacy"><u>privacy policy</u></a>.</p>
    </div>
{/if}

<style>
    #container{
        width: 100%;
        background-color: var(--offwhite_grack);
        color: var(--grack_gentle);
        border-radius: var(--r5);
        position: absolute;
        bottom: 0;
        padding: 1vh 1vw 1vh 1vw;
        animation-name: slideLeft;
        animation-duration: 2s;
        z-index: 98;
        transition: transform 1s;
    }

    .close{
        transform: translateX(13.75vw);
        -webkit-transform: translateX(13.75vw);
    }

    #text{
        font-size: 0.8vw;
    }

    a{
        text-decoration: none;
        color: var(--grack_pop);
    }

    a:hover{
        opacity: 0.5;
    }
</style>