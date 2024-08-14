<script lang="ts">
    import Button from '$lib/components/reusable/button.svelte'
    let loggedIn=true

    let code;
    let codeEntered;

    const handleInput = (e) => {
        code = e.target.value.toUpperCase();

        if(code == "SPACE"){
            codeEntered = true;
        }else{
            codeEntered = false;
        }
    }

    import { lightdark } from '/src/stores/lightdark';
    let darkOn:boolean;
    lightdark.subscribe(value => {
        darkOn=value;
    })
</script>

<svelte:head>
    <title>prog. beta</title>
    <meta name="description" content="we invite you to take part in beta testing of machinist.">
</svelte:head>

{#if loggedIn}
    {#if codeEntered}
        <div id="main" class="main">
            <div id="gradient">
                <div id="landing">
                    <div id="depositBox">
                        <a href="/beta/deposit"><h4 id="deposit" class="centerText">submit<br>deposit</h4></a>
                        <h6 class="centerText">250 due Jul 04</h6>
                    </div>
                </div>
    
                <h6 id="welcome" class="centerText">welcome to program beta. we're glad to see you.</h6>

                <img id="machinist" src="/img/machinist/lightOpen_grack.png" alt="Machinist CNC mill">

                <h6 id="intro" class="mainPadding centerText">This will be your machine. <br> We call her "Machinist".</h6>
            </div>

            <h6 id="intro" class="mainPadding centerText">She's designed by former student team members, <br> for current student team members.</h6>

            <h6 id="intro" class="mainPadding centerText">Choose from 2 colorways: light mode & dark mode. <br> 7000 & 7500, respectively.</h6>

            <h6 id="intro" class="mainPadding centerText">We invite you to take a first look at her. <br> And help us bring Machinist to the wider market.</h6>

            <h6 id="intro" class="mainPadding centerText">Reserve your machine for 250 by Jul 04 <br> and learn more by clicking 
                {#if darkOn}
                    <a href="/machinist">here</a>.
                {:else}
                    <a href="/machinist"><u style="color: var(--offwhite_grack)">here</u></a>.
                {/if}
            </h6>
            
            <img id="parachutes" src="/img/parachutes.jpg" alt="Zack and Alex holding parachutes.">

            <p class="centerText">//Rutgers Rocket Propulsion Lab, where it started.</p>

            {#if darkOn}
                <img id="progB" src="/img/assets/logos/progB_gentle.png" alt="Program Beta Logo.">
                <img id="progBTimeline" src="/img/progBTimeline_gentle.png" alt="Program Beta Timeline">
            {:else}
                <img id="progB" src="/img/assets/logos/progB_offwhite.png" alt="Program Beta Logo.">
                <img id="progBTimeline" src="/img/progBTimeline_offwhite.png" alt="Program Beta Timeline">
            {/if}

            <!-- chat with a founder -->
            <h2 id="chat" class="mainPadding">chat with <br> a founder</h2>
            <div id="contact" class="mainPadding">
                <h4>Zack</h4>
                <div class="split">
                    <h6>zachariah@thecncco.com</h6>
                    <h6 class="rightAlign">609-756-7766</h6>
                </div>
                <p>specialty: cnc expert</p>
                <p>habits: not quite good at answering his phone :&#40; but you can spam him :D</p>
            </div>

            <div id="contact" class="mainPadding">
                <h4>Alex</h4>

                <div class="split">
                    <h6>alex@thecncco.com</h6>
                    <h6 class="rightAlign">732-640-3933</h6>
                </div>

                <p>specialty: cnc expert</p>
                <p>habits: good with texts, will get calls most times.</p>
            </div>

            <div id="contact" class="mainPadding">
                <h4>Chianli</h4>

                <div class="split">
                    <h6>chianli@thecncco.com</h6>
                    <h6 class="rightAlign">732-762-2854</h6>
                </div>

                <p>specialty: program beta coordinator</p>
                <p>habits: fast with calls and texts, give a day or two for email.</p>
            </div>

            <!-- submit deposit -->
            <div id="depositBox2">
                <a href="/beta/deposit"><h4 id="deposit" class="centerText">submit<br>deposit</h4></a>
            </div>
        </div>
    {:else}
        <div class="main mainPadding">
            <h2 class="centerText">enter your code</h2>
            <input id="code" type="text" style="text-transform:uppercase" on:input={handleInput}>
            {#if darkOn}
                <p class="centerText"><a href="/#talkToUs" class="grackPop">contact us</a> to request a code</p>
            {:else}
                <p class="centerText"><a href="/#talkToUs"><u>contact us</u></a> to request a code</p>
            {/if}
        </div>
    {/if}
{:else}
    <div class="main mainPadding">
        <h4 class="centerText">log in to access your machine.</h4>

        <br>
        <br>

        <div id="centerDiv">
            <Button text="login"/>
            <br><br>
            <Button text="register"/>
        </div>
    </div>
{/if}

<style>
    #centerDiv{
        display: inline-block;
        position: relative;
        left: 50%;
        transform: translate(-50%);
    }

    #code{
        width: 80%;
        height: 20vh;
        color: var(--grack_pop);
        font-size: 15vh;
        font-family: c10p;
        text-align: center;
        background-color: var(--offwhite_grack);
        border: 3px solid var(--grack_pop);
        border-radius: var(--r4);
        padding-left: 2vw;
        padding-right: 2vw;
        margin-top: 7.5vh;
        margin-bottom: 5vh;
        position: relative;
        left: 50%;
        transform: translate(-50%);
        outline: none;
    }

    @media screen and (max-width:35.5625em){
        #code{
            font-size: 5vh;
            height: 7.5vh;
        }
    }

    /* logged in, code entered */
    #main{
        padding-bottom: 15vh;
        background-color: var(--grack);
        padding-top: 0vh;
        color: var(--offwhite_gentle);
    }

    #landing{
        background-image: url("/img/blackhole.png");
        background-size: 90vw;
        background-repeat: no-repeat;
        height: 115vh;
    }

    @media screen and (max-width:35.5625em){
        #landing{
            height: 60vh;
        }
    }

    #gradient{
        background-image: linear-gradient(180deg, black, var(--grack));
    }

    #depositBox{
        margin-top: 15vh;
        width: 30vw;
        float: right;
    }

    @media screen and (max-width:35.5625em){
        #depositBox{
            margin-top: 20vh;
            height: 20vh;
            margin-right: 10%;
            width: 45%;
        }
    }

    #deposit{
        color: var(--grack);
        -webkit-text-stroke-width: 1px;
        -webkit-text-stroke-color: rgb(100,200,180);
    }

    #deposit:hover{
        cursor: pointer;
        color: rgb(100,200,180);
    }

    #welcome{
        margin-top: -10vh;
        margin-bottom: 10vh;
    }

    @media screen and (max-width:35.5625em){
        #welcome{
            width: 60vw;
            margin-left: 20vw;
        }
    }

    #machinist{
        width: 70%;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    #intro{
        margin-top: 7.5vh;
    }

    #parachutes{
        width: 80%;
        margin-top: 10vh;
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: var(--r4);
    }

    #progB{
        width: 50%;
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-top: 15vh;
    }

    #depositBox2{
        width: 30vw;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    #progBTimeline{
        margin: 10%;
        width: 80%;
    }

    /* contact */
    #contact{
        margin-bottom: 10vh;
    }

    #chat{
        text-align: right;
        margin-top: 10vh;
        margin-bottom: 10vh;
    }

    @media screen and (max-width:35.5625em){
        #chat{
            text-align: center;
        }
    }

    @media screen and (max-width:35.5625em){
        .rightAlign{
            text-align: left;
        }
    }
</style>