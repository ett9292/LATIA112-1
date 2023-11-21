let myGraph = document.getElementById('myGraph');
let trace1 = {};
trace1.type = "pie";
trace1.labels = [];
trace1.values = [];

for(let i=0 ; i<evaluation_ratio.length ; i++)
{
    trace1.labels[i] = evaluation_ratio[i]['name'];
    trace1.values[i] = evaluation_ratio[i]['count'];
}

let data = [];
data.push(trace1);

let layout = {
    margin:{
        t:30,
        l:50,
    }
    
};


Plotly.newPlot(myGraph, data, layout);

