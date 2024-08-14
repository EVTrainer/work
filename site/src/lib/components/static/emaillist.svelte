<script lang="ts">
    let submitStatus: string;
    const submitForm = async(data) => {
        submitStatus = "submitting"
        const formData = new FormData(data.currentTarget);

        const res = await fetch(
            "email.json", 
            {
                method: "POST",
                body: formData,
            }
        );

        const {message}:any = await res.json;
        submitStatus = message;
    };
</script>

<div>
    {#if submitStatus === "submitting"}
        <p class="centerText">submitting...</p>
    {:else if submitStatus === "failed"}
        <p class="centerText">form submission failed :&#40;</p>
    {:else if submitStatus === "success"}
        <p class="centerText">successfully submitted :D</p>
    {:else}
        <form class="container" on:submit|preventDefault={submitForm}>
            <div class="title">
                <p>Be the first to know!</p>
            </div>
        
            <div>
                <input class="email" type="email" name="email" placeholder="coolperson@email.com">
            </div>
        
            <div>
                <input class="submit" type="submit" value="submit">
            </div> 
        </form>
    {/if}
</div>

<style>
    .container{
        display: flex;
        margin-left: 9vw;
    }

    .email{
        border-radius: var(--r6);
        height: 2vw;
        width: 25vw;
        border: none;
        margin-top: .5vh;
        margin-bottom: .5vh;
        margin-left: 1vw;
        padding-left: 1vw;
        padding-right: 1vw;
        background-color: var(--offwhite_grack);
        font-family: c10p;
        outline: none;
        color: var(--grack_gentle);
    }

    .submit{
        border-radius: var(--r6);
        height: 2vw;
        width: 7vw;
        border: 2px solid var(--offwhite_pop);
        margin-top: .5vh;
        margin-bottom: .5vh;
        margin-left: 1vw;
        background-color: var(--grack_dark);
        font-family: c10p;
        outline: none;
        color: var(--offwhite_pop);
    }

    .submit:hover{
        cursor: pointer;
        background-color: var(--offwhite_pop);
        color: var(--grack_dark);
    }

    .title{
        margin-top: .5vh;
    }

    @media screen and (max-width:64em){
        .submit{
            font-size:1.25vw;
        }
    }

    @media screen and (max-width:35.5625em){
        .container{
            display:flex;
            flex-direction:column;
            margin:auto;
            row-gap:5vw;
        }
        .submit{
            height:6vw;
            width:21vw;
        }
        .email{
            width:50vw;
            height:4vw;
        }
    }
</style>