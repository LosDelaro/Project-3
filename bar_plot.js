// make plot based on input
// show is either No Reservations, Parts Unknown, A Cook's Tour, or The Layover
function makePlot() {
  let visits = [159, 94, 94, 42, 32, 32, 24, 14, 4];

  // Create an array of category labels
  let labels = ["North America", "Asia", "Europe", "South America", "Africa", "Central America", "Middle East", "Oceania", "Antaractica"];
  
  // @ADD YOUR CODE HERE
  let trace = {
    x: labels,
    y: visits,
    type: 'bar',
    marker: {color: 'tropic'}
  };
  
  let data = [trace];
  
  let layout = {
    title: "Anthony Bourdain Visits"
  };
  
  Plotly.newPlot('bar', data, layout);
};

makePlot();