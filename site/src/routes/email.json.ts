export const post = async ({request}) => {
    const body = await request.formData();

    const email = body.get("email");

    const res = await fetch(`https://docs.google.com/forms/d/e/1FAIpQLScxU6L9yRL-pyykAkxIvGeV-ymw1fNqIMNNaODcXrXt95i_-Q/formResponse?usp=pp_url&entry.890209095=${email}&entry.1508880283=${email}&entry.1590162580=${email}&entry.1834937435=${email}&submit=Submit`);
}
