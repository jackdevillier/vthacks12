const statebuttons = document.getElementsByClassName("state-button");

for (let i = 0; i < statebuttons.length; i++) {
    statebuttons[i].addEventListener("click", () => {
        alert(`clicked ${statebuttons[i].attributes}`)
    })
}
