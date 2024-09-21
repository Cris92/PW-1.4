function toggleTags(element) {
    const hiddenTags = element.nextElementSibling;
    if (hiddenTags.style.display === "none" || hiddenTags.style.display === "") {
        hiddenTags.style.display = "block";
        element.innerText = "-";
    } else {
        hiddenTags.style.display = "none";
        const extraTags = hiddenTags.children.length;
        element.innerText = `+${extraTags}`;
    }
}
