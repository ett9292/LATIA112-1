let myGraph = document.getElementById('myGraph');
let myGraph2 = document.getElementById('myGraph2');
let myGraph3 = document.getElementById('myGraph3');

function unpack(rows, key){
    return rows.map(function(row){
        return row[key];
    });
}

let trace1 ={};
trace1.type ="bar";
trace1.title ="偏鄉學校類別統計數量";
trace1.x = [];
trace1.y = [];
trace1.labels =[];
trace1.values =[];
trace1.hole =0.5;
trace1.domain ={
    row:3,
    column:0
};

for (let i=0; i<type_count.length; i++){
    trace1.x[i] = type_count[i]['type'];
    trace1.y[i] = type_count[i]['count'];
}

let trace2 ={};
trace2.type ="pie";
trace2.title ="原住民學生比例";
trace2.labels =[];
trace2.values =[];
trace2.hole =0.5;
trace2.domain ={
    row:0,
    column:1
};

for(let x=0; x<type_count.length; x++){
    trace2.labels[x] =type_count[x]['type'];
    trace2.values[x] =type_count[x]['Indigenous'];
}


let trace3 = {};
trace3.type = "scattermapbox";
trace3.title = "六都偏鄉學校數";
trace3.labels =[];
trace3.values =[];
trace3.text = [];
trace3.lat = unpack(city_location, "lat");
trace3.lon = unpack(city_location, "lon");
trace3.marker = {
    color:'blue',
    size:[]
};

for(let i=0;i<city_location.length;i++){
    trace3.text[i] = 0;
}

for (let i = 0; i < city_location.length; i++) {
    trace3.marker.size[i] = city_count[i]['count'];
}

console.log(trace3.text);


let data = [];
data.push(trace1);

let data2 = [];
data2.push(trace2);

let data3 = [];
data3.push(trace3);

let layout = {
    title : "偏鄉學校類別統計數量",
    margin:{
        t:50,
        l:50
    },
    annotations: [
        {
            text: "台灣偏鄉學校的地區屬性(偏鄉程度)中，「偏遠」為最多<br>其次為「特偏」，最少為「極偏」，且偏鄉程度特偏以上數量明顯較少",
            showarrow: false,
            x: 0.5,  
            y: -0.12, 
            xref: 'paper',
            yref: 'paper',
            xanchor: 'center',
            yanchor: 'top',
            font: {
                size: 14,
                color: 'black'  
            }
        }
    ]
};

let layout2 = {
    title : "原住民學生比例",
    margin: {
        t: 50,
        l: 80
    },
    annotations: [
        {
            text: "數值說明：偏鄉學校中所有原住民學生數，以地區屬性(偏鄉/特偏/極偏)分別計算<br>結果觀察：原住民學生分佈於「極偏」學校的比例相當高，佔55.3%，<br>其次有34.1%就讀「特偏」學校，僅10%就讀「偏遠」學校",
            showarrow: false,
            x: 0.53,  
            y: -0.05, 
            xref: 'paper',
            yref: 'paper',
            xanchor: 'center',
            yanchor: 'top',
            font: {
                size: 14,
                color: 'black'  
            }
        }
    ]
};

let layout3 = {
    title : "六都偏鄉學校數",
    margin: {
        t: 50,
        l: 60
    },
    dragmode:"zoom",
    mapbox:{
        style:"open-street-map",
        center:{
            lat: 23.708167, 
            lon: 120.929999
        },
        zoom:5.5
    },
    annotations: [
        {
            text: "數值說明：台北0所，新北58所，桃園30所，台中48所，台南103所，高雄72所<br>台灣六都中，台南市所在偏鄉學校最多，台北市則完全沒有",
            showarrow: false,
            x: 0.53,  
            y: -0.05, 
            xref: 'paper',
            yref: 'paper',
            xanchor: 'center',
            yanchor: 'top',
            font: {
                size: 14,
                color: 'black'  
            }
        }
    ]
};


Plotly.newPlot(myGraph, data, layout);
Plotly.newPlot(myGraph2, data2, layout2);
Plotly.newPlot(myGraph3, data3, layout3);
    
