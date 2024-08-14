<script lang="ts">
    let submitStatus: string;
    const submitForm = async(data) => {
        submitStatus = "submitting"
        const formData = new FormData(data.currentTarget);

        const res = await fetch(
            "contact.json",
            {
                method: "POST",
                body: formData,
            }
        );

        const {message}:any = await res.json;
        submitStatus = message;
    };
</script>

<div class="container">
    <div class="subContainer">
        {#if submitStatus === "submitting"}
            <h4 class="centerText">submitting...</h4>
        {:else if submitStatus === "failed"}
            <h4 class="centerText">form submission failed :&#40;</h4>
        {:else if submitStatus === "success"}
            <h4 class="centerText">successfully submitted :D</h4>
        {:else}
            <form on:submit|preventDefault={submitForm}>
                <div class="row">
                    <div class="col">
                        <p>what's your name?</p>
                        <input class="shorttext" type="text" name="name" placeholder="Leeroy Jenkins">

                        <br>

                        <p>what's your email and/or phone #?</p>
                        <input class="shorttext" type="email" name="email" placeholder="leeroyj@gmail.com">
                        <input class="shorttext" type="tel" name="phone" placeholder="732-420-2984">
                    </div>    

                    <div class="col">
                        <p>what would you like to tell us?</p>
                        <textarea name="message" placeholder="I love your machines! When will the Kickstarter launch?"></textarea>
                    </div>

                    <div class="submitDiv">
                        <input class="submit" type="submit" value="submit">
                    </div> 
                </div>
            </form>
        {/if}
    </div>
</div>    

<style>
    .container{
        position: relative;
        background-color: var(--grack_dark);
        border-radius: var(--r4);
        height: 45vh;
    }

    .subContainer{
        position: absolute;
        width: 90%;
        top: 50%; left: 50%;
        transform: translate(-50%,-50%);
    }

    p{
        color: var(--offwhite_gentle);
    }

    h4{
        color: var(--offwhite_gentle);
    }

    input{
        border-radius: var(--r6);
        border: 2px solid var(--offwhite_grack);;
        margin-top: .5vh;
        margin-bottom: .5vh;
        padding-left: 1vw;
        padding-right: 1vw;
        background-color: var(--offwhite_grack);
        font-family: c10p;
        outline: none;
        color: var(--grack_gentle);
    }

    .row{
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        width: 100%;
    }

    .col{
        display: flex;
        flex-direction: column;
        flex-basis: 100%;
        flex: 1;
    }
    .shorttext{
        width: 22vw;
    }

    textarea{
        width: 25vw;
        height: 100%;
        border-radius: var(--r6);
        margin-top: .5vh;
        margin-bottom: .5vh;
        padding-left: 1vw;
        padding-right: 1vw;
        padding-top: .5vw;
        padding-bottom: .5vw;
        background-color: var(--offwhite_grack);
        font-family: c10p;
        outline: none;
        color: var(--grack_gentle);
        resize: none;
        border: none;
    }

    .submitDiv{
        display: block;
        margin-top: 3vh;
        margin-left: auto;
        margin-right: auto;
        height: 3vw;
    }

    .submit{
        border-radius: var(--r5);
        line-height: 2;
        border: 2px solid var(--offwhite_pop);;
        margin-top: .5vh;
        margin-bottom: .5vh;
        width: 9vw;
        background-color: var(--grack_dark);
        font-family: c10p;
        outline: none;
        color: var(--offwhite_pop);
    }

    .submit:hover{
        cursor: pointer;
        line-height: 2;
        border: 2px solid var(--offwhite_pop);;
        margin-top: .5vh;
        margin-bottom: .5vh;
        width: 9vw;
        background-color: var(--offwhite_pop);
        font-family: c10p;
        outline: none;
        color: var(--grack_dark);
    }

    @media screen and (max-width:64em){
        .submitDiv{
            margin-bottom:2vw;
        }
    }

    @media screen and (max-width:35.5625em){
        .row{
            display:flex;
            flex-direction:column;
            text-align: center;
        }

        .shorttext{
            width:75vw;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }

        .submit{
            width:20vw;
        }

        .submitDiv{
            margin-top:0;
            margin-bottom:0;
        }

        textarea{
            width:75vw;
        }

        .container{
            height:100vw;
        }
    }
</style>