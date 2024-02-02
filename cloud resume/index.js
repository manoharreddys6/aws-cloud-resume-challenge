const counter = document.querySelector(".counter-number");

async function updateCounter() {
    try {
        let response = await fetch("https://a5hnljvnqh5hizotjblf6kcjku0kxndm.lambda-url.ap-south-1.on.aws/");
        let data = await response.json();

        console.log("Response:", data); // Add this line for debugging

        counter.innerHTML = ` Views: ${data.views}`;
    } catch (error) {
        console.error("Error fetching views:", error);
        counter.innerHTML = "Couldn't read views";
    }
}

updateCounter();
