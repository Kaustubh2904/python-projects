// script.js
const volumeLevel = document.getElementById("volume-level");

// Function to update the volume bar color based on system volume
function updateVolumeColor(volume) {
    const volumePercentage = (volume / 100) * 100;
    volumeLevel.style.height = `${volumePercentage}%`;

    // Calculate the color based on the volume percentage
    const redValue = Math.min(255, Math.floor(volumePercentage * 2.55));
    const greenValue = Math.min(255, Math.floor((100 - volumePercentage) * 2.55));
    const blueValue = 0;

    const color = `rgb(${redValue}, ${greenValue}, ${blueValue})`;
    volumeLevel.style.backgroundColor = color;
}

// Simulate changing the system volume (you would replace this with actual volume events)
let currentVolume = 50; // Initial volume
updateVolumeColor(currentVolume);

// Example: Change the volume and update the bar color
document.addEventListener("keydown", (event) => {
    if (event.key === "ArrowUp" && currentVolume < 100) {
        currentVolume += 10;
        updateVolumeColor(currentVolume);
    } else if (event.key === "ArrowDown" && currentVolume > 0) {
        currentVolume -= 10;
        updateVolumeColor(currentVolume);
    }
});
