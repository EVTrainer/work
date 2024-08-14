<script>
    export let blogs
</script>

<div class="latest">
    {#each blogs as blog}
    <a href="{blog.path}">
        <div class="miniCard">
            <p>by {blog.author}</p>
            <h1 class="miniTitle">{blog.title}</h1>
            <div class="blogInfo">
                <div class="blogdate"><p>{blog.date}</p></div>
                <div class="readtime"><p>{blog.readtime} min read</p></div>
            </div>
        </div>
    </a>
    {/each}
</div>

<style>
    .miniCard{
        width: 24vw;
        height: 15vw;
        background-color: var(--grack_dark);
        color: var(--offwhite_gentle);
        border-radius: 1vw;
        padding: 1vw 2.5vw 2.5vw 2vw;
        position: relative;
        margin-bottom: .5em;
    }

    .miniCard:hover{
        opacity: 0.95;
    }

    .miniTitle{
        font-size: 2.5vw;
    }

    .blogInfo{
        width: 20vw;
        position: absolute;
        bottom: 1vw;
    }

    .latest{
        margin-left: -5vw;
        margin-right: -5vw;
        padding-left: 5vw;

        display: grid;
        grid-auto-flow: column;
        gap: .5vw;

        overflow-x: auto;
        overscroll-behavior-inline: contain;
    }

    .blogdate{
        float: left;
    }

    .readtime{
        float: right;
    }

    @media screen and (max-width:35.5625em){
        .latest{
            margin:auto;
            padding:auto;
            column-gap:5vw;
        }
        .miniCard{
            width:56vw;
            height:35vw;
        }

        .blogdate{
            margin-top:3vw;
            float:none;

        }

        .readtime{
            float:none;
        }
        .blogInfo{
            position:relative;
            width:30vw;

        }
        .miniTitle{
            font-size:7.5vw;
        }
        .blogtext{
            font-size:3vw;
        }
    }
</style>