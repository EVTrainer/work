import { onMount } from 'svelte';
import { writable } from 'svelte/store';

let bool;

if (typeof window !== 'undefined') {
    if(window.matchMedia("(prefers-color-scheme:dark)").matches){
        bool=true;
    } else {
        bool=false;
    }  
}

export let lightdark = writable(bool);