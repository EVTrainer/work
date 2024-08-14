<script lang="ts">
    import {page} from "$app/stores";

    let bool = false;
    let sign = "+";
    let display3 = "none";

    let display = "none";
    let togglemenu = () => {
        if(bool == true){
            setTimeout(function(){display = "none"}, 100);
            sign = "+";
            display3 = "none";
            sign2 = "+";
            display2 = "none";
        }else{
            display = "block";
        }
        bool = !bool;
    }
    
    let textChange = () => {
        if(sign == "+"){
            sign = "-";
            display3 = "block";
        }else{
            sign = "+";
            display3 = "none"
        }
    }
    
    let sign2 = "+";
    let display2 = "none";
    let textChange2 = () => {
        if(sign2 == "+"){
            sign2 = "-";
            display2 = "block";
        }else{
            sign2 = "+";
            display2 = "none"
        }
    }
    // scrolls nav up with banner gone
</script>

<!-- menu -->
<div class="menu" class:open={bool} on:click={togglemenu}></div>
   
<nav class="nav" style="display: {display}" class:slide={bool} class:slideleft={!bool}>
    <ul class="navLi">
        <li><a href="/" on:click={togglemenu}><p class:inactive={$page.url.pathname !== "/"}>&gt;</p> <p class:inactive={$page.url.pathname == "/"}>&nbsp;</p> <p>&nbsp;home</p></a></li>
        
        <br>

        <li><a href="/ourtech" on:click={togglemenu}><p class:inactive={$page.url.pathname !== "/ourtech"}>&gt;</p> <p class:inactive={$page.url.pathname == "/ourtech"}>&nbsp;</p> <p>&nbsp;our tech </p> </a><p class="sign" on:click={textChange}> {sign} </p> 
            <ul class="subMenu" style="display: {display3};">
                <li><a href="/carpenter" on:click={togglemenu}><p class:inactive={$page.url.pathname !== "/carpenter"}>&gt;</p> <p class:inactive={$page.url.pathname == "/carpenter"}>&nbsp;</p> <p>&nbsp;carpenter</p></a></li>
                <li><a href="/machinist" on:click={togglemenu}><p class:inactive={$page.url.pathname !== "/machinist"}>&gt;</p> <p class:inactive={$page.url.pathname == "/machinist"}>&nbsp;</p> <p>&nbsp;machinist</p></a></li>
            </ul>
        </li>

        <br>

        <li><a href="/aboutus" on:click={togglemenu}><p class:inactive={$page.url.pathname !== "/aboutus"}>&gt;</p> <p class:inactive={$page.url.pathname == "/aboutus"}>&nbsp;</p> <p>&nbsp;about us </p> </a> <p class="sign" on:click={textChange2}> {sign2} </p>
            <ul class="subMenu" style="display: {display2};">
                <li><a href="/aboutus/blog" on:click={togglemenu}><p class:inactive={$page.url.pathname !== "/aboutus/blog"}>&gt;</p> <p class:inactive={$page.url.pathname == "/aboutus/blog"}>&nbsp;</p> <p>&nbsp;our blog</p></a></li>
                <li><a href="/aboutus/ourstory" on:click={togglemenu}><p class:inactive={$page.url.pathname !== "/aboutus/ourstory"}>&gt;</p> <p class:inactive={$page.url.pathname == "/aboutus/ourstory"}>&nbsp;</p> <p>&nbsp;our story</p></a></li>
                <li><a href="/aboutus/ourteam" on:click={togglemenu}><p class:inactive={$page.url.pathname !== "/aboutus/ourteam"}>&gt;</p> <p class:inactive={$page.url.pathname == "/aboutus/ourteam"}>&nbsp;</p> <p>&nbsp;our team</p></a></li>
            </ul>
        </li>
        <br>
        <li on:click={togglemenu}><a href="/#talkToUs"><p class:inactive={$page.url.pathname !== "/#talkToUs"}>&gt;</p> <p class:inactive={$page.url.pathname == "/#talktous"}>&nbsp;</p> <p>&nbsp;talk to us</p></a></li>
    </ul>

    <div id="backdrop" on:click={togglemenu}></div>
</nav>
       
<style>
    .nav{
        position: fixed;
        background-color: transparent;
        width:100%;
        opacity:1;
        height:120%;
        backdrop-filter: blur(3px);
    }

    #backdrop{
        height:120vh;
        width:100vw;
        background-color:var(--offwhite_grack);
        opacity:.5;
        position: fixed;
        top: 0;
        left: 0;
    }

    .navLi{
        margin-top:20vh;
    }
   
    .menu {
        margin-top: 10vh;
        width: 10vw;
        height: .75vh;
        background-color: var(--grack_gentle);
        border-radius: 5px;
        position:absolute;
        top:50%;
        margin-left:3vw;
        z-index: 98;
    }

    .menu::before,
    .menu::after {
        content: '';
        position: absolute;
        width: 10vw;
        height: .75vh;
        background-color: var(--grack_gentle);
        border-radius: 5px;
   }

    .menu::before {
        transform: translateY(-2vh);
    }

   .menu::after {
        transform: translateY(2vh);
    }
   
    .open{
        transform: translateX(-50px);
        background: transparent;
        box-shadow: none;
    }

    .open::before {
        transform: rotate(45deg) translate(35px, -35px);
    }

    .open::after {
        transform: rotate(-45deg) translate(35px, 35px);
    }

    .navLi li{
        list-style: none;
        text-align: left;
        position: relative;
        padding-left: 5vw;
        padding-top: 5vw;
        z-index:99;
    }

    @media screen and (min-width:35.5625em){
        .navLi li{
            padding-top:2.5vw;
        }
    }

    .navLi li a{
        text-decoration: none;
    }

    .navLi li a:hover{
        text-decoration: none;
        font-weight: bold;
    }

    .subMenu{
        margin-left: 5vw;   
    }

    p{
        display: inline;
        color: var(--grack_gentle); 
        font-size:6vw;
        text-align:center;
    }

    .sign{
        right:0;
        padding-right:10vw;
        font-size:10vw;
        transform: translateY(-25%);
        position:absolute;
    }

    @media screen and (min-width:35.5625em){
        p{font-size:3vw;}
        .sign{
            font-size:5vw;
        }
    }

    .inactive{
        display: none;
    }

    .slide{
        animation: .5s alternate slideRight;
    }

    .slideleft{
        animation: .5s alternate slideRight2;
    }
</style>