<script lang="ts">
    export let text: string = "button";
    export let link: string = "/";
</script>

<div class="button">
    <a href={link}><p>{text}</p></a>
</div>

<style>
    .button{
        text-align: center;
        border: 2px solid var(--grack_pop);
        border-radius: var(--r5);
        display: inline-block;
        width: 9vw;
    }

    @media screen and (max-width:64em){
        .button{
            padding: .25vw;
            width: 10vw;
            margin-right: -5vw;
        }
    }

    @media screen and (max-width:35.5625em){
        .button{
            width: 27.5vw;
            margin-top: 1vh;
            padding: none;
            margin-right: none;
        }
    }

    .button:hover{
        background-color: var(--grack_pop);
    }

    .button a{
        text-decoration: none;
        display: block;
    }

    .button a p{
        color: var(--grack_pop);
    }

    .button a p:hover{
        color: var(--offwhite_grack);
    }
</style>