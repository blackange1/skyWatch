console.log("start radar")
const $svg = document.querySelector('svg')
if ($svg) {
    console.log($svg)
    // repeat each two second
    const updateRadar = () => {
        fetch("/api/radar/poltava")
            .then(response => response.json())
            .then((data) => {
                const status = data['status']
                console.log("|--------")
                console.log("|--status", status)
                console.log("|--data", data)
                if (status === "ok") {
                    $svg.innerHTML = ""
                    for (const coordinate of data["coordinates"]) {
                        const $circle = document.createElementNS("http://www.w3.org/2000/svg", "circle")
                        $circle.setAttribute("cx", coordinate['x'])
                        $circle.setAttribute("cy", coordinate['y'])
                        $circle.setAttribute("r", "8")
                        $circle.setAttribute("stroke", "green")
                        $circle.setAttribute("stroke-width", "1")
                        $circle.setAttribute("fill", "grey")
                        $circle.setAttribute("opacity", "1")
                        $svg.appendChild($circle)
                    }
                }
            })
            .catch(e => console.error(e))
    }
    updateRadar()
    setInterval(updateRadar, 2000)
}