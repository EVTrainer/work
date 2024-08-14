export const post = async ({request}) => {
    const body = await request.formData();

    const name = body.get("name");
    const email = body.get("email");
    const phone = body.get("phone");
    const message = body.get("message");

    const res = await fetch(`https://docs.google.com/forms/d/e/1FAIpQLScxU6L9yRL-pyykAkxIvGeV-ymw1fNqIMNNaODcXrXt95i_-Q/formResponse?usp=pp_url&entry.890209095=${name}&entry.1508880283=${phone}&entry.1590162580=${email}&entry.1834937435=${message}&submit=Submit`);
}