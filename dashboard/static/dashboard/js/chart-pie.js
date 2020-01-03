var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["USA", "CDN", "CHN", "FRA", "GER"],
    datasets: [{
      data: [20, 12, 4, 7, 9],
      backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745'],
    }],
  },
});