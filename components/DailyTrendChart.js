import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css'
import useSWR from 'swr'
import { Line } from 'react-chartjs-2'

const fetcher = (...args) => fetch(...args).then(res => res.json())

export default function DailyTrendChart() {

    const API_URL = "http://localhost:8088/system/webdev/Jakes_Project/api/daily-trend"
    const { data, error } = useSWR(API_URL, fetcher)

    if(error) return <div>error</div>
    if(!data) return <div>loading...</div>

    let labels = []
    let DC_POWER = []
    let AC_POWER = []
    data.rows.forEach(row => {
        const split = row[0].split(' ') 
        labels.push(split[1])
        DC_POWER.push(row[1])
        AC_POWER.push(row[2])
    })

    const chartData = {
        labels: labels,
        datasets: [
          {
            label: 'DC Power',
            fill: false,
            lineTension: 0.1,
            backgroundColor: 'rgba(75,192,192,0.4)',
            borderColor: 'rgba(75,192,192,1)',
            borderCapStyle: 'butt',
            borderDash: [],
            borderDashOffset: 0.0,
            borderJoinStyle: 'miter',
            pointBorderColor: 'rgba(75,192,192,1)',
            pointBackgroundColor: '#fff',
            pointBorderWidth: 1,
            pointHoverRadius: 5,
            pointHoverBackgroundColor: 'rgba(75,192,192,1)',
            pointHoverBorderColor: 'rgba(220,220,220,1)',
            pointHoverBorderWidth: 2,
            pointRadius: 1,
            pointHitRadius: 10,
            data: DC_POWER
          },
          {
            label: 'AC Power',
            fill: false,
            lineTension: 0.1,
            backgroundColor: 'rgba(255,71,26,0.4)',
            borderColor: 'rgba(255,71,26,1)',
            borderCapStyle: 'butt',
            borderDash: [],
            borderDashOffset: 0.0,
            borderJoinStyle: 'miter',
            pointBorderColor: 'rgba(255,71,26,1)',
            pointBackgroundColor: '#fff',
            pointBorderWidth: 1,
            pointHoverRadius: 5,
            pointHoverBackgroundColor: 'rgba(255,71,26,1)',
            pointHoverBorderColor: 'rgba(220,220,220,1)',
            pointHoverBorderWidth: 2,
            pointRadius: 1,
            pointHitRadius: 10,
            data: AC_POWER
          }
        ]
    };

    return(
        <div>
            <Line data={chartData}></Line>
        </div>
    )
}