document.querySelector("#search-criteria-list").addEventListener("click", changeSearchCriteria)

function changeSearchCriteria(evt) {
    const display = document.querySelector("#criteria-display")
    const input = document.querySelector("#criteria-input")
    const target = evt.target
    if (target.classList.contains("dropdown-item")) {
        const {textContent} = target
        display.textContent = textContent
        input.placeholder = textContent + "(으)로 검색하기..."
        document.querySelector("input[name='criteria']").value = target.dataset.searchCriteria
    }
}

function fillData() {
    const bookInfo = {
        title: document.querySelector("#title").textContent,
        contents: document.querySelector("#contents").textContent,
        thumbnail: document.querySelector("#thumbnail").getAttribute("src"),
        url: document.querySelector("#url").getAttribute("href"),
        authors: document.querySelector("#authors").textContent.trim().substring(5)
    }
    const container = document.querySelector("#book-info-container")
    for (const data of container.children) {
        const key = data.getAttribute("name")
        if (key !== "isbn") data.value = bookInfo[key]
    }

    return true
}