import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css'
import useSWR from 'swr'

const fetcher = (...args) => fetch(...args).then(res => res.json())

export async function getStaticProps() {
    const API_URL = "http://localhost:8088/system/webdev/Jakes_Project/api/daily-trend"
    const { data, error } = useSWR(API_URL, fetcher)
    //const response = await fetch(API_URL)
    //const data = await response.json()

    if(error) return <div>error</div>
    if(!data) return <div>loading...</div>

    
    console.log(data)
    if(!data) return (<div>Loading...</div>)

    
}

export default function DailyTrendChart({ options }) {
    console.log(options)

    return(
        <p>{options}</p>
    )
}

//export default DailyTrendChart;