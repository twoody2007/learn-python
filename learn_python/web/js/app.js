
async function doThing() {
    const resp = await fetch("/do-thing", {
        method: "GET",
    });

    let data = await resp.json();
    console.log(data);
}
