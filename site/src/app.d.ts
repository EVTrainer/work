/// <reference types="@sveltejs/kit" />

declare namespace App {
    interface Locals {
      user?: { email: string }
    }
  
   // interface Platform {}
  
   interface Session {
      user?: { email: string }
    }
  
   // interface Stuff {}
  }