
async function doThing() {
    const resp = await fetch("/do-thing", {
        method: "GET",
    });

    let data = resp.json();
    console.log(data);
}
