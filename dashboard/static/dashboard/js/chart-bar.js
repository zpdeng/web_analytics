// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["2", "3", "4", "5", "6", "7+"],
    datasets: [{
      label: "Pages Viewed",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [68, 29, 25, 10, 5, 3],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'visits'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 100,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: true
    }
  }
});