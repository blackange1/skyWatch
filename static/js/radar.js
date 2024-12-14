console.log("start radar")
const $svg = document.querySelector('svg')
if ($svg) {
    console.log($svg)
    // repeat each two second
    const updateRadar = () => {
        fetch(`/api/radar/${window.location.pathname.split('/')[2]}`)
            .then(response => response.json())
            .then((data) => {
                const status = data['status']
                console.log("|--------")
                console.log("|--status", status)
                console.log("|--data", data)

                if (status === "ok") {
                    $svg.innerHTML = ""
                    const coordinates = data["coordinates"]
                    const count = coordinates.length
                    let index = 0
                    const startRadius = 10.5 - (0.5 * count)
                    const startOpacity = 1.1 - (0.1 * count)
                    for (const coordinate of coordinates) {
                        const $circle = document.createElementNS("http://www.w3.org/2000/svg", "circle")
                        $circle.setAttribute("cx", coordinate['x'])
                        $circle.setAttribute("cy", coordinate['y'])
                        $circle.setAttribute("r", String(startRadius + (0.5 * index)))
                        $circle.setAttribute("stroke", "green")
                        $circle.setAttribute("stroke-width", "1")
                        $circle.setAttribute("fill", "grey")
                        $circle.setAttribute("opacity", String(startOpacity + (0.1 * index)))
                        $svg.appendChild($circle)
                        index++
                    }
                    // change attribute last circle
                    const $lastCircle = $svg.lastElementChild
                    if ($lastCircle) {
                        $lastCircle.setAttribute("fill", "red")
                        $lastCircle.setAttribute("stroke-width", "3")
                    }
                }
            })
            .catch(e => console.error(e))
    }
    updateRadar()
    setInterval(updateRadar, 2000)
}