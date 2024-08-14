<script lang="ts">
    import Latestblog from '$lib/components/reusable/latestblog.svelte'
    import Blogposts from '$lib/components/reusable/blogposts.svelte'

    interface Blog{
        id: number
        path: string
        title: string
        description: string
        author: string
        date: string
        tags: Tag[]
        readtime: number
        thumbnail: string
    }

    interface Tag{
        id: number
        name: string
        color: string
    }

    const tags: Tag[] = [
        {
            id: 1,
            name: "Chianli",
            color: "rgb(252, 232, 225)"
        },
        {
            id: 2,
            name: "Alex",
            color: "rgb(246, 211, 222)"
        },
        {
            id: 3,
            name: "Zack",
            color: "rgb(205, 176, 218)"
        },
        {
            id: 4,
            name: "Website",
            color: "rgb(178, 220, 243)"
        },
        {
            id: 5,
            name: "CNC",
            color: "rgb(206, 242, 225)"
        },
        {
            id: 6,
            name: "Machinist",
            color: "rgb(255, 251, 214)"
        },
        {
            id: 7,
            name: "Carpenter",
            color: "rgb(252, 232, 225)"
        }
    ]

    const blogs: Blog[] = [
        {
            id: 1,
            path: "/aboutus/blog/1",
            title: "Hi, I'm Chianli",
            description: "A rundown of who I am and my role in the company.",
            author: "Chianli Hang",
            date: "Apr 25 2022",
            tags: [tags[0], tags[3]],
            readtime: 5,
            thumbnail: "/img/blog/1/1thumbnail.jpg"
        },
        {
            id: 2,
            path: "/aboutus/blog/2",
            title: "How I Got Here",
            description: "The tantilizing lore of Zachariah Clark.",
            author: "Zachariah Clark",
            date: "Jun 04 2022",
            tags: [tags[2]],
            readtime: 7,
            thumbnail: "/img/blog/2/2thumbnail.jpg"
        },
        {
            id: 3,
            path: "/aboutus/blog/3",
            title: "Intro to Alex",
            description: "The winding road of how I got here.",
            author: "Alex Sanducu",
            date: "Jun 07 2022",
            tags: [tags[1], tags[4], tags[5], tags[6]],
            readtime: 16,
            thumbnail: "/img/blog/3/thumbnail.jpg"
        }
    ]
</script>

<svelte:head>
  <title>our blog</title>
  <meta name="description" content= "Read about making, using, all things CNC and get a glimpse inside our company.">
</svelte:head>

<div class="main mainPadding">
    <h5 class="centerText">Latest</h5>
    <Latestblog blogs='{blogs}'/>

    <br>

    <div class="row">
        <div class="col1">
            <h4 id="about">who<br>we&nbsp;<br>are</h4>
        </div>

        <div class="col2">
            <img id="founders1year" src="/img/founders1year2.jpg" alt="founders at 1 year anniversay party">
        </div>
    </div>

    <br>

    <p class="centerText">
        THE CNC COMPANY is an ad-hoc business spawned from 3 Rutgers rocket scientists, Alex, Chianli, and Zack. Approaching the last years of university, the founders' <a href="https://www.rutgersrpl.com/">Rutgers Rocket Propulsion Lab [RRPL]</a>
        was flying higher than ever but plagued by an annoying problem. Rocket component manufacturing had to be outsourced, causing delays, headache, and inflexibility. Buying a CNC to make parts in-house was impossible with prices hitting 5
        figures. Cheap ones were deceptive, often selling an incomplete machine or a shoddy one. So we set out to engineer quality machines anyone could own supported by expert content for your machining experience to be nothing like ours.
    </p>

    <br>

    <h5>Posts</h5>
    <Blogposts tags='{tags}' blogs='{blogs}'/>
</div>

<style>
    .centerText{
        text-align: center;
    }

    .row{
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        width: 100%;
    }

    .col1{
        display: flex;
        flex-direction: column;
        flex-basis: 100%;
        flex: 0.4;
    }

    .col2{
        display: flex;
        flex-direction: column;
        flex-basis: 100%;
        flex: 1.6;
    }

    #founders1year{
        width: 100%;
        border-radius: 2.5vw;
        display: block;
        margin-top: auto;
        margin-bottom: auto;
    }

    #about{
        display: block;
        margin-top: auto;
        margin-bottom: auto;
        text-align: center;
        margin-left: -3vw;
    }

    @media screen and (max-width:35.5625em){
        h5{
            font-size:10vw;
        }
    }
</style>