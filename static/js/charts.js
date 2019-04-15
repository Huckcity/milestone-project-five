function getData(tickets_data_url) {
  var margin = { top: 20, right: 20, bottom: 30, left: 50 },
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

  var parseDate = d3.time.format("%Y-%m-%d").parse; // for dates like "2014-01-01"
  //var parseDate = d3.time.format("%Y-%m-%dT00:00:00Z").parse;  // for dates like "2014-01-01T00:00:00Z"

  var x = d3.time.scale().range([0, width]);

  var y = d3.scale.linear().range([height, 0]);

  var xAxis = d3.svg
    .axis()
    .scale(x)
    .orient("bottom");

  var yAxis = d3.svg
    .axis()
    .scale(y)
    .orient("left");

  var line = d3.svg
    .line()
    .x(function(d) {
      return x(d.month);
    })
    .y(function(d) {
      return y(d.count_items);
    });

  var svg = d3
    .select("#chart")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  d3.json(tickets_data_url, function(error, data) {
    data.forEach(function(d) {
      d.month = parseDate(d.day);
      d.count_items = +d.count_items;
    });

    x.domain(
      d3.extent(data, function(d) {
        return d.month;
      })
    );
    y.domain(
      d3.extent(data, function(d) {
        return d.count_items;
      })
    );

    svg
      .append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

    svg
      .append("g")
      .attr("class", "y axis")
      .call(yAxis)
      .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Number of tickets");

    svg
      .append("path")
      .datum(data)
      .attr("class", "line")
      .attr("d", line);
  });
}

function getTicketTypeData(type_data_url) {
  // set the dimensions of the canvas
  var margin = { top: 20, right: 20, bottom: 70, left: 40 },
    width = 600 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;

  // set the ranges
  var x = d3.scale.ordinal().rangeRoundBands([0, width], 0.05);

  var y = d3.scale.linear().range([height, 0]);

  // define the axis
  var xAxis = d3.svg
    .axis()
    .scale(x)
    .orient("bottom");

  var yAxis = d3.svg
    .axis()
    .scale(y)
    .orient("left")
    .ticks(10);

  // add the SVG element
  var svg = d3
    .select("#test")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  // load the data
  d3.json(type_data_url, function(error, data) {
    data.forEach(function(d) {
      d.type = d.type;
      d.count = +d.count;
      console.log(d)
    });

    // scale the range of the data
    x.domain(
      data.map(function(d) {
        return d.type;
      })
    );
    y.domain([
      0,
      d3.max(data, function(d) {
        return d.count;
      })
    ]);

    // add axis
    svg
      .append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
      .selectAll("text")
      .style("text-anchor", "end")
      .attr("dx", "-.8em")
      .attr("dy", "-.55em")
      .attr("transform", "rotate(-90)");

    svg
      .append("g")
      .attr("class", "y axis")
      .call(yAxis)
      .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 5)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Frequency");

    // Add bar chart
    svg
      .selectAll("bar")
      .data(data)
      .enter()
      .append("rect")
      .attr("class", "bar")
      .attr("x", function(d) {
        return x(d.type);
      })
      .attr("width", x.rangeBand())
      .attr("y", function(d) {
        return y(d.count);
      })
      .attr("height", function(d) {
        return height - y(d.count);
      });
  });
}
