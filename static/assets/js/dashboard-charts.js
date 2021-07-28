$(function() {
    "use strict";
    // $(document).ready(loadCharts());


    // CO2 chart

    var options_co2 = {
        chart: {
            height: 125,
            type: 'area',
            zoom: {
                enabled: true
            },
            foreColor: 'rgba(255, 255, 255, 0.65)',
            toolbar: {
                show: true
            },
            sparkline: {
                enabled: true,
            },
            dropShadow: {
                enabled: false,
                opacity: 0.15,
                blur: 3,
                left: -7,
                top: 15,
                //color: 'rgba(0, 158, 253, 0.65)',
            }
        },
        plotOptions: {
            bar: {
                columnWidth: '10%',
                endingShape: 'rounded',
                dataLabels: {
                    position: 'top', // top, center, bottom
                },
            }
        },
        dataLabels: {
            enabled: false
        },
        stroke: {
            width: 3,
            curve: 'straight'
        },
        series: [{
            name: '',
            data: [] // use the array for displaying data from mysql or .net remove the hard number-->
        }],

        xaxis: {
            type: 'day',
            categories: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
        },
        yaxis: {
            axisBorder: {
                show: false
            },
            axisTicks: {
                show: false,
            },
            labels: {
                show: false,
                formatter: function(val) {
                    return parseFloat(val);
                }
            }

        },
        fill: {
            type: 'gradient',
            gradient: {
                shade: 'light',
                //gradientToColors: ['rgba(255, 255, 255, 0.12)'],
                shadeIntensity: 1,
                type: 'vertical',
                opacityFrom: 0.7,
                opacityTo: 0.1,
                stops: [0, 100, 100, 100]
            },
        },
        colors: ["#fff"],
        legend: {
            show: 0,
            position: "top",
            horizontalAlign: "center",
            offsetX: -20,
            fontSize: "12px",
            markers: {
                radius: 50,
                width: 10,
                height: 10
            }
        },
        grid: {
            show: false,
            borderColor: 'rgba(66, 59, 116, 0.12)',
        },
        tooltip: {
            theme: 'dark',
            x: {
                show: false
            },

        }
    }

    var chart_co2 = new ApexCharts(
        document.querySelector("#co2-levels-graph"),
        options_co2
    );

    chart_co2.render();


    // Temperature chart

    var options_temp = {
        chart: {
            height: 270,
            type: 'radialBar',
        },
        plotOptions: {
            radialBar: {
                startAngle: -180,
                endAngle: 225,
                hollow: {
                    margin: 0,
                    size: '75',
                    background: 'transparent',
                    dropShadow: {
                        enabled: true,
                        top: -3,
                        left: 0,
                        blur: 4,
                        opacity: 0.35
                    }
                },
                track: {
                    background: 'rgba(255, 255, 255, 0.12)',
                    strokeWidth: '100%',
                    margin: 0, // margin is in pixels
                    dropShadow: {
                        enabled: true,
                        top: -3,
                        left: 0,
                        blur: 4,
                        opacity: 0.35
                    }
                },
                dataLabels: {
                    name: {
                        fontSize: '14px',
                        color: '#fff',
                        offsetY: -10
                    },
                    value: {
                        offsetY: 0,
                        fontSize: '22px',
                        color: '#fff',
                        formatter: function(val) {
                            return val + "";
                        }
                    }
                },


            },
        },
        stroke: {
            dashArray: 4
        },
        fill: {
            type: 'gradient',
            gradient: {
                shade: 'dark',
                type: 'horizontal',
                shadeIntensity: 0.15,
                gradientToColors: ['#fff'],
                inverseColors: false,
                opacityFrom: 1,
                opacityTo: 1,
                stops: [0, 50, 65, 91]
            }
        },
        colors: ["#fff"],
        series: [],
        labels: ['In Degrees '],

    }
    var temp_chart = new ApexCharts(
        document.querySelector("#total-visitors"),
        options_temp
    );

    temp_chart.render();

    // Temperature day  chart homepage

    var options = {
        chart: {

            height: 200,
            type: 'area',
            zoom: {
                autoScaleYaxis: true
            },
            zoom: {
                enabled: true
            },
            foreColor: 'rgba(255, 255, 255, 0.65)',
            toolbar: {
                show: true
            },
            sparkline: {
                enabled: false,
            },
            dropShadow: {
                enabled: false,
                opacity: 0.15,
                blur: 3,
                left: -7,
                top: 15,
                //color: 'rgba(0, 158, 253, 0.65)',
            }
        },
        dataLabels: {
            enabled: false,
            style: {
                colors: ['#333']
            },
            offsetX: 30
        },
        plotOptions: {
            bar: {
                columnWidth: '10%',
                endingShape: 'rounded',
                dataLabels: {
                    position: 'top', // top, center, bottom
                },
            }
        },
        dataLabels: {
            enabled: true,
            background: {
                enabled: false
            },
            textAnchor: 'middle',
            offsetY: -5,
        },
        stroke: {
            width: 3,
            curve: 'smooth'
        },
        series: [{
            name: '',
            data: []
        }],



        xaxis: {
            type: 'datetime',
            categories: [],
            showDuplicates: false,
            labels: {
                show: true,
            },

        },
        yaxis: {
            showDuplicates: false,
            axisBorder: {
                show: false
            },
            axisTicks: {
                show: true,
            },
            labels: {
                show: true,
                formatter: function(val) {
                    return parseFloat(val).toFixed(2);
                }
            },
            tooltip: {
                enabled: true,
                offsetX: 0,
            },

        },

        fill: {
            type: 'gradient',
            gradient: {
                shade: 'light',
                gradientToColors: ['#fff'],
                shadeIntensity: 1,
                type: 'vertical',
                opacityFrom: 0.8,
                opacityTo: 0.2,
                stops: [0, 100, 100, 100]
            },
        },
        colors: ['#fff'],
        grid: {
            show: true,
            borderColor: 'rgba(255, 255, 255, 0.12)',
        },
        tooltip: {
            theme: 'dark',
            x: {
                show: true,
                format: 'HH:mm',
                // formatter: function(val) {

                //     var date = new Date(val * 1000)
                //     return "Time: " + "0" + date.getHours() + ":" + date.getMinutes();
                // }
            },

        },
        title: {
            text: 'Temperature Change Today'
        }
    }

    var tempHumChart = new ApexCharts(
        document.querySelector("#temp-hum"),
        options
    );

    tempHumChart.render();

    var optionsHum = {
        chart: {
            height: 200,
            type: 'area',
            zoom: {
                autoScaleYaxis: true
            },
            zoom: {
                enabled: true
            },
            foreColor: 'rgba(255, 255, 255, 0.65)',
            toolbar: {
                show: true
            },
            sparkline: {
                enabled: false,
            },
            dropShadow: {
                enabled: false,
                opacity: 0.15,
                blur: 3,
                left: -7,
                top: 15,
                //color: 'rgba(0, 158, 253, 0.65)',
            }
        },
        plotOptions: {
            bar: {
                columnWidth: '30%',
                endingShape: 'rounded',
                dataLabels: {
                    position: 'top', // top, center, bottom
                },
            }
        },
        dataLabels: {
            enabled: true,
            background: {
                enabled: false
            },
            textAnchor: 'middle',
            offsetY: -5,
        },
        stroke: {
            width: 3,
            curve: 'smooth'
        },
        series: [{
            name: '',
            data: []
        }],



        xaxis: {
            type: 'datetime',
            categories: [],

        },
        yaxis: {
            axisBorder: {
                show: false
            },
            axisTicks: {
                show: true,
            },
            labels: {
                show: true,
                formatter: function(val) {
                    return parseFloat(val);
                }
            }

        },

        fill: {
            type: 'gradient',
            gradient: {
                shade: 'light',
                gradientToColors: ['#fff'],
                shadeIntensity: 1,
                type: 'vertical',
                opacityFrom: 0.8,
                opacityTo: 0.2,
                stops: [0, 100, 100, 100]
            },
        },
        colors: ['#fff'],
        grid: {
            show: true,
            borderColor: 'rgba(255, 255, 255, 0.12)',
        },
        tooltip: {
            theme: 'dark',
            x: {
                show: false
            },

        },
        title: {
            text: 'Humidity Change Today'
        }
    }

    var HumChart = new ApexCharts(
        document.querySelector("#hum-day"),
        optionsHum
    );

    HumChart.render();


    function loadCharts() {
        var url = '/reading/temperature/';
        $.getJSON(url, function(response) {
            var temperature = parseFloat(response.value).toFixed(2);
            console.log('Temperature:' + temperature);
            var temp_date = new Date(response.date_time).getTime() - 7200000;
            $('#temp_datetime').html(new Date(temp_date).toLocaleString('de-DE'));
            temp_chart.updateSeries([temperature]);
        });

        var url = '/reading/humidity/';
        $.getJSON(url, function(response) {
            var humidity = parseFloat(response.value).toFixed(2);
            console.log("humidity=" + humidity);
            var hum_date = new Date(response.date_time).getTime() - 7200000;
            $('#humidity').html(humidity + " gm<sup>-3</sup>");
            $('#h-datetime').html(new Date(hum_date).toLocaleString('de-DE'));
        });

        var url = '/reading/co2/';
        $.getJSON(url, function(response) {
            var co2 = parseFloat(response.value).toFixed(2);
            console.log("co2=" + co2);
            var co2_date = new Date(response.date_time).getTime() - 7200000;
            $('#co2').html(co2 + " Ppm");
            $('#co2-datetime').html(new Date(co2_date).toLocaleString('de-DE'));
        });

        //co2 data for the day, ploted on the graph
        var url = '/read-day/co2/';
        $.getJSON(url, function(response) {

            var co2Day = [];
            response.forEach(function(item, index) {

                var reading = parseFloat(item.value).toFixed(2);
                co2Day.push({ x: new Date(item.date_time).getTime(), y: reading });

            });

            chart_co2.updateSeries([{
                name: '',
                data: co2Day // use the array for displaying data from mysql or .net remove the hard number-->
            }]);
        });


        //temp data for the day, ploted on the graph
        var url = '/read-day/temperature/';
        $.getJSON(url, function(response) {

            var tempDay = [];
            response.forEach(function(item, index) {

                var readingTemp = parseFloat(item.value).toFixed(2);
                tempDay.push({ x: new Date(item.date_time).getTime(), y: readingTemp });

            });

            tempHumChart.updateSeries([{
                name: '',
                data: tempDay // use the array for displaying data from mysql or .net remove the hard number-->
            }]);
        });


        //humidity data for the day, ploted on the graph
        var url = '/read-day/humidity';
        $.getJSON(url, function(response) {

            var humDay = [];
            response.forEach(function(item, index) {

                var readingHum = parseFloat(item.value).toFixed(2);
                humDay.push({ x: new Date(item.date_time).getTime(), y: readingHum });

            });

            HumChart.updateSeries([{
                name: '',
                data: humDay // use the array for displaying data from mysql or .net remove the hard number-->
            }]);
        });

    }


    loadCharts();
    setInterval(function() {
        loadCharts();
    }, 300000);



});