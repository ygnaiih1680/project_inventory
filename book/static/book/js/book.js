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

function fillData(isbn) {
    const bookInfo = {
        title: document.getElementById(`${isbn}-title`).textContent,
        contents: document.getElementById(`${isbn}-contents`).textContent,
        thumbnail: document.getElementById(`${isbn}-thumbnail`).getAttribute("src"),
        url: document.getElementById(`${isbn}-url`).getAttribute("href"),
        authors: document.getElementById(`${isbn}-authors`).textContent.trim().substring(5)
    }
    const container = document.getElementById(`${isbn}`)
    for (const data of container.children) {
        const key = data.getAttribute("name")
        if (key !== "isbn") data.value = bookInfo[key]
    }
    
    return true
}