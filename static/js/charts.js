var margin = { top: 20, right: 30, bottom: 70, left: 30 },
  $container = $(".chart-container"),
  width = $container.width() - margin.left - margin.right,
  height = $container.height();

function getData(tickets_data_url) {
  var parseDate = d3.time.format("%Y-%m-%d").parse; // for dates like "2014-01-01"

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
    .select("#ticketsLogged")
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
    .select("#bugsVsRequests")
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
      console.log(d);
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

function featureProgress(average_feature_progress) {
  d3.json(average_feature_progress, function(error, data) {
    var color = "#17a2b8";

    var radius = 100;
    var border = 5;
    var padding = 30;
    var startPercent = 0;
    var endPercent = data / 100;

    var twoPi = Math.PI * 2;
    var formatPercent = d3.format(".0%");
    var boxSize = (radius + padding) * 2;

    var count = Math.abs((endPercent - startPercent) / 0.01);
    var step = endPercent < startPercent ? -0.01 : 0.01;

    var arc = d3.svg
      .arc()
      .startAngle(0)
      .innerRadius(radius)
      .outerRadius(radius - border);

    var parent = d3.select("div#featureProgress");

    var svg = parent
      .append("svg")
      .attr("width", boxSize)
      .attr("height", boxSize);

    var defs = svg.append("defs");

    var filter = defs.append("filter").attr("id", "blur");

    filter
      .append("feGaussianBlur")
      .attr("in", "SourceGraphic")
      .attr("stdDeviation", "7");

    var g = svg
      .append("g")
      .attr("transform", "translate(" + boxSize / 2 + "," + boxSize / 2 + ")");

    var meter = g.append("g").attr("class", "progress-meter");

    meter
      .append("path")
      .attr("class", "background")
      .attr("fill", "#ccc")
      .attr("fill-opacity", 0.7)
      .attr("d", arc.endAngle(twoPi));

    var foreground = meter
      .append("path")
      .attr("class", "foreground")
      .attr("fill", color)
      .attr("fill-opacity", 1)
      .attr("stroke", color)
      .attr("stroke-width", 5)
      .attr("stroke-opacity", 1)
      .attr("filter", "url(#blur)");

    var front = meter
      .append("path")
      .attr("class", "foreground")
      .attr("fill", color)
      .attr("fill-opacity", 1);

    var numberText = meter
      .append("text")
      .attr("fill", "#000")
      .attr("text-anchor", "middle")
      .attr("dy", ".85em");

    function updateProgress(progress) {
      foreground.attr("d", arc.endAngle(twoPi * progress));
      front.attr("d", arc.endAngle(twoPi * progress));
      numberText.text(formatPercent(progress));
    }

    var progress = startPercent;

    (function loops() {
      updateProgress(progress);

      if (count > 0) {
        count--;
        progress += step;
        setTimeout(loops, 10);
      }
    })();
  });
}

function commentData(get_comment_data) {
  var parseDate = d3.time.format("%Y-%m-%d").parse; // for dates like "2014-01-01"

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
    .select("#commentsPerDay")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  d3.json(get_comment_data, function(error, data) {
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
