(function() {
    //set up svg and boundaries
    var width = 500,
        height = 500;

    var svg = d3.select("#chart")
        .append("svg")
        .attr("height", height)
        .attr("width", width)
        .append("g")
        .attr("transform", "translate(0,0)")

    //add radius scale to make size dependant on count
    var radiusScale = d3.radiusScale().domain([1,100]).range([10, 80])

    //add force to make bubbles go twords the center and not collide
    var simulation = d3.forceSimulation()
        .force("xForce", d3.forceX(width / 2).strength(0.05))
        .force("yForce", d3.forceY(height / 2).strength(0.05))
        .force("collide", d3.forceCollide(function(d) {
            return radiusScale(d.etyCount)
        }))

    //load data from csv
    d3.queue()
        .defer(d3.csv ,"file.csv")
        .await(ready)

    //append circles
    function ready (error, datapoints) {

        var circles = svg.selectAll(".region")
            .data(datapoints)
            .enter().append("circle")
            .attr("class", "region")
            .attr("r", function(d) {
                return radiusScale(d.etyCount)
            })
            .attr("fill", "lightblue")
            .on('click', function(d) {
                console.log(d)
            })

        //update circles based on force
        simulation.nodes(datapoints)
            .on('tick', ticked)

        function ticked() {
            circles
                .attr("cx", function(d) {
                    return d.x
                })
                .attr("cy", function(d) {
                    return d.y
                })
        }

}

})();
