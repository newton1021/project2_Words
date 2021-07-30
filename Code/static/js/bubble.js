
function makeBubble(datapoints) {
    
    
    //set up svg and boundaries
    var width = 500;
    var height = 400;
    
    
    
    
    var svg = d3.select("#chart")
        .append("svg")
        .attr("height", height)
        .attr("width", width)
        .append("g")
        .attr("transform", "translate(10,10)");
    
    var colorScale = d3.scaleLinear()
        .domain([1,10])
        .range([d3.rgb("white"), d3.rgb("blue")])

    
    //add radius scale to make size dependant on count
    var radiusScale = d3.scaleSqrt()
        .domain([1,30])
        .range([10, 80])
    
    //add force to make bubbles go twords the center and not collide
    var simulation = d3.forceSimulation()
    .force("xForce", d3.forceX(width / 2).strength(0.05))
    .force("yForce", d3.forceY(height / 2).strength(0.05))
    .force("collide", d3.forceCollide(function(d) {
        return radiusScale(d[1])
    }))
    

    
       
    var circles = svg.selectAll(".region")
    .data(datapoints)
    .enter().append("circle")
    .attr("class","region")
    .attr("r", function(d) {
        return radiusScale(d[1])
    })
    
    .attr("fill",function(d) {
        return colorScale(d[1])    
    })
    
    
    .on('click', function(d) {
        console.log(d[0])
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
