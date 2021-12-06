'use strict';
$(document).ready(function() {
    setTimeout(function() {
    function getWeather(lat, lon) {
        fetch(`http://sami.works:8000/api/weather/`)
        .then(res => res.json())
        .then(data => {
            let tempArray = new Array();
            let rainArray = new Array();
            console.log(data);
            for(let i = 0; i <data.length; i++){
                let Item1 = new Object();
                let Item2 = new Object();
                Item1.temp = data[i].temp;
                Item1.fcstTime = data[i].fcstTime;
                Item2.fcstTime = data[i].fcstTime;
                Item2.rain = data[i].rain;
                tempArray.push(Item1);
                rainArray.push(Item2);
                console.log(tempArray);
            }

             Morris.Line({
                element: 'morris-line-chart',
                data: tempArray,
                xkey: 'fcstTime',
                redraw: true,
                resize: true,
                smooth: false,
                ykeys: ['temp'],
                hideHover: 'auto',
                responsive:true,
                labels: ['예상기온'],
                lineColors: ['#1de9b6', '#04a9f5']
            });
            // [ area-angle-chart ] end

            // [ bar-stacked ] chart start
            Morris.Area({
                element: 'morris-bar-stacked-chart',
                data: rainArray,
                lineColors: ['#04a9f5'],
                xkey: 'fcstTime',
                ymax: 100,
                ykeys: ['rain'],
                labels: ['강수확률'],
                pointSize: 0,
                lineWidth: 0,
                resize: true,
                fillOpacity: 0.9,
                responsive:true,
                behaveLikeLine: true,
                hideHover: 'auto'
            });
            // [ bar-stacked ] chart end
        })
    }
    getWeather();
    // [ area-angle-chart ] start
    Morris.Area({
        element: 'morris-area-chart',
        data: [
            {
                y: '2016',
                a: 130,
                b: 100
            },
            {
                y: '2017',
                a: 80,
                b: 60
            },
            {
                y: '2018',
                a: 70,
                b: 200
            },
            {
                y: '2019',
                a: 220,
                b: 150
            },
            {
                y: '2020',
                a: 105,
                b: 90
            },
            {
                y: '2021',
                a: 250,
                b: 150
            }
        ],
        xkey: 'y',
        ykeys: ['a', 'b'],
        labels: ['Series A', 'Series B'],
        pointSize: 0,
        fillOpacity: 0.8,
        pointStrokeColors: ['#b4becb', '#A389D4'],
        behaveLikeLine: true,
        gridLineColor: '#e0e0e0',
        lineWidth: 0,
        smooth: false,
        hideHover: 'auto',
        responsive:true,
        lineColors: ['#b4becb', '#A389D4'],
        resize: true
    });
    // [ area-angle-chart ] end

    // [ area-smooth-chart ] start
    Morris.Area({
        element: 'morris-area-curved-chart',
        data: [{
            period: '2016',
            iphone: 50,
            ipad: 15,
            itouch: 5
        }, {
            period: '2017',
            iphone: 20,
            ipad: 50,
            itouch: 65
        }, {
            period: '2018',
            iphone: 60,
            ipad: 12,
            itouch: 7
        }, {
            period: '2019',
            iphone: 30,
            ipad: 20,
            itouch: 120
        }, {
            period: '2020',
            iphone: 25,
            ipad: 80,
            itouch: 40
        }, {
            period: '2021',
            iphone: 10,
            ipad: 10,
            itouch: 10
        }],
        lineColors: ['#A389D4', '#1de9b6', '#04a9f5'],
        xkey: 'period',
        ykeys: ['iphone', 'ipad', 'itouch'],
        labels: ['Site A', 'Site B', 'Site C'],
        pointSize: 0,
        lineWidth: 0,
        resize: true,
        fillOpacity: 0.9,
        responsive:true,
        behaveLikeLine: true,
        gridLineColor: '#d2d2d2',
        hideHover: 'auto'
    });
    // [ area-smooth-chart ] end

    // [ line-angle-chart ] Start
//    Morris.Line({
//        element: 'morris-line-chart',
//        data: [{
//                y: '2006',
//                a: 20,
//                b: 10
//            },
//            {
//                y: '2007',
//                a: 55,
//                b: 45
//            },
//            {
//                y: '2008',
//                a: 45,
//                b: 35
//            },
//            {
//                y: '2009',
//                a: 75,
//                b: 65
//            },
//            {
//                y: '2010',
//                a: 50,
//                b: 40
//            },
//            {
//                y: '2011',
//                a: 75,
//                b: 65
//            },
//            {
//                y: '2012',
//                a: 100,
//                b: 90
//            }
//        ],
//        xkey: 'y',
//        redraw: true,
//        resize: true,
//        smooth: false,
//        ykeys: ['a', 'b'],
//        hideHover: 'auto',
//        responsive:true,
//        labels: ['Series A', 'Series B'],
//        lineColors: ['#1de9b6', '#04a9f5']
//    });
    // [ line-angle-chart ] end
//// [ bar-stacked ] chart start
//            Morris.Bar({
//                element: 'morris-bar-stacked-chart',
//                data: rainArray,
//                xkey: 'fcstTime',
//////                stacked: true,
//                barSizeRatio: 0.8,
//                barGap: 5,
//                redraw: true,
//                resize: true,
//                responsive:true,
//                hideHover: 'auto',
//                ykeys: ['rain'],
//                labels: ['강수확률'],
//                barColors: ["0-#1de9b6-#1dc4e9", "0-#899FD4-#A389D4", "#04a9f5"]
//            });
//            // [ bar-stacked ] chart end
        }, 700);
});
