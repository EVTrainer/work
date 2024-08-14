<script context="module" lang="ts">
    import type { Load } from '@sveltejs/kit'
  
    export const load: Load = ({ session }) => {
        if (!session.user) {
            return {
                status: 302,
                redirect: '/profile1',
            }
        }
  
        return {
            status: 200,
            props: {
                email: session.user.email,
                // fake password just so input has something showing
                password: session.user.email,
                firstname: session.user.firstname,
            },
        }
    }
</script>
  
<script lang="ts">
    export let email: string
    export let password: string
    export let firstname: string|undefined
    export let lastname: string|undefined

    import { lightdark } from '/src/stores/lightdark';
    let darkOn:boolean;
    lightdark.subscribe((value: boolean) => {
        darkOn=value;
    })

    const update = async(event: SubmitEvent) => {}


    let loggedIn:boolean = false;
    let profilePicExists:boolean = false
    let profilePic:string = "/img/profile_offwhite.png"

    let firstNameUnsaved:boolean = false
    let nameHide:boolean = true
    const firstNameInput = () => {
        firstNameUnsaved = true
        nameHide = false
    }

    let lastNameUnsaved:boolean = false
    const lastNameInput = () => {
        lastNameUnsaved = true
        nameHide = false
    }

    let emailUnsaved:boolean = false
    const emailInput = () => {
        emailUnsaved = true
    }

    let passwordUnsaved:boolean = false
    const passwordInput = () => {
        passwordUnsaved = true
    }

    let hidePassword:boolean = false
    let hideCurrentPassword:boolean = true
    const showCurrentPassword = () => {
        hidePassword = true
        hideCurrentPassword = false
    }
    let hideNewPassword:boolean = true
</script>
    
<div class="main mainPadding">
    <div id="landing" class="split">
        <div style="width: 20vw;">
            {#if profilePicExists}
                <img src="{profilePic}" alt="Profile pic.">
            {:else}
                {#if darkOn}
                    <div id="profileCircle">
                        <img id="profilePic" src="/img/profile_gentle.png" alt="Profile pic.">
                    </div>
                {:else}
                    <div id="profileCircle">
                        <img id="profilePic" src="/img/profile_offwhite.png" alt="Profile pic.">
                    </div>
                {/if}
            {/if}
    
        </div>

        <div style="width: 20vw;">
            <form on:submit|preventDefault={update} action="/auth/register" method="post">
                <textarea 
                    id="bio" 
                    placeholder="your bio - tell the world about yourself!"
                    maxlength="104"
                ></textarea>

                <div class="split">
                    <div>
                        <input 
                            id="firstName"
                            class="input" 
                            type="text" 
                            class:unsaved={firstNameUnsaved} 
                            on:input={firstNameInput} 
                            bind:value={firstname} 
                            placeholder="first name"
                        >
                    </div>
                    <div>
                        <input
                            id="lastName"
                            class="input"
                            type="text"
                            class:unsaved={lastNameUnsaved} 
                            on:input={lastNameInput} 
                            bind:value={lastname} 
                            placeholder="last name"
                        >
                    </div>
                </div>

                <p id="info" class="centerText tinyText" class:hide={nameHide}>
                    you can only change your name once :&#41;
                </p>

                <input
                    class="input"
                    type="text" 
                    class:unsaved={emailUnsaved} 
                    on:input={emailInput} 
                    bind:value={email} 
                    placeholder="{email}"
                >
    
                <input 
                    class="input" 
                    type="password" 
                    class:unsaved={passwordUnsaved}
                    class:hide={hidePassword}
                    on:click={showCurrentPassword} 
                    bind:value={password} 
                    placeholder="********"
                >

                <div class="split">
                    <div>
                        <input 
                            id="oldPassword"
                            class="input" 
                            type="password" 
                            class:unsaved={passwordUnsaved}
                            class:hide={hideCurrentPassword}
                            on:input={passwordInput} 
                            placeholder="enter current password"
                        >
                    </div>

                </div>

                <input 
                    id="newPassword"
                    class="input" 
                    type="text" 
                    class:unsaved={passwordUnsaved} 
                    class:hide={hideNewPassword}
                    on:input={passwordInput} 
                    placeholder="enter new password"
                >
    
                <div id="buttons" class="split">
                    <div>
                        <button id="save" class="button" type="submit">save</button>
                    </div>
                    <div>
                        <button id="logout" class="button" type="submit">logout</button>        
                    </div>
                    <div>
                        <button id="cancel" class="button" type="submit">cancel</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>

<style>
    #landing{
        min-height: 65vh
    }

    #profileCircle{
        height: 15vw;
        width: 15vw;
        background-color: var(--grack);
        border-radius: 7.5vw;
        border: 3px solid var(--grack_gentle);
        margin-left: 2.5vw;
    }

    #profilePic{
        width: 10vw;
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-top: 2.25vw;
    }

    .input{
        width: 100%;
        border-radius: var(--r6);
        background-color: var(--offwhite_grack);
        color: var(--grack_gentle);
        border: 2px solid var(--grack_gentle);
        margin-top: 3vh;
        padding: 0.5vh 0vw 0.5vh 0vw;
        text-align: center;
        outline: none;
        font-size: 1.5vw;
        font-family: c10p;
    }

    .unsaved{
        color: var(--grack_pop);
        border: 2px solid var(--grack_pop);
    }

    /* button styling */
    .button{
        display: block;
        margin: 3vh auto 0 auto;
        border-radius: var(--r6);
        font-family: c10p;
        padding: 0.5vh 0.75vw 0.5vh 0.75vw;
        width: 6.5vw;
    }

    .button:hover{
      cursor: pointer;
    }

    /* save button styling */
    #save{
        background-color: var(--offwhite_grack);
        border: 2px solid var(--grack_pop);
        color: var(--grack_pop);
    }

    #save:hover{
        background-color: var(--grack_pop);
        color: var(--offwhite_grack);
    }

    /* cancel button styling */
    #cancel{
        background-color: var(--offwhite_grack);
        border: 2px solid var(--grack_bang);
        color: var(--grack_bang);
    }

    #cancel:hover{
        background-color: var(--grack_bang);
        color: var(--offwhite_grack);
    }

    /* logout button styling */
    #logout{
        background-color: var(--grack_gentle);
        border: 2px solid var(--grack_gentle);
        color: var(--offwhite_grack);
    }

    #logout:hover{
        background-color: var(--offwhite_grack);
        color: var(--grack_gentle);
    }

    #bio{
        width: 100%;
        height: 20vh;
        border-radius: var(--r6);
        margin-top: 3vh;
        padding-left: 1vw;
        padding-right: 1vw;
        padding-top: .5vw;
        padding-bottom: .5vw;
        background-color: var(--offwhite_grack);
        font-family: c10p;
        outline: none;
        color: var(--grack_gentle);
        resize: none;
        border: 2px solid var(--grack_gentle);
        font-size: 1.5vw;
    }

    #info{
        margin-top: 1.5vh;
        color: var(--grack_pop);
    }

    #buttons{
        width: 80%;
        margin-left: 10%;
    }

    #firstName{
        margin-right: 3%;
        width: 97%;
    }

    #lastName{
        margin-left: 3%;
        width: 97%;

    }
</style>