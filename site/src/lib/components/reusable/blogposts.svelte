<script lang="ts">
    import { selectedTags, setSelectedTags } from "/src/stores/tagStore";

    export let tags: Tag
    export let blogs: Blog

    const tagsIncluded = (blog: Blog, searchTags: Tag[]):boolean => {
        for(let i=0; i<searchTags.length; i++){
            if(blog.tags.includes(searchTags[i])){
                return true
            }
        }
        return false
    }

    const selected = (id: number, searchTags: Tag[]):boolean => {
        for(let i=0; i<searchTags.length; i++){
            if(id == searchTags[i].id){
                return true
            }
        }
        return false
    }
</script>

<div class="tagSection">
    <div class="tagCenter">
        {#each tags as tag}
            {#if selected(tag.id, $selectedTags)}
                <button class="tag"
                on:click={() => setSelectedTags(tag)}
                style="background-color: {tag.color}; height: 3vw;">
                    <p>{tag.name}</p>
                </button>
            {:else}
                <button class="tag"
                on:click={() => setSelectedTags(tag)}
                style="background-color: {tag.color};">
                    <p>{tag.name}</p>
                </button>
            {/if}
        {/each}
    </div>
</div>

<div>
    {#each blogs as blog}
        {#if tagsIncluded(blog, $selectedTags) || $selectedTags.length===0}
            <a href="{blog.path}">
                <div class="blogCard">
                    <div class="blogtextdiv">
                        <p>by {blog.author}</p>
                        <h5>{blog.title}</h5>
                        <p class="description">{blog.description}</p>

                        <div class="tagSection">
                            <div class="tagCenter">
                                {#each blog.tags as cardtag}
                                    {#if selected(cardtag.id, $selectedTags)}
                                        <button class="cardtag" on:click={() => setSelectedTags(cardtag)} style="background-color: {cardtag.color}; height: 3vw;"><p>{cardtag.name}</p></button>
                                    {:else}
                                        <button class="cardtag" on:click={() => setSelectedTags(cardtag)} style="background-color: {cardtag.color};"><p>{cardtag.name}</p></button>
                                    {/if}
                                {/each}
                            </div>
                        </div>

                        <div id="bottom">
                            <div class="blogdate"><p>{blog.date} &nbsp;</p></div>
                            <div class="readtime"><p>{blog.readtime} min read</p></div>
                        </div>
                    </div>

                    <div class="thumbnaildiv">
                        <img class="thumbnail" src={blog.thumbnail} alt="Blog thumbnail">
                    </div>
                </div>
            </a>
        {/if}
    {/each}
</div>

<style>
    .tagSection{
        height: 3vw;
        position: relative;
    }

    .tagCenter{
        position: absolute;
        top: 50%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
    }

    .tag{
        border: none;
        border-radius: 0.5vw;
        color: var(--grack_dark); 
        margin-right: 0.5vw;
        margin-top: 0.5vw;
        margin-bottom: 0.5vw;
    }

    .tag:hover{
        height: 3vw;
    }

    .cardtag{
        border: none;
        border-radius: 0.5vw;
        color: var(--grack_dark); 
        margin-right: 0.5vw;
        margin-top: 0.5vw;
        margin-bottom: 0.5vw;
    }

    /* for the blog card */
    .blogCard{
        background-color: var(--grack_dark);
        color: var(--offwhite_gentle);
        border-radius: 1.5vw;
        padding: 1.5vw 1.5vw 1.5vw 2.5vw;
        margin-top: 3vh;
        margin-bottom: 3vh;
        display: flex;
        position: relative;
    }

    .blogCard:hover{
        opacity: 0.95;
    }

    .blogtextdiv{
        flex: 1;
        padding-right: 1vw;
    }

    .thumbnaildiv{
        flex: 0.8;
    }

    .thumbnail{
        width: 100%;
        border-radius: 1vw;
    }

    .blogdate{
        float: left;
    }

    .readtime{
        float: right;
    }

    .description{
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2; /* number of lines to show */
        line-clamp: 2; 
        -webkit-box-orient: vertical;
    }

    /* div for publish date and read time */
    #bottom{
        position: absolute;
        bottom: 2.5vh;
        width: 45%;
    }

    @media screen and (max-width:64em){
        .blogCard{
            height:32.5vh;
        }
    }

    @media screen and (max-width:35.5625em){
        .tag{
            border-radius:1vw;


        }
        .tagSection{
            margin-top:3vw;
        }
        .cardtag{
            border-radius:1vw;


        }
        h5{
            font-size:6vw;
        }
        .description{
            font-size:3vw;
        }
        p{
            font-size:2vw;
        }
        .blogCard{
            height:50vw;
        }
    }
</style>