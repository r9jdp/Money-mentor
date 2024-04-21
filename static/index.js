google.charts.load("current", { packages: ["corechart"] });
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
  var data = google.visualization.arrayToDataTable([
    ["Task", "Hours per Day"],
    ["Pay EMI for car", 1200],
    ["Pay for children school fees", 4000],
    ["Add 10% of salary for savings", 5000],
    ["Set aside money for groceries and other household expenses", 15000],
    ["Allocate money for entertainment and personal expenses", 5000],
    ["Allocate money for unexpected expenses", 3000],
  ]);

  var options = {
    title: "My Daily Activities",
    is3D: true,
  };

  var chart = new google.visualization.PieChart(
    document.getElementById("piechart_3d")
  );
  chart.draw(data, options);
}