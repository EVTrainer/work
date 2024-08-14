<script>
    export let words = {words};
    export let wait = 3000;

    let txt = '';
    let wordIndex = 0;
    let isDeleting = false;
    words = JSON.parse(words);

    //type method
    let type = () => {
        //current index of word
        const current = wordIndex % words.length;
        //gets full text of current word
        const fullTxt = words[current];
        //check if isDeleting

        if(isDeleting){
            //remove char
            txt = fullTxt.substring(0, txt.length - 1);
        } else {
            //add char
            txt = fullTxt.substring(0, txt.length + 1);
        }
  
        //initial type speed
        let typeSpeed = 200;
    
        if(isDeleting){
            typeSpeed /= 2;
        }
  
        //if word is complete
        if(!isDeleting && txt === fullTxt){
            //make pause at end
            typeSpeed = wait;
            //set delete to true
            isDeleting = true;
            // else if word had delted into nothing
        } else if (isDeleting && txt === '') {
            isDeleting = false;
            //move to next word
            wordIndex++;
            //pause before typing starts again
            typeSpeed = 500;
        }
  
        setTimeout(() => type(), typeSpeed);
    }

    type();
</script>

<span class="txt"> {txt} </span>

<style>
  /* makes cursor */
  .txt{
    border-right: 0.5em solid var(--grack_gentle);
    line-height: 1em;
  }

  @media screen and (max-width:35.5625em){
      .txt{
          font-size:15vw;
      }
  }
</style>