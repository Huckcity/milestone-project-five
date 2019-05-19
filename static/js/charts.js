
//
// Credit to Stackoverflow for ChartJS overwrite to incorporate text in the center
// of a pie chart. See https://stackoverflow.com/questions/20966817/how-to-add-text-inside-the-doughnut-chart-using-chart-js
//
Chart.pluginService.register({
  beforeDraw: function (chart) {
    if (chart.config.options.elements.center) {
      //Get ctx from string
      var ctx = chart.chart.ctx;
      
      //Get options from the center object in options
      var centerConfig = chart.config.options.elements.center;
      var fontStyle = centerConfig.fontStyle || 'Arial';
      var txt = centerConfig.text;
      var color = centerConfig.color || '#000';
      var sidePadding = centerConfig.sidePadding || 20;
      var sidePaddingCalculated = (sidePadding/100) * (chart.innerRadius * 2)
      //Start with a base font of 30px
      ctx.font = "40px " + fontStyle;
      
      //Get the width of the string and also the width of the element minus 10 to give it 5px side padding
      var stringWidth = ctx.measureText(txt).width;
      var elementWidth = (chart.innerRadius * 2) - sidePaddingCalculated;

      // Find out how much the font can grow in width.
      var widthRatio = elementWidth / stringWidth;
      var newFontSize = Math.floor(30 * widthRatio);
      var elementHeight = (chart.innerRadius * 2);

      // Pick a new font size so it will not be larger than the height of label.
      var fontSizeToUse = Math.min(newFontSize, elementHeight);

      //Set font settings to draw it correctly.
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      var centerX = ((chart.chartArea.left + chart.chartArea.right) / 2);
      var centerY = ((chart.chartArea.top + chart.chartArea.bottom) / 2);
      ctx.font = fontSizeToUse+"px " + fontStyle;
      ctx.fillStyle = color;
      
      //Draw text in center
      ctx.fillText(txt, centerX, centerY);
    }
  }
});
//
// END OVERWRITE
//


//date format options
var options = { year: 'numeric', month: 'long', day: 'numeric' };

function getData(tickets_data_url) {
  fetch(tickets_data_url)
    .then(response => {
      return response.json();
    })
    .then(data => {
      // Work with JSON data here
      const chart_data = data;
      let labels = [];
      let values = [];

      for (let i = 0; i < chart_data.length; i++) {

        date = new Date(chart_data[i].day).toLocaleString('en-GB', options);
        labels.push(date);
        values.push(chart_data[i].count_items);
      }

      var by_day = document.getElementById("tickets-by-day");

      var chart_months = new Chart(by_day, {
        type: "bar",
        data: {
          labels: labels,
          datasets: [
            {
              label: "Tickets Logged",
              data: values,
              backgroundColor: "#233237",
              hoverBackgroundColor : "#18121e",
            }
          ]
        },
        options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true
                }
              }
            ]
          }
        }
      });
    })
    .catch(err => {
      // Do something for an error here
      span = document.getElementById("error1");
      txt = document.createTextNode("There was an error retrieving the dataset");
      span.appendChild(txt);
    });
}

function getTicketTypeData(type_data_url) {
  fetch(type_data_url)
    .then(response => {
      return response.json();
    })
    .then(data => {

      var bugs_vs_features = document.getElementById("bugs-vs-features");
      const avg = Math.round(data)
      const labels = ["Bugs", "Features"]
      const values = [data[0].count, data[1].count]

      var chart_days = new Chart(bugs_vs_features, {
        type: "doughnut",
        data: {
          labels: labels,
          datasets: [
            {
              label: "Bugs vs Features Totals",
              data: values,
              backgroundColor: ["#984b43", "#233237"]
            }
          ]
        },
        options: {
          responsive: true,
          legend: {
            position: 'top',
          },
          animation: {
            animateScale: true,
            animateRotate: true
          }
        }
      });
    })
    .catch(err => {
      // Do something for an error here
      span = document.getElementById("error2");
      txt = document.createTextNode("There was an error retrieving the dataset");
      span.appendChild(txt);
    });
}

function featureProgress(average_feature_progress) {
  fetch(average_feature_progress)
    .then(response => {
      return response.json();
    })
    .then(data => {
      
      const avg = Math.round(data)
      const labels = ["Average Progress", "Remaining"]
      const values = [avg, 100-avg]

      var bugs_vs_features = document.getElementById("feature-progress");
      var chart_days = new Chart(bugs_vs_features, {
        type: "doughnut",
        data: {
          labels: labels,
          datasets: [
            {
              label: "Bugs vs Features Totals",
              data: values,
              backgroundColor: ["#984b43", "#233237"]
            }
          ]
        },
        options: {
          responsive: true,
          legend: {
            position: 'top',
          },
          animation: {
            animateScale: true,
            animateRotate: true
          },
          elements: {
            center: {
              text: avg+'%',
              sidePadding: 10
            }
          }
        }
      });
    })
    .catch(err => {
      // Do something for an error here
      span = document.getElementById("error3");
      txt = document.createTextNode("There was an error retrieving the dataset");
      span.appendChild(txt);
    });
}

function commentData(get_comment_data) {
  fetch(get_comment_data)
    .then(response => {
      return response.json();
    })
    .then(data => {
      
      const chart_data = data;
      let labels = [];
      let values = [];

      for (let i = 0; i < chart_data.length; i++) {

        date = new Date(chart_data[i].day).toLocaleString('en-GB', options);
        labels.push(date);
        values.push(chart_data[i].count_items);
      }

      var by_day = document.getElementById("comments-per-day");

      var chart_months = new Chart(by_day, {
        type: "line",
        data: {
          labels: labels,
          datasets: [
            {
              label: "Comments Activity Monitor",
              data: values,
              borderColor: "#984b43",
              borderWidth: 3,
              fill: false,
            }
          ]
        },
        options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true
                }
              }
            ]
          }
        }
      });
    })
    .catch(err => {
      // Do something for an error here
      span = document.getElementById("error4");
      txt = document.createTextNode("There was an error retrieving the dataset");
      span.appendChild(txt);
    });
}


function ticketStatus(get_comment_data) {
  fetch(get_comment_data)
    .then(response => {
      return response.json();
    })
    .then(data => {

      var ticket_status = document.getElementById('ticket-status');
      var chart_status = new Chart(ticket_status, {
        type: 'pie',
        data: {
          labels: ["Pending", "In Progress", "Complete"],
          datasets: [{
            data: data,
            backgroundColor: [
              '#233237',
              '#984b43',
              '#eac67a',
            ]
          }]
        }
      });

      
    })
    .catch(err => {
      // Do something for an error here
      span = document.getElementById("error5");
      txt = document.createTextNode("There was an error retrieving the dataset");
      span.appendChild(txt);
    });
}
