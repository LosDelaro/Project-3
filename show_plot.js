// make plot based on input
// show is either No Reservations, Parts Unknown, A Cook's Tour, or The Layover
function makePlot() {
  let shows = [275, 158, 42, 20];

  // Create an array of category labels
  let labels = ["No Reservations", "Parts Unknown", "A Cook's Tour", "The Layover"];
  
  // @ADD YOUR CODE HERE
  let trace = {
    values: shows,
    labels: labels,
    hole: .4,
    type: 'pie'
  };
  
  let data = [trace];
  
  let layout = {
    title: "Anthony Bourdain Shows"
  };
  
  Plotly.newPlot('pie', data, layout);
};

makePlot();