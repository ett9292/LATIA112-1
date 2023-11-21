let myGraph = document.getElementById('myGraph');

let trace1 = {};
trace1.mode ="markers";
trace1.type ="scatter";
trace1.name = "Team A";
trace1.marker = {
    size:10
};
trace1.x =[];
trace1.y =[];
trace1.text = [];

for(let i=0;i<set1.length;i++)
{
    trace1.x[i] =set1[i][0];
    trace1.y[i] =set1[i][1];
    trace1.text = [i] = set1[i][2];
}

let trace2 = {};
trace2.mode ="lines+markers";
trace2.type ="scatter";
trace2.x =[];
trace2.y =[];

for(let i=0;i<set2.length;i++)
{
    trace2.x[i] =set2[i][0];
    trace2.y[i] =set2[i][1];
}



let data =[];
data.push(trace1);
data.push(trace2);
let layout ={
    margin:{
        t:0
    }
};

Plotly.newPlot(myGraph, data, layout);