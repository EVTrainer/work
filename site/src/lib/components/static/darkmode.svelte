<script lang="ts">
    import { lightdark } from '/src/stores/lightdark';
    let darkOn:boolean;
    lightdark.subscribe(value => {
        darkOn=value;
    })
    let text:string;
    let display:string;
    let rayDisplay:string; 
    let textColor:string; 
    let backgroundColor:string;
    let border:string;
    let format:string;
    let favicon = "favicon_dark"

    if(window.matchMedia("(prefers-color-scheme:dark)").matches){
        text = "on";
        display = "block";
        rayDisplay = "none";
        textColor = "rgb(255, 250, 240)";
        backgroundColor = "rgb(45,45,45)";
        border = ".5px solid rgb(255,250,240)";
        format = "left";
        document.documentElement.className = "dark";
        favicon = "favicon_light";
    } else {
        text = "off";
        display = "none";
        rayDisplay = "inline";
        textColor = "rgb(45,45,45)";
        backgroundColor = "rgb(255,250,240)";
        border = "0.5px solid rgb(45, 45, 45)";
        format = "right";
    }
    const toggle = () => {
        if (darkOn == true){
            document.documentElement.className = "light"

            format = "right";
            border = "0.5px solid rgb(45, 45, 45)";
            text = "off"
            textColor = "rgb(45,45,45)";
            display = "none";
            backgroundColor = "rgb(255,250,240)";
            rayDisplay = "inline";
        } else {
            document.documentElement.className = "dark"

            format = "left"; 
            border = "0.5px solid rgb(195, 190, 180)";
            textColor = "rgb(195, 190, 180)";
            text = "on"
            backgroundColor = "rgb(42.5, 45, 45)";
            display = "block";
            rayDisplay = "none";
        }
        lightdark.update(darkOn => !darkOn);
    }
</script>
    <svelte:head>
        <link rel="shortcut icon" type="image/png" href="/img/assets/logos/{favicon}.png">
    </svelte:head>

    <input type="checkbox" id="buttonClick"/>
   
    <label id="darkMode" for="buttonClick" style="background-color: {backgroundColor}; border: {border}" on:click={toggle}> 
        <div id="bigdot" style="display: {display}"></div>

        <p class="text" style="float: {format}; color: {textColor}"> {text} </p>

        <div id="wrapper">
            <div id="dot" class:dotmove={darkOn}></div>
        </div>

        <img id="image" style="display: {rayDisplay}" src="/img/assets/icons/darkMode/sunRays.png" alt="rays">
    </label>

<style>
    @media screen and (max-width:35.5625em){
        #darkMode{
            margin-top: 10.5vh;
        }
    }

   .text{
       display:inline;
       position:relative;
       font-size:.708vw;
       margin-left:.5vw;
       top:50%;
       transform: translateY(-50%);
   }
   
   #bigdot{
       width:1.5vw; 
       height:1.5vw;  
       background-color: rgb(255,250,240);
       display:none;
       position:absolute;
       border-radius:10000px;
       margin-left:3vw;
       top:50%;
       transform: translate(0,-50%);
   }
   
   #image{
       width:1.875vw;  
       height:1.875vw;
       left:1.15vw;
       top:50%;
       transform: translate(0, -50%);
       position:absolute;
   }
   
   #wrapper{
       position:absolute;
       top:50%;
       transform: translate(0 ,-50%);
   }
   
   #dot{
        width:1.25vw;
        height:1.25vw;
        border-radius:0.625vw;
        float:left;
        position:relative;
        margin-left:.25vw;
        -webkit-transition: .5s;
        -ms-transition: -5s;
        transition: .5s;
        transition-timing-function: ease-in-out;
        background-color:rgb(45,45,45);
   }
   
   .dotmove{
        -webkit-transform: translate(2.60vw, -.4vh);
        -ms-transform: translate(2.60vw, -.4vh);
        transform: translate(2.6vw, -.4vh); 
   }
   
   #darkMode{
        border-radius: 5vw;
        background-color: rgb(255,250,240);
        width:5vw;
        height:5vh;
        top:50%;
        transform: translate(-30%, -50%);
        margin-left:-30%;
        position:relative;
        float:right;
        padding-right: .5vw;
        cursor:pointer;
        transition: background-color .5s;
   }
   
   #buttonClick{
        display:none;
   }
   
   #buttonClick:checked + label{
        background-color: rgb(45, 45, 45);
   }

   @media screen and (max-width:64em){
        #darkMode{
            width:6.5vw;
        }
        .text{
            font-size:1vw;
        }
        #dot{
            margin-top:-.05vw;
            width:1.75vw;
            height:1.75vw;
            border-radius:10000vw;
        }
        #bigdot{
            margin-left:3.5vw;
            width:2.25vw;
            height:2.25vw;
        }
        #image{
            margin-left:.25vw;
            width:2.6vw;
            height:2.6vw;
        }
        .dotmove{
        -webkit-transform: translate(3vw, -.3vh);
        -ms-transform: translate(3vw, -.3vh);
        transform: translate(3vw, -.3vh); 
       }
   }

    @media screen and (max-width:35.5625em){
       #darkMode{
           height:5vh;
           width:20vw;
           border-radius:1000vw;
           margin-right:-2.5vw;
       }


       .text{
           font-size:2.5vw;
           margin-left:2vw;
           margin-right:1vw;
       }

       #image{
            width:7.5vw;
            height:7.5vw;
            margin-left:3.5vw;
       }

       #dot{
            width:5vw;
            height:5vw;
            border-radius:10000vw;
            margin-left: 1vw;
            margin-top: none;
       }

       #bigdot{
           width:6vw;
           height:6vw;
           margin-left:12vw;
       }

       .dotmove{
        -webkit-transform: translate(10vw, -.6vh);
        -ms-transform: translate(10vw, -.6vh);
        transform: translate(10vw, -.6vh); 
       }
   }
</style>